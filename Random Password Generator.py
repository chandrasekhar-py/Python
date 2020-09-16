print("Welcome to my random password generater, this program will generate 6-digit passwords with random symbols, letters and numbers!")

i = False
while i == False:

    i = input("Type Y and press enter to generate a password")
    if i == "Y" or i =="y":
    
        from random import randint

        letters = ["a","b", "c", "d", "d", "e" , "f", "g", "h", "j", "k", "l", "m", "n", "o", "p",
        "q", "s", "t", "v", "u", "v", "w", "x", "y", "z"]
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        symbols = ["!", "@", "#", "$", "%", "&"]
        Capletters = ["Q", "W", "E", "R" , "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]

        x = letters[randint(0,23)]    
        y = numbers[randint(0,8)]
        z = Capletters[randint(0,23)]
        q = symbols[randint(0,5)]
        w = letters[randint(0,23)]
        e = numbers[randint(0,8)]

        f = (x,y,z,q,w,e)
        print(f[0], f[1], f[2], f[3], f[4], f[5])
    
    i = False
