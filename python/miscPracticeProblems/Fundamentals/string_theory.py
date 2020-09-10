string = "Saul"


def string_theory(string):
    return True if len(string) > 3 and string[0] == "S" else False


print(string_theory(string))
