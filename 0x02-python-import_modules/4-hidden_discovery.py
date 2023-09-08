#!/usr/bin/python3

if __name__ == "__main__":
    """all names defined in the hidden_4 is printed"""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
