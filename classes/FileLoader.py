class FileLoader:
    def __init__(self, source_file_path):
        self.source_file_path = source_file_path
        self.source_file = None
        self.content = None

        self.__read_file_content()

    def __read_file_content(self):
        self.source_file = open(self.source_file_path, 'r')
        self.content = self.source_file.read()
