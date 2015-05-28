class Shape:
    def radius(self, r):
        return r * r * 3.1415

    def area(self, x, y):
        return x * y

    def __str__(self):
        return "x&Y"

class Token:
    def __init__(self, tok_type, tok_value, tok_begin, tok_end, tok_line):
        self.type = tokenize.tok_name[tok_type]
        self.value = tok_value
        self.begin = tok_begin
        self.end = tok_end
        self.line = tok_line

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.value == other.value
