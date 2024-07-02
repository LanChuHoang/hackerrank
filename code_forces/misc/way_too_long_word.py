n = int(input())
for _ in range(n):
    word = input()
    l = len(word)
    if l <= 10:
        print(word)
    else:
        print(word[0], l - 2, word[-1], sep="")
