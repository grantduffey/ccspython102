hotel = {
    '1': {
        '185': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}

check = input("Do you want to check in or check out? Type (in/out) | ")
floor = ""
room = ""

numOcc = 0
occupants = []
if check.upper() == "IN":
    while True:
        floor = input("What floor number? | ")
        room = input("What room number? | ")
        if room in hotel[floor[0]]:
            print("Room occupied! Please choose another room. \n")
            continue
        break
    numOcc = int(input("How many occupants? | "))
    i = 1
    while i < (numOcc + 1):
        name = input("What is the name of occupant %d? | " % i)
        occupants.append(name)
        i += 1
    hotel[floor] = {room: occupants}
    
if check.upper() == "OUT":
    while True:
        floor = input("What floor number? | ")
        room = input("What room number? | ")
        if room not in hotel[floor[0]]:
            print("Room is not occupied! Please choose the correct room. \n")
            continue
        break
    del hotel[floor][room]

print(hotel)