#!/usr/bin/python3
def print_hidden():
    import hidden_4
    for name in dir(hidden_4):
        if name[0] != "_":
            print(name)


if __name__ == "__main__":
    print_hidden()
