def accommodate(*guests, **rooms):
    unsuccessful_accommodations = 0
    sorted_rooms = sorted(rooms.items(), key=lambda x: (x[1], x[0]))
    room_accommodations = {}
    for guest in guests:
        for room in sorted_rooms:
            if room[1] >= guest:
                room_accommodations[room[0][-3:]] = guest
                sorted_rooms.remove(room)
                break
        else:
            unsuccessful_accommodations += guest

    result = []
    if room_accommodations:
        result.append(f"A total of {len(room_accommodations)} accommodations were completed!")
        for room, guests in sorted(room_accommodations.items()):
            result.append(f"<Room {room} accommodates {guests} guests>")
    else:
        result.append("No accommodations were completed!")
    if unsuccessful_accommodations:
        result.append(f"Guests with no accommodation: {unsuccessful_accommodations}")
    if sorted_rooms:
        result.append(f"Empty rooms: {len(sorted_rooms)}")

    return "\n".join(result)

print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))