class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if n1 == 0:
            return 0

        index = 0          # current position in s2
        count_s2 = 0       # number of completed s2 matches

        recall = {}

        s1_count = 0

        while s1_count < n1:
            s1_count += 1

            for ch in s1:
                if ch == s2[index]:
                    index += 1

                    if index == len(s2):
                        count_s2 += 1
                        index = 0

            if index in recall:
                prev_s1_count, prev_s2_count = recall[index]

                cycle_s1 = s1_count - prev_s1_count
                cycle_s2 = count_s2 - prev_s2_count

                remaining = n1 - s1_count

                cycles = remaining // cycle_s1

                count_s2 += cycles * cycle_s2
                s1_count += cycles * cycle_s1
            else:
                recall[index] = (s1_count, count_s2)

        return count_s2 // n2