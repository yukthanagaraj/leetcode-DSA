class Solution:
    def isNumber(self, s):
        try:
            num = float(s)

            # Invalid special values
            if s.lower() in ["inf", "+inf", "-inf",
                             "infinity", "+infinity", "-infinity",
                             "nan"]:
                return False

            return True
        except:
            return False


# Example Usage
obj = Solution()

print(obj.isNumber("0"))           # True
print(obj.isNumber("2e10"))        # True
print(obj.isNumber("-0.1"))        # True
print(obj.isNumber("abc"))         # False
print(obj.isNumber("1e"))          # False
print(obj.isNumber("-Infinity"))   # False
        