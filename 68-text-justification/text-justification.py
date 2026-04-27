class Solution(object):
    def fullJustify(self, words, maxWidth):
        lines = []
        i = 0

        # Step 1: Group words into lines
        while i < len(words):
            line_len = len(words[i])
            j = i + 1
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            lines.append(words[i:j])
            i = j

        result = []

        for k, line in enumerate(lines):
            # Step 2: Last line or single word — left-justify
            if k == len(lines) - 1 or len(line) == 1:
                result.append(" ".join(line).ljust(maxWidth))
                continue

            # Step 3: Middle lines — distribute spaces evenly
            total_spaces = maxWidth - sum(len(w) for w in line)
            gaps = len(line) - 1
            space, extra = divmod(total_spaces, gaps)

            justified = ""
            for m, word in enumerate(line[:-1]):
                justified += word + " " * (space + (1 if m < extra else 0))
            justified += line[-1]
            result.append(justified)

        return result
        