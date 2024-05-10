class TrieNode:
    def __init__(self):
        self.children={}
        self.isEOW=False

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        crawl=self.root

        for c in word:
            if c not in crawl.children:
                crawl.children[c]=TrieNode()
            crawl=crawl.children[c]
        
        crawl.isEOW=True

    def search(self, word: str) -> bool:
        crawl=self.root

        for c in word:
            if c not in crawl.children:
                return False
            crawl=crawl.children[c]
        
        return crawl.isEOW

    def startsWith(self, prefix: str) -> bool:
        crawl=self.root

        for c in prefix:
            if c not in crawl.children:
                return False
            crawl=crawl.children[c]
        
        return True
