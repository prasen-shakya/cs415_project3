class TernaryTrieNode:
    def __init__(self, value: str):
        self.value: str = value
        self.next: TernaryTrieNode | None = None
        self.left: TernaryTrieNode | None = None
        self.right: TernaryTrieNode | None = None
        self.end: bool = False

    def insert(self, word: str):
        pass

    def search(self, word: str):
        pass

    def autocomplete(self, prefix: str):
        pass