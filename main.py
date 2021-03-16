def PassBuffer(password):
    newpass = password
    for i in password:
        newpass += str(ord(i))
    passlen = len(newpass)
    characterlist= ["@", "$", "^", "*", "!", ")", "#", "&", "-", "(", "^%", "&$", "@^",
                    "&!","'&", "$", "^", "*", "!", ")", "#", "&", "-", "^%", "&$", "@^"]
    letterCombos = ["Sy", "Br", "hE", "zY", "JK", "Pw", "zo", "Vp","u", "x", "p", "w", "i", "Sy", "Br",
                    "hE", "zY", "JK", "Pw", "zo", "Vp","u" ]
    numbers = ["12", "2", "53", "76", "374", "8", "0", "9", "63", "5", "12", "2", "53", " 76", "374"]
    ASCI = []
    listpass = []
    for letter in newpass:
        listpass.append(letter)

    for character in newpass:
        temp = str(ord(character))
        ASCI.append(temp[-1])

    for i in range(0, passlen, 2):
        listpass[i] = characterlist[int(ASCI[i])]

    for i in range(0, passlen, 3):
        listpass[i] = letterCombos[int(ASCI[i])]

    for i in range(0, passlen, 4) :
        listpass[i] = numbers[int(ASCI[i])]
    finalpass = "".join(listpass)

    return finalpass

print(PassBuffer("luca"))


