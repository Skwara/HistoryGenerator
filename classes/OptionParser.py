class OptionParser:
    def __init__(self, arguments):
        self.arguments = arguments
        self.__check_for_errors()

    def __check_for_errors(self):
        # TODO it can be optional...
        pass

    def __check_for_arg(self, arg_name):
        return arg_name in self.arguments and self.arguments[arg_name] is not None

    @property
    def is_verbose(self):
        return self.__check_for_arg('verbose')

    @property
    def is_add(self):
        return self.__check_for_arg('add')

    @property
    def is_diff(self):
        return self.__check_for_arg('diff')

    @property
    def file_path(self):
        # TODO Extract parsing method
        if 'add' in self.arguments and self.arguments['add'] is not None:
            return self.arguments['add'][0]
        elif 'diff' in self.arguments and self.arguments['diff'] is not None:
            return self.arguments['diff'][0]
        else:
            # TODO Think of better name
            return "---"

    @property
    def revision_id_1(self):
        if 'diff' in self.arguments and self.arguments['diff'] is not None:
            return self.arguments['diff'][1]
        else:
            return "---"

    @property
    def revision_id_2(self):
        if 'diff' in self.arguments and self.arguments['diff'] is not None:
            return self.arguments['diff'][2]
        else:
            return "---"

    # For debug
    # def check(self):
    #     print("is_verbose: " + str(self.arguments))
    #     print("is_verbose: " + str(self.is_verbose))
    #     print("is_add: " + str(self.is_add))
    #     print("is_diff: " + str(self.is_diff))
    #     print("file_path: " + str(self.file_path))
    #     print("revision_id_1: " + self.revision_id_1)
    #     print("revision_id_2: " + self.revision_id_2)
