text = "asdfasff"


def checkPalindrome(text):
    if len(text) % 2 == 0:
        k = int(len(text)/2 )   
    else:
        k = len(text)//2 + 1

    i = 0
    j = len(text) - 1 
    print(k)
    for x in range(k):
        if text[i] != text[j]:
            return False
        i+=1
        j-=1
    return True

print(checkPalindrome(text))
print(text)
