from classes.FileSystemHandler import FileSystemHandler


class DiffGeneratorException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Diff:
    def __init__(self, file_path, revision_id_1, revision_id_2, lcs_array, content_1, content_2):
        self.file_path = file_path
        self.revision_id_1 = revision_id_1
        self.revision_id_2 = revision_id_2
        self.lcs_array = lcs_array
        self.content_1 = content_1
        self.content_2 = content_2


class DiffGenerator:
    @classmethod
    def generate_diff(cls, file_path, revision_id_1, revision_id_2):
        revision1_content = FileSystemHandler.read_revision_content(file_path, revision_id_1)
        revision2_content = FileSystemHandler.read_revision_content(file_path, revision_id_2)
        lcs_array = cls.__generate_lcs_array(revision1_content, revision2_content)
        # lcs = cls.__generate_lcs(lcs_array, revision1_content, revision2_content)
        return Diff(file_path, revision_id_1, revision_id_2, lcs_array, revision1_content, revision2_content)

    @classmethod
    def __generate_lcs_array(cls, seq1, seq2):
        c = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

        for i in range(1, len(seq1) + 1):
            for j in range(1, len(seq2) + 1):
                if seq1[i - 1] == seq2[j - 1]:
                    c[i][j] = c[i - 1][j - 1] + 1
                else:
                    c[i][j] = max(c[i - 1][j], c[i][j - 1])

        return c

    @classmethod
    def __generate_lcs(cls, lcs_array, seq1, seq2):
        return cls.__generate_lcs_inner(lcs_array, seq1, seq2, len(seq1), len(seq2))

    @classmethod
    def __generate_lcs_inner(cls, lcs_array, seq1, seq2, i, j):
        if i == 0 or j == 0:
            return []
        elif seq1[i - 1] == seq2[j - 1]:
            arr = cls.__generate_lcs_inner(lcs_array, seq1, seq2, i - 1, j - 1)
            arr.append(seq1[i - 1])
            return arr
        else:
            if lcs_array[i][j - 1] > lcs_array[i - 1][j]:
                return cls.__generate_lcs_inner(lcs_array, seq1, seq2, i, j - 1)
            else:
                return cls.__generate_lcs_inner(lcs_array, seq1, seq2, i - 1, j)

    # TODO fix it?
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
