
namespace DirectoryMapper
{
    internal class Directory
    {
        private int _totalFileSize = -1;
        private int _totalSubDirectorySize = -1;

        public Directory(string name, Directory? parent)
        {
            Name = name;
            ParentDirectory= parent;
        }
        public string Name { get; init; }
        
        public IList<File> Files { get; init; } = new List<File>();

        public IList<Directory> SubDirectories { get; init; } = new List<Directory>();

        public Directory? ParentDirectory { get; init; }

        public int TotalDirectorySize
        {
            get { return GetTotalFileSize() + GetTotalSubDirectoriesSize(); }
        }

        private int GetTotalFileSize()
        {
            if (_totalFileSize != -1)
            {
                return _totalFileSize;
            }

            _totalFileSize = Files.Sum(file => file.Size);
            return _totalFileSize;
        }

        private int GetTotalSubDirectoriesSize()
        {
            if (_totalSubDirectorySize!= -1)
            {
                return _totalSubDirectorySize;
            }

            _totalSubDirectorySize = 0;

            foreach(var subDir in SubDirectories)
            {
                _totalSubDirectorySize += subDir.GetTotalFileSize() + subDir.GetTotalSubDirectoriesSize();
            }

            return _totalSubDirectorySize;
        }
    }
}
