class Solution:
    def addBinary(self, a, b):
        # Convert binary strings to integers
        num1 = int(a, 2)
        num2 = int(b, 2)

        # Add them
        total = num1 + num2

        # Convert back to binary and remove '0b'
        return bin(total)[2:]


# Example Usage
obj = Solution()

print(obj.addBinary("11", "1"))        # Output: "100"
print(obj.addBinary("1010", "1011"))   # Output: "10101"