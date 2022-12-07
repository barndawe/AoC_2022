namespace DirectoryMapper
{
    internal class File
    {
        public File(string name, int size)
        {
            Name = name;
            Size = size;
        }

        public string Name { get; init; }
        public int Size { get; init; }
    }
}
