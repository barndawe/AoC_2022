#pragma once
#include <vector>
#include <string>

std::vector<std::vector<bool>> Create2dVisibilityVector(size_t height, size_t width);
std::vector<std::vector<int>> Create2dScenicVector(size_t height, size_t width);
std::vector<std::vector<int>> Create2dTreeVectorFromStrings(std::vector<std::string> const* lines);
void CalculateVisibility(std::vector<std::vector<int>> const* treeHeights, std::vector<std::vector<bool>>* treeVisibility);
void CalculateScenics(std::vector<std::vector<int>> const* treeHeights, std::vector<std::vector<int>>* scenics);
