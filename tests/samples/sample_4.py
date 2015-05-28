class Shape:
    def area(self, x, y):
        return z * y

class Token:
    def __init__(self, tok_type, tok_value, tok_begin, tok_end, tok_line):
        self.type = tokenize.tok_name[tok_type]
        self.value = tok_value
        self.begin = tok_begin
        self.end = tok_end
        self.line = tok_line

    def __str__(self):
        return self.value
        # return str(self.begin) + "-" + str(self.end) + ": " + str(self.type) + " - " + self.value

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value