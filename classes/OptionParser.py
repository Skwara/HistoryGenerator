class OptionParser:
    def __init__(self, input_line):
        self.input_line = input_line
        self.__check_for_errors()

    def __check_for_errors(self):
        pass

    @property
    def is_verbose(self):
        pass

    @property
    def is_add(self):
        pass

    @property
    def is_diff(self):
        pass

    @property
    def file_name(self):
        pass

    @property
    def revision_id_1(self):
        pass

    @property
    def revision_id_2(self):
        pass
