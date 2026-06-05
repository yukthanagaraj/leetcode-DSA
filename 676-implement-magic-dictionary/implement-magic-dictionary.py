class MagicDictionary:

    def __init__(self):
        self.words = []

    def buildDict(self, dictionary):
        self.words = dictionary

    def search(self, searchWord):
        for word in self.words:
            if len(word) != len(searchWord):
                continue

            diff = 0
            for a, b in zip(word, searchWord):
                if a != b:
                    diff += 1
                    if diff > 1:
                        break

            if diff == 1:
                return True

        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)