#the rooms names and their tempratures
rooms = {"Golden Gate":70, "Great Hall":55, "Times Square":40, "Stonehenge":19}

def heat_up(room):

    #it will increase the temp of the room by 5 degrees
    #find the room in the dictionary, if it's there 
    #add 5 to temp for that room
    #else return an error

    #option1 loop through key and values in the rooms dictionary
    #until we find the room, if we never find it in the loop
    #return error
    for current_room, temp in rooms.items(): #thats how you access keys and values in a dictionary
        print(current_room)
        print(temp)
        if current_room == room:
            rooms[room] = rooms[room] + 5
            return room
        else:
            return "error"

    #option2 we could check if room is in rooms.keys()
#     if room in rooms.keys():
#         #add 5 to it
#         rooms[room] = rooms[room] + 5 
#     else:
#         return "error"

def cool_down(room):
    if room in rooms.keys():
        #subtract 5 from it
        rooms[room] = rooms[room] - 5
    else:
        return "Error"

    


heat_up("Great Hall")
print(rooms)
cool_down("Times Square")
print(rooms)