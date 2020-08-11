#https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
        #self.children = collections.defaultdict(TrieNode)
class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True
        # node = self.root
        # for i in word:
        #     node = node.children[i]
        # node.word = True

    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word

    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True
            
    
    # Your Trie object will be instantiated and called as such:
    # trie = Trie()
    # trie.insert("somestring")
    # trie.search("key")