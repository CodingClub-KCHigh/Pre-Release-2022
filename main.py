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

# ------------- TASK 2 ------------------
num_holes_played = 1
while num_holes >= 0:
    print(f"\n{num_holes_played} hole(s) has been played")
    for name in names:
        stroke_1 = int(input(f"{name} enter the number of strokes you played: "))
        stroke_2 = int(input("Enter the number of strokes again to confirm: "))
        while stroke_1 != stroke_2:
            print("Error. Both strokes are not equal.")
            stroke_1 = int(input(f"{name} enter the number of strokes: "))
            stroke_2 = int(input(f"{name} enter the number of strokes again to confirm: "))
        scores[names.index(name)] += stroke_2
        choice = input("Do you wish to see the total number of strokes you have played? (y/n): ")
        if choice == "y":
            print(f"{name}'s total strokes is {scores[names.index(name)]}")
        print("Strokes entered successfully")
    print(f"You have {num_holes-1} holes left to play")
    num_holes-=1
    num_holes_played+=1
# ---------------------------------------------
