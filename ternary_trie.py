class TernaryTrieNode:
    def __init__(self, value: str):
        self.value: str = value
        self.next: TernaryTrieNode | None = None
        self.left: TernaryTrieNode | None = None
        self.right: TernaryTrieNode | None = None
        self.end: bool = False

    def insert(self, word: str):
        i = 0
        cur_node = self

        while i < len(word):
            # Handle root edge case
            if cur_node.value == "ROOT":
                self.value = word[i]
                continue

            if word[i] < cur_node.value:
                if cur_node.left is None:
                    cur_node.left = TernaryTrieNode(word[i])

                cur_node = cur_node.left
                continue

            if word[i] > cur_node.value:
                if cur_node.right is None:
                    cur_node.right = TernaryTrieNode(word[i])
                
                cur_node = cur_node.right
                continue

            if i == len(word) - 1:
                cur_node.end = True
                break

            i += 1

            if cur_node.next == None:
                cur_node.next = TernaryTrieNode(word[i])
                
            cur_node = cur_node.next

    def search(self, word: str):
        pass

    def autocomplete(self, prefix: str):
        pass