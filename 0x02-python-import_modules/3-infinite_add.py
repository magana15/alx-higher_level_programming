#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    def car():#carrier
        total = 0
        for i in range(1,len(sys.argv)):
            total += int(sys.argv[i])
        print(total)
        car()

