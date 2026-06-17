class Solution:
    def numUniqueEmails(self, emails):
        unique = set()

        for email in emails:
            local, domain = email.split("@")

            # Ignore everything after '+'
            if '+' in local:
                local = local.split('+')[0]

            # Remove dots
            local = local.replace('.', '')

            # Add final email
            unique.add(local + '@' + domain)

        return len(unique)