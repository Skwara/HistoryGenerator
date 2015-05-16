from io import StringIO
from pprint import pprint
import tokenize


def print_2d_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print('{:4}'.format(array[i][j]), end="")
        print("\n")


class Parser:
    @staticmethod
    def generate_tokens(content):
        tokens = []
        inner_tokens = tokenize.generate_tokens(StringIO(content).readline)
        for token_type, token_value, token_begin, token_end, token_line in inner_tokens:
            tokens.append(Token(token_type, token_value, token_begin, token_end, token_line))

        return tokens

    @staticmethod
    def lcs_array(seq1, seq2):
        c = [[0 for x in range(len(seq1) + 1)] for x in range(len(seq2) + 1)]

        for i in range(1, len(c)):
            for j in range(1, len(c[0])):
                if seq1[i - 1] == seq2[j - 1]:
                    c[i][j] = c[i - 1][j - 1] + 1
                else:
                    c[i][j] = max(c[i - 1][j], c[i][j - 1])

        return c

    @staticmethod
    def resolve_lcs(seq, lcs_array):
        i = len(lcs_array) - 1
        j = len(lcs_array[0]) - 1
        lcs = []

        while not (i == 0 and j == 0):
            if i == 0:
                j -= 1
            elif j == 0:
                i -= 1
            else:
                if lcs_array[i][j - 1] == lcs_array[i][j]:
                    j -= 1
                elif lcs_array[i - 1][j] == lcs_array[i][j]:
                    i -= 1
                else:
                    lcs.append(seq[j - 1])
                    i -= 1
                    j -= 1

        return lcs


class Token:
    def __init__(self, tok_type, tok_value, tok_begin, tok_end, tok_line):
        self.type = tokenize.tok_name[tok_type]
        self.value = tok_value
        self.begin = tok_begin
        self.end = tok_end
        self.line = tok_line

    def __str__(self):
        return str(self.begin) + "-" + str(self.end) + ": " + str(self.type) + " - " + self.value

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value

# content1 = open("tests/samples/sample_1.py").read()
# content2 = open("tests/samples/sample_2.py").read()
#
# tokens1 = Parser.generate_tokens(content1)
# tokens2 = Parser.generate_tokens(content2)
#
# lcs_array = Parser.lcs_array(tokens1, tokens2)
#
# print_2d_array(lcs_array)

content1 = "abcdefgh"
content2 = "abcdifgh"

lcs_array = Parser.lcs_array(content1, content2)

print_2d_array(lcs_array)

lcs = Parser.resolve_lcs(content1, lcs_array)

pprint(lcs)
