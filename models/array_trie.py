class ArrayTrieNode:
    def __init__(self, value: str):
        self.value: str = value
        self.children: list[ArrayTrieNode | None] = [None] * 26
        self.end: bool = False

        self.total_build_operations = 0
        self.total_pointer_units = 26

    def insert(self, word: str):
        cur_node: ArrayTrieNode = self

        for c in word:
            ch_index = ord(c) - ord('a')

            child = cur_node.children[ch_index]
            self.total_build_operations += 1

            # If the child doesn't exist, create it and update the children array
            if child is None:
                self.total_pointer_units += 26
                child = ArrayTrieNode(c)
                self.total_build_operations += 1
                cur_node.children[ch_index] = child
                self.total_build_operations += 1

            cur_node = child

        cur_node.end = True
        self.total_build_operations += 1

    def search(self, word: str):
        cur_node: ArrayTrieNode = self
        total_operations = 0

        for c in word:
            ch_index = ord(c) - ord('a')

            child = cur_node.children[ch_index]

            total_operations += 1

            if child is None:
                return (False, total_operations)

            cur_node = child

        total_operations += 1
        return (cur_node.end, total_operations)

    def autocomplete(self, prefix: str) -> tuple[list[str], int]:
        res = []

        # Get to the prefix node
        cur_node: ArrayTrieNode = self
        total_operations = 0

        for c in prefix:
            ch_index = ord(c) - ord('a')

            child = cur_node.children[ch_index]
            total_operations += 1

            # If there are no more children, we can't autocomplete anything else
            if child is None:
                return (res, total_operations)

            cur_node = child


        def dfs(node: ArrayTrieNode, path: list[str]):
            nonlocal total_operations
            total_operations += 1
            if node.end:
                res.append(prefix + "".join(path))

            for child in node.children:
                total_operations += 1
                if child is not None:
                    path.append(child.value)
                    dfs(child, path)
                    path.pop()
            
        dfs(cur_node, [])
        return (res, total_operations)