slot = 0
parked = ["_"] * 15

def land():
    cnt = 0
    for i in range(1, 6):
        print(f"Lane {i}:", end=" ")
        for j in range(1, 4):
            print(parked[cnt], end="\t")
            cnt += 1
        print()
    print()

while slot < 15:
    opt = int(input("Parking Spots Choice Menu\n1. Parking\n2. Vehicle Return\n\tChoice: "))
    if opt == 1:
        vehicle = input("Enter The Vehicle Number: ")
        while parked[slot] != "_":  # Find the first empty slot
            slot += 1
        if parked[slot] == "_":
            parked[slot] = vehicle
            print(f"Vehicle can be parked at slot {slot}")
            land()

    elif opt == 2:
        vehicle = input("Enter The Vehicle Number: ")
        if vehicle in parked:
            slot = parked.index(vehicle)
            print(f"Vehicle found at slot: {slot}")
            parked[slot] = "_"
            land()  # Show parking lot after the vehicle is returned
        else:
            print("Vehicle not found.")
