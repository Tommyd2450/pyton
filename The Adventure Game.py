room_list = []
# room = []
room = ["You are in your messy bedroom with your pet cat sparkles, you see another room to the north, and a hallway to the east.",3,1,None,None]
room_list.append(Bedroom)
room = ["You feel slightly lazy standing on the dirty colthes from last week and you feel like playing games in your gaming room.",4,2,None,0]
room_list.append(Messy Hallway)
room = ["As you pass by you smell the wonderful sent of flowers on top of the shelf feeling refreshed as you feel determined to go game, you are now in the bathroom staring out the window as the sun light shines in the tub.",5,None,None,1]
room_list.append(Bathroom)
room = ["Now you’re in the gaming room you see nothing but the LGB lights in the edges of the room and seeing the game has to restart so there is no point of playing anymore but feeling sleepy",None,4,0,None]
room_list.append(Gaming room)
room = ["As you step into the Sparkles territory you see her playing with the yarn ball and as you admire her cuteness you smell as if an atomic bomb has exploded while you stare at the litter box", 6,5,1,3]
room_list.append(Sparkles Domain)
room = ["While stepping in the kitchen you feel slightly hungry but as tingly feeling makes you think twice as if a beast was about to attack, as you turn you see Sparkles sitting on top of the fridge and you don’t feel as hungry as you were before",None,None,2,4]
room_list.append(Kitchen)
room = ["Stepping out of the house you feel the cool breeze of air and you don’t smell the stickiness from Sparkles litter no more, and see the whole neighborhood and the sun view from afar and as you enjoy this moment you took a photo of you with sparkles in the beautiful sunset", None,None,4,1]
room_list.append(Balcony)

current_room = 0

done = False
next_room = ""

while not done:
    print()
    print(room_list[current_room][0])
    direction = input("What do you want to do? ")
    if direction == "n":
        next_room = room_list[current_room][1]
    elif direction == "e":
        next_room = room_list[current_room][2]
    elif direction == "s":
        next_room = room_list[current_room][3]
    elif direction == "w":
        next_room = room_list[current_room][4]
    else:
        print()
        print("I don't understand.")
    if next_room == "none":
        print("You can't go that way!")
    current_room = next_room
