import random

x = random.randint(0, 999)
winner = 777
print(x)

if x == winner:
    print(f"Now that was lucky... congrats, i guess")
else:
    print(f"You're not the lottery winner")