class TernaryTrieNode:
    def __init__(self, value: str):
        self.value: str = value
        self.next: TernaryTrieNode | None = None
        self.left: TernaryTrieNode | None = None
        self.right: TernaryTrieNode | None = None
        self.total_build_operations = 0
        self.total_pointer_units = 3
        self.end: bool = False

    def insert(self, word: str):
        i = 0
        cur_node = self

        while i < len(word):
            # Handle root edge case
            if cur_node.value == "ROOT":
                self.value = word[i]
                continue

            self.total_build_operations += 1 
            if word[i] < cur_node.value:
                if cur_node.left is None:
                    cur_node.left = TernaryTrieNode(word[i])
                    self.total_pointer_units += 3
                    self.total_build_operations += 2

                cur_node = cur_node.left
                continue

            self.total_build_operations += 1 
            if word[i] > cur_node.value:
                if cur_node.right is None:
                    cur_node.right = TernaryTrieNode(word[i])
                    self.total_pointer_units += 3
                    self.total_build_operations += 2

                cur_node = cur_node.right
                continue

            self.total_build_operations += 1

            if i == len(word) - 1:
                cur_node.end = True
                self.total_build_operations += 1 
                break

            i += 1

            if cur_node.next is None:
                cur_node.next = TernaryTrieNode(word[i])
                self.total_pointer_units += 3
                self.total_build_operations += 2

            cur_node = cur_node.next

    def search(self, word: str):
        i = 0
        cur_node = self

        total_operations = 0
        
        while i < len(word):
            total_operations += 1
            if word[i] < cur_node.value:
                if cur_node.left is None:
                    return (False, total_operations)

                cur_node = cur_node.left
                continue

            total_operations += 1
            if word[i] > cur_node.value:
                if cur_node.right is None:
                    return (False, total_operations)

                cur_node = cur_node.right
                continue

            total_operations += 1

            if i == len(word) - 1:
                total_operations += 1 
                return (cur_node.end, total_operations)

            i += 1

            if cur_node.next is None:
                return (False, total_operations)

            cur_node = cur_node.next

        return (False, total_operations)

    def autocomplete(self, prefix: str):
        pass