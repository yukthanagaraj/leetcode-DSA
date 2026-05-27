class Solution:
    def strongPasswordChecker(self, password):

        n = len(password)

        # check missing character types
        missing_lower = 1
        missing_upper = 1
        missing_digit = 1

        for ch in password:
            if ch.islower():
                missing_lower = 0
            elif ch.isupper():
                missing_upper = 0
            elif ch.isdigit():
                missing_digit = 0

        missing_types = missing_lower + missing_upper + missing_digit

        # find repeating sequences
        replace = 0
        one_mod = 0
        two_mod = 0

        i = 2

        chars = list(password)

        while i < n:
            if chars[i] == chars[i - 1] == chars[i - 2]:

                length = 2

                while i < n and chars[i] == chars[i - 1]:
                    length += 1
                    i += 1

                replace += length // 3

                if length % 3 == 0:
                    one_mod += 1
                elif length % 3 == 1:
                    two_mod += 1
            else:
                i += 1

        # case 1: too short
        if n < 6:
            return max(missing_types, 6 - n)

        # case 2: valid length
        elif n <= 20:
            return max(missing_types, replace)

        # case 3: too long
        else:
            delete = n - 20

            remaining_delete = delete

            # remove from groups where len % 3 == 0
            use = min(remaining_delete, one_mod)
            replace -= use
            remaining_delete -= use

            # remove from groups where len % 3 == 1
            use = min(remaining_delete // 2, two_mod)
            replace -= use
            remaining_delete -= use * 2

            # remove from remaining groups
            replace -= remaining_delete // 3

            return delete + max(missing_types, replace)