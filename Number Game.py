import random

n1 = random.randint(1,100)
n2 = random.randint(1,100)

p1 = input("Player 1: ")
p2 = input("Player 2: ")

g1 = 22
g2 = 22

s1 = 0
s2 = 0

print("player 1 turn")

while g1 != n1:
    g1 = int(input("guess the num: "))
    s1 = s1 + 1

    if g1 < n1:
        print("Too low")
    elif g1 > n1:
        print("Too high")

print("Correct!")

print("player 2 turn")

while g2 != n2:
    g2 = int(input("guess the num: "))
    s2 = s2 + 1

    if g2 < n2:
        print("Too low")
    elif g2 > n2:
        print("Too high")

print("Correct!")

if s1 > s2:
    print(p2, "wins")
elif s2 > s1:
    print(p1, "wins")
else:
    print("draw")
  