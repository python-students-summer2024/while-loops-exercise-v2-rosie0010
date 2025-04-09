def get_starting_number():
    while True:
        num_bottles = input("Enter the number of beer bottles to start with: ")
        if num_bottles.isnumeric() and int(num_bottles) >= 1:
            return int(num_bottles)
            
        else:
            print("Please input a valid number of bottles to start with")


def sing(starting_bottles):
    i = starting_bottles
    continue_singing = True
    while continue_singing:
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            if i - 1 == 1:
                print(f"Take one down, pass it around, {i - 1} bottle of beer on the wall.")
                print()
            else:
                print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall.")
                print()
        else:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            print()
            continue_singing = False
        i -= 1