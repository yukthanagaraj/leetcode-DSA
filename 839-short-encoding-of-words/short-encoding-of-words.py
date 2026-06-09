class TrieNode:
    def __init__(self):
        self.children = {}


class Solution:
    def minimumLengthEncoding(self, words):
        
        root = TrieNode()
        total = 0
        
        # Remove duplicates
        words = list(set(words))
        
        # Store reversed words in trie
        for word in words:
            node = root
            
            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            
            # mark end of word
            node.word = word
        
        # DFS count only leaf nodes
        def dfs(node):
            length = 0
            
            if not node.children:
                return len(node.word) + 1
            
            for child in node.children.values():
                length += dfs(child)
            
            return length
        
        return dfs(root)