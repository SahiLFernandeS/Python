# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()

combined = lower_name1 + lower_name2

t = combined.count('t')
r = combined.count('r')
u = combined.count('u')
e = combined.count('e')

true = t + r + u + e

l = combined.count('l')
o = combined.count('o')
v = combined.count('v')
e = combined.count('e')

love = l + o + v + e

per = str(true) + str(love)

percent = int(per)

if percent >= 90 or percent <= 10:
  print(f"Your score is {percent}, you go together like coke and mentos.")
elif percent >= 40 and percent <= 50:
  print(f"Your score is {percent}, you are alright together..")
else:
  print(f"your score is {percent}")