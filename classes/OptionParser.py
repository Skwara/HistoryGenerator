class OptionParser:
    def __init__(self, arguments):
        self.arguments = arguments
        self.__check_for_errors()

    def __check_for_errors(self):
        # TODO it can be optional...
        pass

    @property
    def is_verbose(self):
        # TODO
        pass

    @property
    def is_add(self):
        # TODO
        pass

    @property
    def is_diff(self):
        # TODO
        pass

    @property
    def file_path(self):
        # TODO
        pass

    @property
    def revision_id_1(self):
        # TODO
        pass

    @property
    def revision_id_2(self):
        # TODO
        pass
