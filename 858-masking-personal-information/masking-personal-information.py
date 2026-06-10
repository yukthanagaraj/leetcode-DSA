class Solution:
    def maskPII(self, s):
        
        # Email
        if '@' in s:
            name, domain = s.lower().split('@')
            
            return name[0] + "*****" + name[-1] + "@" + domain
        
        # Phone
        digits = ""
        
        for ch in s:
            if ch.isdigit():
                digits += ch
        
        local = digits[-10:]
        country = len(digits) - 10
        
        result = "***-***-" + local[-4:]
        
        if country > 0:
            result = "+" + "*" * country + "-" + result
        
        return result