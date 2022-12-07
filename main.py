import sys
if __name__ == "__main__":
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        input = f.read()
    print(eval(input))