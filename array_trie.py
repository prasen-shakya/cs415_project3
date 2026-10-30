class ArrayTrieNode:
    def __init__(self, value: str):
        self.value: str = value
        self.children: list[ArrayTrieNode | None] = [None] * 26
        self.end: bool = False

    def insert(self, word: str):
        cur_node: ArrayTrieNode = self
        total_operations = 0

        for c in word:
            ch_index = ord(c) - ord('a')

            child = cur_node.children[ch_index]

            # If the child doesn't exist, create it and update the children array
            if child is None:
                child = ArrayTrieNode(c)
                cur_node.children[ch_index] = child

            cur_node = child
            total_operations += 1

        cur_node.end = True

        return total_operations
 
    def search(self, word: str):
        cur_node: ArrayTrieNode = self
        total_operations = 0
        autocomplete_results = []

        for c in word:
            ch_index = ord(c) - ord('a')

            child = cur_node.children[ch_index]

            total_operations += 1

            if child is None:
                return (False, total_operations, autocomplete_results)

            cur_node = child

        autocomplete_results = self.autocomplete(cur_node, word)
        return (cur_node.end, total_operations, autocomplete_results)

    def autocomplete(self, cur_node: ArrayTrieNode, prefix: str) -> list[str]:
        res = []

        def dfs(node: ArrayTrieNode, path: list[str]):
            if node.end:
                res.append(prefix + "".join(path))

            for child in node.children:
                if child is not None:
                    path.append(child.value)
                    dfs(child, path)
                    path.pop()
            
        dfs(cur_node, [])
        return res