class ArrayTrieNode:
    def __init__(self, value: str):
        self.value: str = value
        self.children: list[ArrayTrieNode | None] = [None] * 26
        self.end: bool = False

    def insert(self, word: str):
        pass
    
    def search(self, word: str):
        pass