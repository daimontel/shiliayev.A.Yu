def rle_encode(s: str) -> str:
    if not s:
        return ""
    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            
            result.append(f"{s[i - 1]}{count}")
            count = 1

    
    result.append(f"{s[-1]}{count}")

    return "".join(result)


# использования
print(rle_encode("aaabbc"))      
print(rle_encode("abcd"))        
print(rle_encode("aaaa"))        
print(rle_encode(""))            
