class Solution:
    def spellchecker(self, wordlist, queries):

        exact = set(wordlist)

        case_map = {}
        vowel_map = {}

        def mask(word):
            res = []
            for ch in word.lower():
                if ch in "aeiou":
                    res.append("*")
                else:
                    res.append(ch)
            return "".join(res)

        # Build maps
        for word in wordlist:
            lower = word.lower()

            if lower not in case_map:
                case_map[lower] = word

            m = mask(word)

            if m not in vowel_map:
                vowel_map[m] = word


        ans = []

        for query in queries:

            # 1. Exact match
            if query in exact:
                ans.append(query)

            # 2. Case match
            elif query.lower() in case_map:
                ans.append(case_map[query.lower()])

            # 3. Vowel match
            elif mask(query) in vowel_map:
                ans.append(vowel_map[mask(query)])

            else:
                ans.append("")

        return ans