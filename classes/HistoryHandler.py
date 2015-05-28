from classes.FileSystemHandler import FileSystemHandler, FileSystemHandlerException
from classes.DiffGenerator import DiffGenerator, DiffGeneratorException
from classes.DiffPrinter import DiffPrinter


class HistoryHandlerException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class HistoryHandler:
    def __init__(self):
        self.diff = None

    @staticmethod
    def add_to_history(file_path):
        try:
            FileSystemHandler.add_to_history(file_path)
        except FileSystemHandlerException as e:
            print("Error: adding to history failed")
            print("\t" + str(e))
            raise HistoryHandlerException("HistoryHandler failed")

    def generate_diff(self, file_path, revision_id_1, revision_id_2):
        try:
            self.diff = DiffGenerator.generate_diff(file_path, revision_id_1, revision_id_2)
        except DiffGeneratorException as e:
            print("Error: generating diff failed")
            print("\t" + str(e))
            raise HistoryHandlerException("HistoryHandler failed")

    def print_diff(self, opt):
        if opt.is_verbose:
            DiffPrinter.print_verbose_diff(self.diff, opt.verbose_separator, opt.verbose_padding)
        elif opt.is_json_verbose:
            DiffPrinter.print_json_verbose_diff(self.diff)
        else:
            DiffPrinter.print_basic_diff(self.diff)
