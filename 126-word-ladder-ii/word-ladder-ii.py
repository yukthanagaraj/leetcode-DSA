from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # BFS to build parent graph (which words can lead to each word at shortest path)
        layer = {beginWord}
        parents = defaultdict(set)
        found = False
        
        while layer and not found:
            wordSet -= layer  # remove visited words
            next_layer = set()
            for word in layer:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            next_layer.add(newWord)
                            parents[newWord].add(word)
                            if newWord == endWord:
                                found = True
            layer = next_layer
        
        if not found:
            return []
        
        # Backtrack from endWord to beginWord using parent map
        results = []
        def backtrack(word, path):
            if word == beginWord:
                results.append(list(reversed(path)))
                return
            for parent in parents[word]:
                path.append(parent)
                backtrack(parent, path)
                path.pop()
        
        backtrack(endWord, [endWord])
        return results