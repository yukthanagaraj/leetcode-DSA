

class Solution:
    def expressiveWords(self, s, words):
        
        def stretchy(word):
            i = j = 0

            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    return False

                i1, j1 = i, j

                while i1 < len(s) and s[i1] == s[i]:
                    i1 += 1
                while j1 < len(word) and word[j1] == word[j]:
                    j1 += 1

                cnt_s = i1 - i
                cnt_w = j1 - j

                if cnt_s < 3:
                    if cnt_s != cnt_w:
                        return False
                else:
                    if cnt_w > cnt_s:
                        return False

                i, j = i1, j1

            return i == len(s) and j == len(word)

        return sum(stretchy(word) for word in words)