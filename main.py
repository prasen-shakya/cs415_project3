import argparse
import string
from array_trie import ArrayTrieNode

parser = argparse.ArgumentParser()

parser.add_argument("input_file")
parser.add_argument("flag", type=int)

args = parser.parse_args()

words = []
translator = str.maketrans('', '', string.punctuation)

try:
    with open(f"./input/{args.input_file}") as file:
        for line in file:
            words_in_line = line.split()

            for word in words_in_line:
                normalized_word = word.lower().translate(translator)

                if normalized_word != "":
                    words.append(normalized_word)
except FileNotFoundError:
    print(f"Error: The file '{args.input_file}' was not found.")
    exit(1)

root = ArrayTrieNode("ROOT")

for word in words:
    root.insert(word)

print(f"Time taken to build the standard Trie is {root.total_build_operations} operations and space occupied by it is {root.total_pointer_units} pointer units")
print()

while True:
    try:
        search_string = input("Enter search string: ")
    except (EOFError, KeyboardInterrupt):
        break

    search_string = search_string.strip().lower().translate(translator)
    success, search_operations = root.search(search_string)
    autocomplete_results, autocomplete_operations = root.autocomplete(search_string)
    print()
    print(f"Time taken to search in the standard Trie is {search_operations} operations")
    print(f"Auto-complete results using standard Trie are: {", ".join(autocomplete_results)}")
    print(f"Time taken to find auto-complete results in the standard Trie is {autocomplete_operations} operations")
    print()
