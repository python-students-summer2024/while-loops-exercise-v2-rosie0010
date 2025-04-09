def get_starting_number():
    while True:
        num_bottles = input("Enter the number of beer bottles to start with: ")
        if num_bottles.isnumeric() and int(num_bottles) >= 1:
            return int(num_bottles)
            
        else:
            print("Please input a valid number of bottles to start with")
        

def sing(num_bottles):
    for i in range(num_bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")

            if i -1 == 1:
                print("Take one down, pass it around, 1 bottle of beer on the wall.")
                print()

            else:
                print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
                print()

        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")