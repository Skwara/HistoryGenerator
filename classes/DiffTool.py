class DiffTool:
    @staticmethod
    def lcs_array(seq1, seq2):
        c = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

        for i in range(1, len(seq1) + 1):
            for j in range(1, len(seq2) + 1):
                if seq1[i - 1] == seq2[j - 1]:
                    c[i][j] = c[i - 1][j - 1] + 1
                else:
                    c[i][j] = max(c[i - 1][j], c[i][j - 1])

        return c

    @staticmethod
    def lcs(lcs_array, seq1, seq2, i, j):
        if i == 0 or j == 0:
            return []
        elif seq1[i - 1] == seq2[j - 1]:
            arr = DiffTool.lcs(lcs_array, seq1, seq2, i - 1, j - 1)
            arr.append(seq1[i - 1])
            return arr
        else:
            if lcs_array[i][j - 1] > lcs_array[i - 1][j]:
                return DiffTool.lcs(lcs_array, seq1, seq2, i, j - 1)
            else:
                return DiffTool.lcs(lcs_array, seq1, seq2, i - 1, j)

    # @staticmethod
    # def lcs_all(lcs_array, seq1, seq2, i, j):
    #     if i == 0 or j == 0:
    #         return {""}
    #     elif seq1[i - 1] == seq2[j - 1]:
    #         return set([z + seq1[i-1] for z in DiffTool.lcs_all(lcs_array, seq1, seq2, i - 1, j - 1)])
    #     else:
    #         r = set()
    #         if lcs_array[i][j - 1] >= lcs_array[i - 1][j]:
    #             r.update(DiffTool.lcs_all(lcs_array, seq1, seq2, i, j - 1))
    #         if lcs_array[i - 1][j] >= lcs_array[i][j - 1]:
    #             r.update(DiffTool.lcs_all(lcs_array, seq1, seq2, i - 1, j))
    #         return r

    @staticmethod
    def print_diff_default(lcs_array, seq1, seq2, i, j):
        if i > 0 and j > 0 and seq1[i-1] == seq2[j-1]:
            DiffTool.print_diff_default(lcs_array, seq1, seq2, i-1, j-1)
            print("  " + str(seq1[i-1]))
        else:
            if j > 0 and (i == 0 or lcs_array[i][j-1] >= lcs_array[i-1][j]):
                DiffTool.print_diff_default(lcs_array, seq1, seq2, i, j-1)
                print("+ " + str(seq2[j-1]))
            elif i > 0 and (j == 0 or lcs_array[i][j-1] < lcs_array[i-1][j]):
                DiffTool.print_diff_default(lcs_array, seq1, seq2, i-1, j)
                print("- " + str(seq1[i-1]))

    @staticmethod
    def print_diff(lcs_array, seq1, seq2, i, j):
        if i > 0 and j > 0 and seq1[i-1] == seq2[j-1]:
            DiffTool.print_diff(lcs_array, seq1, seq2, i-1, j-1)
            print(" " + str(seq1[i-1]), end="")
        else:
            if j > 0 and (i == 0 or lcs_array[i][j-1] >= lcs_array[i-1][j]):
                DiffTool.print_diff(lcs_array, seq1, seq2, i, j-1)
                print(" +" + str(seq2[j-1]), end="")
            elif i > 0 and (j == 0 or lcs_array[i][j-1] < lcs_array[i-1][j]):
                DiffTool.print_diff(lcs_array, seq1, seq2, i-1, j)
                print(" -" + str(seq1[i-1]), end="")
