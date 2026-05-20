class Solution:
    def simplifyPath(self, path):
        stack = []

        # Split path by "/"
        for part in path.split("/"):

            # Ignore empty parts and "."
            if part == "" or part == ".":
                continue

            # Go back to parent directory
            elif part == "..":
                if stack:
                    stack.pop()

            # Valid directory name
            else:
                stack.append(part)

        # Build canonical path
        return "/" + "/".join(stack)