def isAnagram(s,t):
        
        if len(s) != len(t):
            return False
        
        dic1 = {}
        dic2 = {}
        
        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] = 1
            else:
                dic1[s[i]] = dic1[s[i]] + 1
        
        for i in range(len(t)):
            if t[i] not in dic2:
                dic2[t[i]] = 1
            else:
                dic2[t[i]] = dic2[t[i]] + 1
                
        if dic1 == dic2:
            return True
        else:
            return False

print(isAnagram("tay","art"))