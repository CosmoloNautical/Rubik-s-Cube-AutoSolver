import os
import Autosolver as auto


# A function to clear the screen to make the program easier to view on back to back use
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        os.system('clear')
    else:
        # for windows platfrom
        os.system('cls')


while True:
    # rcube re-imported to reset the state of the cube
    import rcube

    # Simple select menu, easily expandable
    x = input("""Would you like the program to:
  A: Solve a random cube
  B: Solve a custom cube
  C: Input a custom scramble algorithm
  D: Exit
  > """)
    # x.upper() and .strip() to prevent user error
    x = x.upper().strip()
    # Checking if the user's input is in the bounds of the option selection
    if x in ["A", "B", "C", "D"]:
        if x == "A":
            rcube.scrambler()
        elif x == "B":
            # A while loop to allow the user to retry inputting the cube
            while True:
                # Screen clear for clarity
                screen_clear()
                rcube.cube_input_array()
                # show the cube to the user so they can double check it is correct
                rcube.display_cube()
                # prompt the user on whether or not the iputted cube is correct
                if input("Is This correct? Y/N\n>").upper().strip() == "Y":
                    break
        elif x == "C":
            rcube.cube_input_alg()
        elif x == "D":
            exit()
        input("Press enter to start solving")
        # pass false for later checks on whether or not the cube is impossible
        auto.CFOP(False)
        # Input to allow the user to view the cube and info before the screen is cleared
        input("Press enter to return to main menu")
    # Screen clear for clarity
    screen_clear()
