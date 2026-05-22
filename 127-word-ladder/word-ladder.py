from collections import deque

class Solution:
    def ladderLength(self,beginWord,endWord,wordList):
        wordSet = set(wordList)

        # If endWord not present, return 0
        if endWord not in wordSet:
            return 0

        queue = deque()
        queue.append((beginWord, 1))  # (current_word, steps)

        while queue:
            word, steps = queue.popleft()

            # Try changing each character
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + ch + word[i+1:]

                    # If reached endWord
                    if newWord == endWord:
                        return steps + 1

                    # If valid word, add to queue
                    if newWord in wordSet:
                        queue.append((newWord, steps + 1))
                        wordSet.remove(newWord)  # mark visited

        return 0