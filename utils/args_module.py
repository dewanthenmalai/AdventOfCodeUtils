import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzle", help="The puzzle to solve", type=int)
    parser.add_argument("-t", "--test", action="store_true", help="Use test input file")
    args = parser.parse_args()
    return args