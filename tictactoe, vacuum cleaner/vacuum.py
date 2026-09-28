rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"

def sense():
    return rooms[location]

def act(status):
    global location
    if status == "Dirty":
        rooms[location] = "Clean"
        print(f"Location {location}: Dirty -> Suck -> Clean")
    elif location == "A":
        location = "B"
        print("Location A: Clean -> Move Right -> B")
    elif location == "B":
        location = "A"
        print("Location B: Clean -> Move Left -> A")

print("Initial:", rooms, "| Vacuum at", location)
for step in range(6):
    status = sense()
    act(status)

print("Final:", rooms)
