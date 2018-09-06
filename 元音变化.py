import re
yuanyin = ('a','e','i','o','u')
yuanyin2 = ('a','e','i','o','u','y')
def zhaoy(word):
    for a in word:
        if word[0] == y:
            continue
        elif a == y:
            return 1
def quchufuyin(word):
    n = 1 
    if len(word) == 1:
        return word + 'ay'
    else:
        while(word[n] not in yuanyin2):
            n += 1
            if n == (len(word) - 1):
                break
        newword = word[n:] + word[:n] + 'ay'
        return newword
word = ("请输入一段单词")
for a in word:
    if word[0] in yuanyin:
        

        
