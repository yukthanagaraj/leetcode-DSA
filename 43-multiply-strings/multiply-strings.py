class Solution:
    def multiply(self, num1, num2):

        # if any number is 0
        if num1 == "0" or num2 == "0":
            return "0"

        n1 = len(num1)
        n2 = len(num2)

        result = [0] * (n1 + n2)

        # multiply from right to left
        for i in range(n1 - 1, -1, -1):

            for j in range(n2 - 1, -1, -1):

                mul = int(num1[i]) * int(num2[j])

                pos1 = i + j
                pos2 = i + j + 1

                total = mul + result[pos2]

                result[pos2] = total % 10
                result[pos1] += total // 10

        # convert list to string
        answer = ""

        for num in result:

            # skip leading zeros
            if not (len(answer) == 0 and num == 0):
                answer += str(num)

        return answer