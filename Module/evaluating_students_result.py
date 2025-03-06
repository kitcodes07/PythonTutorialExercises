



class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    # Write your code here.
    def __init__(self, line_number, line):
        super().__init__()
        self.line_number = line_number
        self.line = line


class FileEmpty(StudentsDataException):
    # Write your code here.
    def __init__(self):
        super().__init__()


from os import strerror

try:
    scores = {}
    src = input("Enter Prof. Jekyll's filename: ")
    s = open(src, "r")
    lines = s.readlines()
    s.close()
    if len(lines) == 0:
        raise FileEmpty()

    for i in range(len(lines)):
        line = lines[i].split()
        if len(line) != 3:
            raise BadLine(i+1,lines[i])

        student = f"{line[0]} {line[1]}"

        try:
            score = float(line[2])
        except ValueError:
            raise BadLine(i+1,lines[i])

        if student in scores:
            scores[student] += score
        else:
            scores[student] = score

    ol = sorted(scores.keys())
    for student in ol:
        print(f"{student}\t\t{scores[student]}")


except IOError as e:
    print("Can't access the file:", strerror(e.errno))
    exit(e.errno)
except FileEmpty:
    print("The file is empty!")

except BadLine as bl:
    print(f"Bad Line #{bl.line_number}: {bl.line}")
