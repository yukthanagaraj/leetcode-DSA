class Solution:
    def numRabbits(self, answers):
        count = {}

        for ans in answers:
            count[ans] = count.get(ans, 0) + 1

        result = 0

        for ans, freq in count.items():
            group_size = ans + 1

            # Number of groups needed
            groups = (freq + group_size - 1) // group_size

            result += groups * group_size

        return result