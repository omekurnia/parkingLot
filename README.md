# parkingLot
This is parking lot program simulation to keep track of cars and its details from the parking lot.

Make sure you already have node installed on your computer. You also need to install prompt-sync package so you can input name and phone number to be search on the blocked.txt.

To Use :

1. git clone this repository
2. cd into project directory
3. Install prompt-sync package with npm install prompt-sync
4. Run blacklists.js on your terminal with command node parking_lot.js

When you run the program, it will give you prompt message to write a command,
There are 8 commands you can try in the program, each of them has one functionality.
- status : the program will return the content of parking_lot.txt. If you haven't created any parking lot yet, then the program will suggest you how to create it.
- create_parking_lot : will create a parking_lot.txt file on the directory. You can't create another parking lot file if you already have one.
- remove_parking_lot : to delete existing parking lot file. you can not delete if you don't have any and the program will suggest you to create a new one.
- park (registration number) (car color) : will add the car and its slot into parking_lot.txt file. Make sure you write it right. as of now the registration number is only for indonesian. one example of correct command is => park B-1990-HA white
- leave (slot number) : to remove car from certain slot you given on the input. example => leave 4, will remove car on slot 4.
- registration_number_for_cars_with_color (color) : will return to you registration number from cars with certain color. example => registration_number_for_cars_with_color white.
- slot_numbers_for_cars_with_colors (color) : will return to you slot numbers from cars with certain color. example => slot_number_for_cars_with_color white.
- slot_number_for_registration_number (registration number) : will return to you slot number from cars with certain registration number. example => slot_number_for_registration_number B-1990-HA.

Enjoy!

Any suggestion for improvment is really appreciated, thank you for reading.
