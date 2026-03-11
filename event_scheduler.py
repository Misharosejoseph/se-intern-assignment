def can_attend_all(events):

    events.sort()

    for i in range(1,len(events)):
        if events[i][0] < events[i-1][1]:
            return False

    return True



def min_rooms_required(events):

    if not events:
        return 0

    start = sorted([e[0] for e in events])
    end = sorted([e[1] for e in events])

    s = 0
    e = 0
    rooms = 0
    max_rooms = 0

    while s < len(events):

        if start[s] < end[e]:
            rooms += 1
            max_rooms = max(max_rooms,rooms)
            s += 1
        else:
            rooms -= 1
            e += 1

    return max_rooms
if __name__ == "__main__":

    events = [(9,10),(10,11),(11,12)]

    print("Can attend all:", can_attend_all(events))

    events2 = [(9,11),(10,12),(11,13)]

    print("Minimum rooms:", min_rooms_required(events2))