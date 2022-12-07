
using DirectoryMapper;
using System.Text.RegularExpressions;
using Directory = DirectoryMapper.Directory;

var directoryStructure = CreateDirectoryStructure();

var totalSizeOnDisk = directoryStructure.TotalDirectorySize;
var diskSize = 70000000;

var freeSpace = diskSize - totalSizeOnDisk;
var requiredSpace = 30000000;



var total = GetTotalSizeOfAllDirsUnderSize(directoryStructure, 100000);
Console.WriteLine(total);

var minSizeDirectory = GetSmallestDirectorySizeToFreeUpSpace(directoryStructure, requiredSpace - freeSpace);
Console.WriteLine(minSizeDirectory);

Directory CreateDirectoryStructure()
{
    var inputLines = System.IO.File.ReadAllLines("input.txt");

    //input lines are one of 4 patterns:
    // $ cd <dir> - where <dir> is either '/' (set current dir to root), '..' (go to current dir's parent), <dir name> (go to subdirectory with given name in current directory)
    // $ ls - no-op
    // dir <dirName> - declares subdirectory in current directory
    // <size> <filename> - declares filename with given size

    var root = new Directory("/", null);

    Directory currentDirectory = root;
    var fileRegex = new Regex("^([0-9]+)\\s([A-Za-z0-9.]+)$");

    foreach (var line in inputLines)
    {
        if (string.IsNullOrWhiteSpace(line))
        {
            continue;
        }

        string dirName;

        switch (line)
        {
            case var _ when line.StartsWith(Constants.ChangeDir):
                dirName = line.Replace(Constants.ChangeDir, string.Empty);
                currentDirectory = ChangeDir(dirName, currentDirectory, root);         
                break;

            case var _ when line.StartsWith(Constants.List):
                break;

            case var _ when line.StartsWith(Constants.Dir):
                dirName = line.Replace(Constants.Dir, string.Empty);
                currentDirectory.SubDirectories.Add(new Directory(dirName, currentDirectory));
                break;

            case var _ when fileRegex.IsMatch(line):
                var match = fileRegex.Match(line);
                currentDirectory.Files.Add(new DirectoryMapper.File(match.Groups[2].Value, int.Parse(match.Groups[1].Value)));
                break;
        }
    }

    return root;
}

int GetTotalSizeOfAllDirsUnderSize(Directory currentDir, int maxSize)
{
    var directoryTotal = 0;

    if(currentDir.TotalDirectorySize <= maxSize)
    {
        directoryTotal += currentDir.TotalDirectorySize;
    }

    foreach(var dir in currentDir.SubDirectories)
    {
        directoryTotal += GetTotalSizeOfAllDirsUnderSize(dir, maxSize);
    }

    return directoryTotal;
}

int GetSmallestDirectorySizeToFreeUpSpace(Directory currentDirectory, int minSize)
{
    var currentMin = int.MaxValue;

    if(minSize <= 0)
    {
        return 0;
    }

    if (currentDirectory.TotalDirectorySize > minSize && currentDirectory.TotalDirectorySize < currentMin)
    {
        currentMin = currentDirectory.TotalDirectorySize;
    }

    foreach(var dir in currentDirectory.SubDirectories)
    {
        currentMin = Math.Min(currentMin, GetSmallestDirectorySizeToFreeUpSpace(dir, minSize));
    }

    return currentMin;

}

Directory ChangeDir(string dirName, Directory currentDirectory, Directory root)
{
    if (dirName == "/")
    {
        return root;
    }
    else if (dirName == "..")
    {
        return currentDirectory.ParentDirectory;
    }
    else
    {
        return currentDirectory.SubDirectories.FirstOrDefault(dir => dir.Name.Equals(dirName));
    }
}


