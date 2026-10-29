import argparse

parser = argparse.ArgumentParser()

parser.add_argument("input_filename")
parser.add_argument("flag", type=int)

args = parser.parse_args()

print(args.input_filename)
print(args.flag)
