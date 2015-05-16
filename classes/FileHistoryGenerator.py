from classes.FileLoader import FileLoader
from classes.FileParser import FileParser


class FileHistoryGenerator:
    def __init__(self, source_file):
        self.file_loader = FileLoader(source_file)
        self.file_parser = FileParser(self.file_loader.content)
