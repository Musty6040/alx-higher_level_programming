#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    item = len(sys.argv)
    if item == 1:
        print("{} arguments.".format(item - 1))
    elif item == 2:
        print("{} argument:".format(item - 1))
    else:
        print("{} arguments:".format(item - 1))

    for i in range(1, item):
        print("{}: {}".format(i, sys.argv[i]))
