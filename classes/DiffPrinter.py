from tokenize import untokenize
from termcolor import colored, cprint
from classes.Token import TokenStatus
from enum import Enum
import colorama


class DiffPrinter:
    class _DiffState(Enum):
        Same = 0,
        Added = 1,
        Removed = 2

    @classmethod
    def print_verbose_diff(cls, diff, separator, padding):
        colorama.init()
        cls.separator = separator
        cls.padding = padding
        cls.__print_diff_verbose(diff.lcs_array, diff.content_1, diff.content_2,
                                 len(diff.content_1), len(diff.content_2))

    @classmethod
    def print_basic_diff(cls, diff):
        tokens = []
        cls.__prepare_tokens(tokens, diff.lcs_array, diff.content_1, diff.content_2,
                             len(diff.content_1), len(diff.content_2))
        output = cls.__prepare_output_colors(tokens)
        print(output)

    @classmethod
    def __print_diff_verbose(cls, lcs_array, seq1, seq2, i, j):
        if i > 0 and j > 0 and seq1[i - 1] == seq2[j - 1]:
            cls.__print_diff_verbose(lcs_array, seq1, seq2, i - 1, j - 1)
            cls.__do_print(seq1[i - 1], cls._DiffState.Same)
        else:
            if j > 0 and (i == 0 or lcs_array[i][j - 1] >= lcs_array[i - 1][j]):
                cls.__print_diff_verbose(lcs_array, seq1, seq2, i, j - 1)
                cls.__do_print(seq2[j-1], cls._DiffState.Added)
            elif i > 0 and (j == 0 or lcs_array[i][j - 1] < lcs_array[i - 1][j]):
                cls.__print_diff_verbose(lcs_array, seq1, seq2, i - 1, j)
                cls.__do_print(seq1[i - 1], cls._DiffState.Removed)

    @classmethod
    def __prepare_tokens(cls, tokens, lcs_array, content_1, content_2, i, j):
        if i > 0 and j > 0 and content_1[i - 1] == content_2[j - 1]:
            cls.__prepare_tokens(tokens, lcs_array, content_1, content_2, i - 1, j - 1)
            token = content_1[i - 1]
            tokens.append(token)
        else:
            if j > 0 and (i == 0 or lcs_array[i][j - 1] >= lcs_array[i - 1][j]):
                cls.__prepare_tokens(tokens, lcs_array, content_1, content_2, i, j - 1)
                token = content_2[j - 1]
                token.status = TokenStatus.added
                tokens.append(token)
            elif i > 0 and (j == 0 or lcs_array[i][j - 1] < lcs_array[i - 1][j]):
                cls.__prepare_tokens(tokens, lcs_array, content_1, content_2, i - 1, j)
                token = content_1[i - 1]
                token.status = TokenStatus.removed
                tokens.append(token)

    @classmethod
    def __prepare_output_signs(cls, tokens):
        untokenize_input = []
        for token in tokens:
            if token.status == TokenStatus.not_changed:
                untokenize_input.append([token.type, token.value])
            elif token.status == TokenStatus.added:
                untokenize_input.append([token.type, "+" + token.value])
            elif token.status == TokenStatus.removed:
                untokenize_input.append([token.type, "-" + token.value])

        return untokenize(untokenize_input)

    @classmethod
    def __prepare_output_colors(cls, tokens):
        colorama.init()
        untokenize_input = []
        for token in tokens:
            if token.status == TokenStatus.not_changed:
                untokenize_input.append([token.type, token.value])
            elif token.status == TokenStatus.added:
                untokenize_input.append([token.type, colored(token.value, 'green')])
            elif token.status == TokenStatus.removed:
                untokenize_input.append([token.type, colored(token.value, 'red')])

        return untokenize(untokenize_input)

    @classmethod
    def __do_print(cls, value, diff_state):
        diff_char = ''
        if diff_state == cls._DiffState.Same:
            diff_char = '='
        elif diff_state == cls._DiffState.Added:
            diff_char = '+'
        elif diff_state == cls._DiffState.Removed:
            diff_char = '-'

        # Optional replacements for better readability. To be discussed.
        token = value.value.replace('\n', '\\n')
        if str(value.type_str) == "INDENT":
            token = "INDENT"
        elif str(value.type_str) == "DEDENT":
            token = "DEDENT"
        elif str(value.type_str) == "ENDMARKER":
            token = "ENDMARKER"

        print("%s%c%s%c%s%c%s%c%s%c%s" %
               (str(diff_char).ljust(cls.padding),
                cls.separator,
                str(value.type_str).ljust(cls.padding),
                cls.separator,
                str(value.begin[0]).ljust(cls.padding),
                cls.separator,
                str(value.begin[1]).ljust(cls.padding),
                cls.separator,
                str(value.end[1]).ljust(cls.padding),
                cls.separator,
                str(token).ljust(cls.padding)))
