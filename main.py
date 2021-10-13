# ------------- TASK 1 ------------------
num_players = int(input("Enter the number of players taking part: "))
while num_players > 4 or num_players < 2:
    num_players = int(input("Error. Only 2, 3 or 4 people play at one given time. Re enter the number of players playing: "))
num_holes = int(input("Enter the number of holes to be played (9/18): "))
names = []
scores = [0]*num_players
for count in range(0, num_players):
    name = input(f"Enter player {count+1}'s name': ")
    names.append(name)
    
while num_holes != 9 and num_holes != 18:
    num_holes = int(input("Error. Only 9 or 18 holes may be played: Re enter the number of holes to be played: "))
par = int(input("Enter the par for the course: "))
print(f"There will be {num_players} people playing")
for name in names:
    print(f"{name} will be playing")
print(f"The number of holes to be played is {num_holes}")
print(f"The par for the course is {par}")
# ---------------------------------------------