const fs = require("fs");
const prompt = require("prompt-sync")();
const parking_lot = "parking_lot.txt";
const slot_num = "slot_num.txt";

function create_parking_lot() {
    fs.appendFileSync(parking_lot, "Slot No    " + "Registration Number    " + "Color" + "\n");
    console.log("Created parking lot with " + slot.toString() + " slots");
}

function save_slot_num() {
    fs.writeFileSync(slot_num, Number(slot)+1);
}

function check_slot() {
    totalSlot = fs.readFileSync(slot_num).toString();
    return totalSlot;
}

function park(n, regnum, color) {
    fs.appendFileSync(parking_lot, n.toString() + "          " + regnum + "              " + color + "\n");
    console.log("Allocated slot number: " + n.toString());
}

function status() {
    status = fs.readFileSync(parking_lot).toString();
    return status;
}

function check_n() {
    status = status().replace(/\n/g, " ");
    totalSlot = check_slot();
    for (var n = 1; status.split(" ").includes(n.toString()); n++) {}
    if (n >= Number(totalSlot)) {
        console.log("Sorry we are out of space.");
    } else {
        park(n, regnum, color);
    }
}

function leave(slot_num_leave) {
    fs.readFile(parking_lot, {encoding: 'utf-8'}, function(err, data) {
        if (err) throw error;
    
        var dataArray = data.split('\n');
        var lastIndex = -1;

        for (var index=0; index<dataArray.length; index++) {
            if (dataArray[index].includes(slot_num_leave)) {
                lastIndex = index;
                break; 
            }
        }
    
        dataArray.splice(lastIndex, 1);
    
        const updatedData = dataArray.join('\n');
        fs.writeFile('parking_lot.txt', updatedData, (err) => {
            if (err) throw err;
            console.log("Slot number" + " " + slot_num_leave + " " + "is free")
        });
    
    });
}

function check_regnum(color) {
    var newStatus = fs.readFileSync(parking_lot).toString();
    var dataArray = newStatus.split('\n');
    newLine = "";
    for (line of dataArray) {
        if (line.includes(color)) {
            newLine += line.substring(11, 20) + ", ";
        }   
    }
    console.log(newLine.substring(0, newLine.length-2));
}

function check_slot_num(color) {
    var newStatus = fs.readFileSync(parking_lot).toString();
    var dataArray = newStatus.split('\n');
    var newLine = "";
    for (line of dataArray) {
        if (line.includes(color)) {
            newLine += line.substring(0, 2) + ", ";
        }   
    }
    console.log(newLine.substring(0, newLine.length-2));
}

function check_regnum(regnum) {
    var newStatus = fs.readFileSync(parking_lot).toString();
    var dataArray = newStatus.split('\n');
    var newLine = "";
    for (line of dataArray) {
        if (line.includes(regnum)) {
            newLine += line.substring(0, 2) + ", ";
        }
    }
    console.log(newLine.substring(0, newLine.length-2));
}

var input = prompt("Write a command: ")
if (input.includes("status")) {
    if (fs.existsSync(parking_lot)) {
        console.log(status());
    } else {
        console.log("Can not find parking lot file. Write command 'create_parking_lot' to create a new one.");
    }
} else if (input.includes("create_parking_lot")) {
    var slot = input.split(" ")[1];
    if (fs.existsSync(parking_lot)) {
        console.log("Can not create. We already register a parking lot. Write command 'status' to see the status");
    } else {
        create_parking_lot();
        save_slot_num();
    }
} else if (input.includes("remove_parking_lot")) {
    if (fs.existsSync(parking_lot)) {
        fs.unlinkSync(parking_lot);
        fs.unlinkSync(slot_num);
    } else {
        console.log("No parking lot file in the system. Create a new one with command create_parking_lot");
    }
} else if (input.includes("park")) {
    var regnum = input.split(" ")[1];
    var color = input.split(" ")[2];
    if (fs.existsSync(parking_lot)) {
        check_n();
    } else {
        console.log("Can not find parking lot text file. Write command 'create_parking_lot' to create a new one.");
    }
} else if (input.includes("leave")) {
    var slot_num_leave = input.split(" ")[1];
    if (slot_num_leave > check_slot) {
        console.log("Error, we only have " + check_slot + " slot(s)");
    } else {
        leave(slot_num_leave);
    }
} else if (input.includes("registration_number_for_cars_with_color")) {
    var color = input.split(" ")[1];
    var status = status().replace("\n", " ");
    if (status.includes(color)) {
        check_regnum(color);
    } else {
        console.log("No cars with " + color + " color in parking lot");
    }
} else if (input.includes("slot_numbers_for_cars_with_colors")) {
    var color = input.split(" ")[1];
    var status = status().replace("\n", " ");
    if (status.includes(color)) {
        check_slot_num(color);
    } else {
        console.log("No cars with " + color + " color in parking lot");
    }
} else if (input.includes("slot_number_for_registration_number")) {
    var regnum = input.split(" ")[1];
    var status = status().replace("\n", " ");
    if (status.includes(regnum)) {
        check_regnum(regnum);
    } else {
        console.log("No cars with " + regnum + " color in parking lot");
    } 
} else {
    console.log("Wrong command. Please check again.");
}