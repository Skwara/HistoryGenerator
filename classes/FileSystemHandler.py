class FileSystemHandlerException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class FileSystemHandler:
    @classmethod
    def add_to_history(cls, file_path):
        if not cls.__history_exists(file_path):
            cls.__create_history(file_path)

        rev_id = cls.__generate_revision_id(file_path)
        cls.__save_revision(rev_id, file_path)

    @classmethod
    def read_revision_content(cls, file_path, revision_id):
        # TODO
        # this has to return array of tokens
        pass

    @classmethod
    def __history_exists(cls, file_path):
        # TODO
        # discover a way for differentiate file histories not only by file name but file path
        pass

    @classmethod
    def __create_history(cls, file_path):
        # TODO
        pass

    @classmethod
    def __generate_revision_id(cls, file_path):
        # TODO
        pass

    @classmethod
    def __save_revision(cls, rev_id, file_path):
        # TODO
        # file path is needed for copying the file from it's source
        pass
