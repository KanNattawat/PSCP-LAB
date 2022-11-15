""" pscp """

def main(num, txt):
    """ main """
    char = "abcdefghijklmnopqrstuvwxyz"
    char += char
    ans = ""
    for i in txt:
        while num > 26:
            num -= 26
        if i == " ":
            ans += " "
        elif i.isupper():
            ans += (char[char.find(i.lower())+num]).upper()
        elif i.islower():
            ans += char[char.find(i)+num]
        else:
            ans += i
    return ans

print(main(int(input()), input()))
