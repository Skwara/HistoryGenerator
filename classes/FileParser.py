from io import StringIO
import tokenize


class FileParser:
    def __init__(self, string):
        self.string = string
        self.__parse()

    def __parse(self):
        tokens = tokenize.generate_tokens(StringIO(self.string).readline)
        for token_type, token_value, token_begin, token_end, token_line in tokens:
            print(str(token_begin) + "-" + str(token_end) + ": " + str(tokenize.tok_name[token_type]) + " - " + token_value)
