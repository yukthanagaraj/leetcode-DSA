class Solution:
    def lengthLongestPath(self, input):
        max_len = 0

        # Stores current path length at each depth
        path_len = {0: 0}

        for line in input.split('\n'):

            # Find depth level
            depth = line.count('\t')

            # Remove tabs to get actual name
            name = line.lstrip('\t')

            if '.' in name:
                # It's a file
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                # It's a directory
                path_len[depth + 1] = path_len[depth] + len(name) + 1

        return max_len