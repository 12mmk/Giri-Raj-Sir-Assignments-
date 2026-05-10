target_floor = int(input("Enter the target floor: "))
total_weight = int(input("Enter the total weight of the passengers: "))
door_status = input("Is the door open or closed? (open/closed): ")

if target_floor >= 0 and target_floor <=10:
    if total_weight > 500:
        print("OVERWEIGHT: LIFT CANNOT MOVE")
    else:
        if door_status == "open":
            print("WARNING: CLOSE THE DOOR")
        elif door_status == "closed":
            print("ACTIVATE ELEVATOR MOTION")
        else:
            print("INVALID DOOR STATUS")
else:
    print("INVALID FLOOR NUMBER")

        