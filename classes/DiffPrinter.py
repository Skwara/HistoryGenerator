class DiffPrinter:
    @classmethod
    def print_verbose_diff(cls, diff):
        # TODO
        # Diff class is used here
        pass

    @classmethod
    def print_basic_diff(cls, diff):
        # TODO
        # Diff class is used here
        pass

    # TODO modify input to take diff object or use it at the lowest level getting data from diff object first
    @classmethod
    def __print_diff_default(cls, lcs_array, seq1, seq2):
        cls.__print_diff_default_inner(lcs_array, seq1, seq2, len(seq1), len(seq2))

    # TODO modify input to take diff object or use it at the lowest level getting data from diff object first
    @classmethod
    def __print_diff(cls, lcs_array, seq1, seq2):
        cls.__print_diff_inner(lcs_array, seq1, seq2, len(seq1), len(seq2))

    @classmethod
    def __print_diff_default_inner(cls, lcs_array, seq1, seq2, i, j):
        if i > 0 and j > 0 and seq1[i-1] == seq2[j-1]:
            cls.__print_diff_default_inner(lcs_array, seq1, seq2, i-1, j-1)
            print("  " + str(seq1[i-1]))
        else:
            if j > 0 and (i == 0 or lcs_array[i][j-1] >= lcs_array[i-1][j]):
                cls.__print_diff_default_inner(lcs_array, seq1, seq2, i, j-1)
                print("+ " + str(seq2[j-1]))
            elif i > 0 and (j == 0 or lcs_array[i][j-1] < lcs_array[i-1][j]):
                cls.__print_diff_default_inner(lcs_array, seq1, seq2, i-1, j)
                print("- " + str(seq1[i-1]))

    @classmethod
    def __print_diff_inner(cls, lcs_array, seq1, seq2, i, j):
        if i > 0 and j > 0 and seq1[i-1] == seq2[j-1]:
            cls.__print_diff_inner(lcs_array, seq1, seq2, i-1, j-1)
            print(" " + str(seq1[i-1]), end="")
        else:
            if j > 0 and (i == 0 or lcs_array[i][j-1] >= lcs_array[i-1][j]):
                cls.__print_diff_inner(lcs_array, seq1, seq2, i, j-1)
                print(" +" + str(seq2[j-1]), end="")
            elif i > 0 and (j == 0 or lcs_array[i][j-1] < lcs_array[i-1][j]):
                cls.__print_diff_inner(lcs_array, seq1, seq2, i-1, j)
                print(" -" + str(seq1[i-1]), end="")
