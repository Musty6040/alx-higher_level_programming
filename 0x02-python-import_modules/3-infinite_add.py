#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = 0
    for i in range(1, len(sys.argv)):
        args += int(sys.argv[i])
    print("{}".format(args))
