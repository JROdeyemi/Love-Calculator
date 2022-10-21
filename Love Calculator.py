# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1.lower()
name2.lower()

T = (int(name1.count('t')) + int(name2.count('t')))
R = (int(name1.count('r')) + int(name2.count('r')))
U = (int(name1.count('u')) + int(name2.count('u')))
E = (int(name1.count('e')) + int(name2.count('e')))

L = (int(name1.count('l')) + int(name2.count('l')))
O = (int(name1.count('o')) + int(name2.count('o')))
V = (int(name1.count('v')) + int(name2.count('v')))
E = (int(name1.count('e')) + int(name2.count('e')))

true = (T + R + U + E)
love = (L + O + V + E)

newtrue = str(true)
newlove = str(love)

truelove = (newtrue + newlove)

newtruelove = int(truelove)

if newtruelove < 10 or newtruelove > 90:
    print(f'Your score is {newtruelove}, you go together like coke and mentos.')
elif newtruelove > 40 and newtruelove < 50:
    print(f'Your score is {newtruelove}, you are alright together')
else:
    print(f'Your score is {newtruelove}.')
