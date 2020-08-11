# https://leetcode.com/problems/add-and-search-word-data-structure-design/

class TrieNode:
    def __init__(self):
        self.eword = False
        self.children = defaultdict(TrieNode)
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for i in word:
            node = node.children[i]
        node.eword = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
    
        ans = None  
        def dfs(node, word):
            nonlocal ans

            if ans == True:
                return

            if not word:
                ans = node.eword
                return

            ch = word[0]
            if ch == ".":
                for node in node.children.values():
                    dfs(node, word[1:])

            else:
                if ch in node.children:
                    dfs(node.children[ch], word[1:])
                else:
                    return False
                    
        dfs(self.root, word)
        return ans         


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)