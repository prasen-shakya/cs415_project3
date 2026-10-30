import argparse
import string

parser = argparse.ArgumentParser()

parser.add_argument("input_file")
parser.add_argument("flag", type=int)

args = parser.parse_args()

words = []
translator = str.maketrans('', '', string.punctuation)

with open(f"./input/{args.input_file}") as file:
    for line in file:
        words_in_line = line.split()

        for word in words_in_line:
            normalized_word = word.lower().translate(translator)

            if normalized_word != "":
                words.append(normalized_word)

print(words)