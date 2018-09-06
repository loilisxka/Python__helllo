def hefa(c):
    for line in c:
        if ord(word[0]) >= 48 and ord(word[0]) <= 57:
            print ("第",line,"行为非法字符")
        else:
            print("true")
word = input("请输入字符（一行一串字符）")
words = ''

for line in iter(word):
    words = words + line + ''
c = words.split()
hefa(c)
