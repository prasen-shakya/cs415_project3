import argparse
import string
from models.array_trie import ArrayTrieNode
from models.ternary_trie import TernaryTrieNode

parser = argparse.ArgumentParser()

parser.add_argument("input_file",
                    help="Name of the text file to read words from.")
parser.add_argument("flag", type=int, choices=[1, 2],
                    help="1 = interactive search, 2 = search every word in the file")

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

array_root = ArrayTrieNode("ROOT")
ternary_root = TernaryTrieNode("ROOT")


for word in words:
    array_root.insert(word)

print(f"Time taken to build the standard Trie is {array_root.total_build_operations} operations and space occupied by it is {array_root.total_pointer_units} pointer units")
print()

if args.flag == 1:
    while True:
        try:
            search_string = input("Enter search string: ")
        except (EOFError, KeyboardInterrupt):
            break

        search_string = search_string.strip().lower().translate(translator)
        success, search_operations = array_root.search(search_string)
        autocomplete_results, autocomplete_operations = array_root.autocomplete(search_string)
        print()
        print(f"Time taken to search in the standard Trie is {search_operations} operations")
        print(f"Auto-complete results using standard Trie are: {", ".join(autocomplete_results)}")
        print(f"Time taken to find auto-complete results in the standard Trie is {autocomplete_operations} operations")
        print()
else:
    total_search_operations = 0 

    for word in words:
        total_search_operations += array_root.search(word)[1]

    print(f"Time taken to search all the strings in the standard Trie is {total_search_operations} operations")
