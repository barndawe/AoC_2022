
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "TreeHouseLocator.h"

using namespace std;

int main()
{
    ifstream input("input.txt");
    std::vector<string> lines;
    copy(istream_iterator<string>(input), istream_iterator<string>(), back_inserter(lines));

    auto treeHeights = Create2dTreeVectorFromStrings(&lines);

    //assuming the tree vector is rectangular (it should be!)
    auto treeVisibility = Create2dVisibilityVector(treeHeights.size(), treeHeights[0].size());
    auto scenics = Create2dScenicVector(treeHeights.size(), treeHeights[0].size());

    CalculateVisibility(&treeHeights, &treeVisibility);
    CalculateScenics(&treeHeights, &scenics);

    int visibleCount = 0;

    cout << "Visibility:\n";
    for (auto const& visRow : treeVisibility) {
        for (auto const visCol : visRow) {
            cout << visCol;

            if (visCol) {
                visibleCount++;
            }
         }
        cout << "\n";
    }

    cout << "\n\n" << "total visible:\n" << visibleCount;

    int maxScenic = 0;

    cout << "\n\nScenics:\n";
    for (auto const& scenicRow : scenics) {
        for (auto const scenicCol : scenicRow) {
            cout << scenicCol;

            if (scenicCol > maxScenic) {
                maxScenic = scenicCol;
            }
        }
        cout << "\n";
    }

    cout << "\n\n" << "Max Scenics:\n" << maxScenic;
}

vector<vector<bool>> Create2dVisibilityVector(size_t height, size_t width) {
    auto treeVisibility = vector<vector<bool>>(height-2, vector<bool>(width, false));

    //add true vectors to the top and bottom
    treeVisibility.emplace(treeVisibility.begin(), width, true);
    treeVisibility.emplace_back(width, true);

    //set the first and last elements in the inner vector to true, but skip the first and last rows
    for (auto h = 1; h < height-1; h++) {
        treeVisibility[h][0] = true;
        treeVisibility[h][treeVisibility[h].size() - 1] = true;
    }

    return treeVisibility;
}

vector<vector<int>> Create2dTreeVectorFromStrings(vector<string> const* lines) {
    vector<vector<int>> treeHeights;

    for (auto const& line : *lines) {
        auto const currentRow = vector<char>(line.begin(), line.end());

        auto currentRowAsInt = vector<int>();

        for (auto const& number : currentRow) {
            currentRowAsInt.emplace_back(number - '0');
        }
        treeHeights.emplace_back(currentRowAsInt);
    }

    return treeHeights;
}

void CalculateVisibility(vector<vector<int>> const* treeHeights, vector<vector<bool>>* treeVisibility) {
    //a tree is visible as long as the tree on the 'outside' of it is shorter than it is
    //once a tree isn't visible then trees further in can't be (from that direction anyway)

    size_t const& height = treeHeights->size();
    size_t const& width = treeHeights[0].size();

    int currentTallest = 0;

    //always start one row/column 'in' and cut of the first and last column/row of the search

    //top->bottom
    for (size_t w = 1; w < width - 1; w++) {
        currentTallest = (*treeHeights)[0][w];
        for (size_t h = 1; h < height - 1; h++) {
            if ((*treeHeights)[h][w] > currentTallest) {
                currentTallest = (*treeHeights)[h][w];
                (*treeVisibility)[h][w] = true;
            }
        }
    }

    //left->right
    for (size_t h = 1; h < height - 1; h++) {
        currentTallest = (*treeHeights)[h][0];
        for (size_t w = 1; w < width - 1; w++) {
            if ((*treeHeights)[h][w] > currentTallest) {
                currentTallest = (*treeHeights)[h][w];
                (*treeVisibility)[h][w] = true;
            }
        }
    }

    //right->left
    for (size_t h = 1; h < height - 1; h++) {
        currentTallest = (*treeHeights)[h][width - 1];
        for (size_t w = width - 2; w > 1; w--) {
            if ((*treeHeights)[h][w] > currentTallest) {
                currentTallest = (*treeHeights)[h][w];
                (*treeVisibility)[h][w] = true;
            }
        }
    }

    //bottom->top
    for (size_t w = 1; w < width - 1; w++) {
        currentTallest = (*treeHeights)[height-1][w];
        for (size_t h = height -2; h > 1; h--) {
            if ((*treeHeights)[h][w] > currentTallest) {
                currentTallest = (*treeHeights)[h][w];
                (*treeVisibility)[h][w] = true;
            }
        }
    }
}

vector<vector<int>> Create2dScenicVector(size_t height, size_t width) {
    return vector<vector<int>>(height, vector<int>(width, 0));
}

void CalculateScenics(std::vector<std::vector<int>> const* treeHeights, std::vector<std::vector<int>>* scenics) {
    //for each tree check how far up,down, left, and right you can go until you find a tree the same height or taller
    //(or an edge) and multiply.

    size_t const& height = treeHeights->size();
    size_t const& width = treeHeights[0].size();

    int currentTreeHeight;
    int searchingTreeHeight;
    int upVisible;
    int downVisible;
    int leftVisible;
    int rightVisible;
    size_t tempH;
    size_t tempW;

    //skip the edges again
    for (size_t h = 1; h < height - 1; h++) {
        for (size_t w = 1; w < width - 1; w++) {
            upVisible = downVisible = leftVisible = rightVisible = 0;
            tempH = h;
            tempW = w;

            currentTreeHeight = (*treeHeights)[h][w];

            //search up (h--)
            do
            {
                upVisible++;
                tempH--;
                searchingTreeHeight = (*treeHeights)[tempH][w];

            } while (tempH > 0 && searchingTreeHeight < currentTreeHeight);
            

            //search down (h++)
            tempH = h;

            do
            {
                downVisible++;
                tempH++;
                searchingTreeHeight = (*treeHeights)[tempH][w];

            } while (tempH < height - 1 && searchingTreeHeight < currentTreeHeight);

            //search left (w--)
            do
            {
                leftVisible++;
                tempW--;
                searchingTreeHeight = (*treeHeights)[h][tempW];

            } while (tempW > 0 && searchingTreeHeight < currentTreeHeight);

            //search right (w++)
            tempW = w;

            do
            {
                rightVisible++;
                tempW++;
                searchingTreeHeight = (*treeHeights)[h][tempW];

            } while (tempW < width - 1 && searchingTreeHeight < currentTreeHeight);

            //calculate and apply
            (*scenics)[h][w] = upVisible * downVisible * leftVisible * rightVisible;
        }
    }
}