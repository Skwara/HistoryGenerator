import os
import shutil
import tokenize
from io import StringIO
from classes.Token import Token


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
        file = open(cls.__history_path(file_path) + str(revision_id))
        return cls.__generate_tokens(file.read())
        pass

    @classmethod
    def __generate_tokens(cls, content):
        tokens = []
        inner_tokens = tokenize.generate_tokens(StringIO(content).readline)
        for token_type, token_value, token_begin, token_end, token_line in inner_tokens:
            tokens.append(Token(token_type, token_value, token_begin, token_end, token_line))

        return tokens

    @classmethod
    def __history_exists(cls, file_path):
        return os.path.isdir(cls.__history_path(file_path))

    @classmethod
    def __create_history(cls, file_path):
        os.makedirs(cls.__history_path(file_path))

    @classmethod
    def __generate_revision_id(cls, file_path):
        revisions = os.listdir(cls.__history_path(file_path))
        if not revisions:
            return 1
        else:
            return max([int(revision) for revision in revisions]) + 1

    @classmethod
    def __save_revision(cls, revision_id, file_path):
        shutil.copyfile(file_path, cls.__history_path(file_path) + str(revision_id))

    @classmethod
    def __history_path(cls, file_path):
        return "history/" + os.path.basename(file_path) + "/"
