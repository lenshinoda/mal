import sys


def READ(x):
    return x


def EVAL(x):
    return x


def PRINT(x):
    return x


def prep(x):
    stdin = READ(x)
    result = EVAL(stdin)
    printed = PRINT(result)
    return printed


if __name__ == "__main__":
    while True:
        try:
            user_input = input("user>")
            x = prep(user_input)
            print(x)
        except EOFError:
            sys.exit()
