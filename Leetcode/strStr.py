def strStr( haystack, needle):
        
    n1 = len(haystack)
    n2 = len(needle)
    ptr = 0 
    count = 0
    
    if n1 < n2 :
        return -1
    if needle == "":
        return 0
    
    while ptr < n1:
        if haystack[ptr] == needle[0]:
            index = ptr
            print(f"break")
            while count < n2 and ptr < n1:
                    if haystack[ptr] == needle[count]:
                        print(f"{haystack[ptr]}")
                        count +=1
                        ptr += 1
                    else:
                        count = 0
                        ptr -= 1
                        break
            if count == n2:
                return index
        ptr += 1
    return -1

print(strStr("mississippi","issip"))