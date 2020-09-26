import os

def check_n():
    slot_num = check_slots()
    parking_lot = status()
    n = 1
    for _ in parking_lot:
        if str(n) in parking_lot.split():
            n += 1
    if n > int(slot_num):
        print("Sorry we are out of space.")
    else:
        park(n, regnum, color)

def create(slot):
    print("Created parking lot with: " + str(slot) + " slots")
    with open("parking_lot.txt", "a") as file:
        file.write("Slot No    " + "Registration Number    " + "Color" + "\n")

def save_slot_num(slot):
    with open("slot_num.txt", "w") as file:
        file.write(str(slot))

def check_slots():
    with open("slot_num.txt", "r") as file:
        slot_num = file.read()
        return slot_num

def park(n, regnum, color):
    print("Allocated slot number: " + str(n))
    with open("parking_lot.txt", "a") as file:
        file.write(str(n) + "          " + regnum + "              " + color + "\n")

def status():
    with open("parking_lot.txt", "r") as file:
        parking_lot = file.read()
        return parking_lot

def leave(slot_num_leave):
    print("Slot number " + slot_num_leave + " is free")
    with open("parking_lot.txt", "r") as file:
        lines = file.readlines() 
    with open("parking_lot.txt", "w") as file:
        for line in lines:
            if not line.startswith(slot_num_leave):
                file.write(line)

def check_regnum(color):
    with open("parking_lot.txt", "r") as file:
        lines = file.readlines()
    matching_lines = [line for line in lines if color in line]
    n = 0
    slot_num = len(matching_lines) - 1
    for _ in matching_lines:
        regnum = matching_lines[n][11:20]
        print(regnum)
        if n < slot_num:
            n += 1

def check_slot_num(color):
    with open("parking_lot.txt", "r") as file:
        lines = file.readlines()
    matching_lines = [line for line in lines if color in line]
    n = 0
    slot_num = len(matching_lines) - 1
    for _ in matching_lines:
        slot = matching_lines[n][0:2]
        print(slot)
        if n < slot_num:
            n += 1

def result():
    print("Result:")

def welcome_msg():
    print("---------------------------------------------------------------------------------")
    print("1. 'status' to check if we had any parking lot.")
    print("2. 'create_parking_lot' and total number of slot to initiate our parking slot.")
    print("    Example: create_parking_lot 4 to create parking lot with four slots.")
    print("3. 'park' followed by car registration number and its color.")
    print("    Registration number must only contain 9 characters including dash ('-') symbol.")
    print("    Example: park B-1994-FA Black")
    print("4. 'leave' and followed by slot number of the car that want to leave the parking lot.")
    print("    Example: leave 3 to make slot number 3 available.")
    print("5. 'regno_for_cars_with_color' followed by color of your choice")
    print("    to check cars registration number associated with certain color in parking lot.")
    print("    Example: regno_for_cars_with_color white")
    print("6. 'slot_numbers_for_cars_with_color' followed by color of your choice")
    print("    to check slot numbers associated with certain car color in parking lot.")
    print("    Example: slot_numbers_for_cars_with_color white")
    print("7. 'delete_parking_lot' to delete current parking lot file")
    print("8. 'exit' to exit the application.")


while True:
    welcome_msg()
    prompt = input("Write a command: ")
    print("---------------------------------------------------------------------------------")
    if prompt == "status":
        if os.path.isfile("parking_lot.txt"):
            parking_lot = status()
            result()
            print(parking_lot)
        else:
            result()
            print("Can not find parking lot file. Write command 'create' (without quote) to create a new one.")
    elif "park" in prompt.split():
        try:
            splitted = prompt.split()
            regnum = splitted[1]
            color = splitted[2]
            if os.path.isfile("parking_lot.txt"):
                result()
                check_n()
            else:
                result()
                print("Can not find parking lot file. Write command 'create_parking_lot' to create a new one.")
        except Exception as e:
            print(e)
    elif "create_parking_lot" in prompt:
        splitted = prompt.split()
        slot = splitted[1]
        if os.path.isfile("parking_lot.txt"):
            result()
            print("Can not create. We already register a parking lot. Write command 'status' (to see the status")
        else:
            result()
            save_slot_num(slot)
            create(slot)
    elif "leave" in prompt:
        splitted = prompt.split()
        slot_num_leave = splitted[1]
        slot_num = check_slots()
        parking_lot = status()
        if int(slot_num_leave) > int(slot_num):
            result()
            print("Error, we only have " + slot_num + " slot(s)")
        elif slot_num_leave not in parking_lot.split():
            result()
            print("We don't have car on slot " + slot_num_leave)
        else:
            result()
            leave(slot_num_leave)
    elif "regno_for_cars_with_color" in prompt:
        splitted = prompt.split()
        color = splitted[1]
        parking_lot = status()
        if color.lower() in parking_lot.lower():
            result()
            check_slot_num(color)
        else:
            result()
            print("No cars with " + color + " color in parking lot")
    elif "slot_numbers_for_cars_with_color" in prompt:
        splitted = prompt.split()
        color = splitted[1]
        parking_lot = status()
        if color.lower() in parking_lot.lower():
            result()
            check_regnum(color)
        else:
            result()
            print("No cars with " + color + " color in parking lot")
    elif "delete_parking_lot" in prompt:
        if os.path.isfile("parking_lot.txt"):
            result()
            print("Successfully deleted current parking lot file.")
            os.remove("parking_lot.txt")
            os.remove("slot_num.txt")
        else:
            result()
            print("No parking lot file in the system. Create a new one with command create_parking_lot")
    elif prompt == "exit":
        print("Exiting...")
        break
    else:
        print("Your command isn't registered on system. Please try again with another command.")