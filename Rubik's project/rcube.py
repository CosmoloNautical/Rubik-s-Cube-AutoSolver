from random import randint

# rcube (short for rotations and cube) is practically the engine for the program

# A 3d array to show the user the order that they'll be inputting the colours on the cube
example_cube = [  # [top row],[middle row], [bottom row], [final row for user clarity]
    [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["Up face"]],  # U face 0
    [["10", "11", "12"], ["13", "14", "15"], ["16", "17", "18"], ["Left face"]],  # L face 1
    [["19", "20", "21"], ["22", "23", "24"], ["25", "26", "27"], ["Back face"]],  # B face 2
    [["28", "29", "30"], ["31", "32", "33"], ["34", "35", "36"], ["Right face"]],  # R face 3
    [["37", "38", "39"], ["40", "41", "42"], ["43", "44", "45"], ["Front face"]],  # F face 4
    [["46", "47", "48"], ["49", "50", "51"], ["52", "53", "54"], ["Down face"]]  # D face 5
]

# The main cube 3d array which gets manipulated by the scrambler and solver via the moves defined bellow
cube = [  # [top row],[middle row], [bottom row], [final row for user clarity]
    [["W", "W", "W"], ["W", "W", "W"], ["W", "W", "W"]],  # , ["Up face"]], #U face 0
    [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]],  # , ["Left face"]], #L face 1
    [["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]],  # , ["Back face"]], #B face 2
    [["R", "R", "R"], ["R", "R", "R"], ["R", "R", "R"]],  # , ["Right face"]], #R face 3
    [["G", "G", "G"], ["G", "G", "G"], ["G", "G", "G"]],  # , ["Front face"]], #F face 4
    [["Y", "Y", "Y"], ["Y", "Y", "Y"], ["Y", "Y", "Y"]]  # , ["Down face"]]  #D face 5
]


# with refference to this cube https://rubikscu.be/
# cube[z][y][x]

# Below are the moves that the cube can preform
# There is never a swap involving [x][4][x] so the final row is always unaffected
# The names for the clockwise turns use standard cube notation
def U():
    # Each turn is split into 2 sections, the change on the face(1) and the change around the face(2)
    # for D and U the order is 1 --> 2
    cube[1][0], cube[2][0], cube[3][0], cube[4][0] = cube[4][0], cube[1][0], cube[2][0], cube[3][0]
    cube[0][0][2], cube[0][1][2], cube[0][2][2], cube[0][0][1], cube[0][2][1], cube[0][0][0], cube[0][1][0], cube[0][2][
        0] = cube[0][0][0], cube[0][0][1], cube[0][0][2], cube[0][1][0], cube[0][1][2], cube[0][2][0], cube[0][2][1], \
             cube[0][2][2]


# Names for anticlockwise turns use inv instead of '
def invU():
    cube[4][0], cube[1][0], cube[2][0], cube[3][0] = cube[1][0], cube[2][0], cube[3][0], cube[4][0]
    cube[0][0][0], cube[0][0][1], cube[0][0][2], cube[0][1][0], cube[0][1][2], cube[0][2][0], cube[0][2][1], cube[0][2][
        2] = cube[0][0][2], cube[0][1][2], cube[0][2][2], cube[0][0][1], cube[0][2][1], cube[0][0][0], cube[0][1][0], \
             cube[0][2][0]


def invD():
    cube[1][2], cube[2][2], cube[3][2], cube[4][2] = cube[4][2], cube[1][2], cube[2][2], cube[3][2]
    cube[5][0][0], cube[5][0][1], cube[5][0][2], cube[5][1][0], cube[5][1][2], cube[5][2][0], cube[5][2][1], cube[5][2][
        2] = cube[5][0][2], cube[5][1][2], cube[5][2][2], cube[5][0][1], cube[5][2][1], cube[5][0][0], cube[5][1][0], \
             cube[5][2][0]


def D():
    cube[4][2], cube[1][2], cube[2][2], cube[3][2] = cube[1][2], cube[2][2], cube[3][2], cube[4][2]
    cube[5][0][2], cube[5][1][2], cube[5][2][2], cube[5][0][1], cube[5][2][1], cube[5][0][0], cube[5][1][0], cube[5][2][
        0] = cube[5][0][0], cube[5][0][1], cube[5][0][2], cube[5][1][0], cube[5][1][2], cube[5][2][0], cube[5][2][1], \
             cube[5][2][2]


def L():
    # While for the other 4 rotations the order is 2 --> 1
    cube[4][0][0], cube[4][1][0], cube[4][2][0], cube[5][0][0], cube[5][1][0], cube[5][2][0], cube[2][0][2], cube[2][1][
        2], cube[2][2][2], cube[0][2][0], cube[0][1][0], cube[0][0][0] = cube[0][0][0], cube[0][1][0], cube[0][2][0], \
                                                                         cube[4][0][0], cube[4][1][0], cube[4][2][0], \
                                                                         cube[5][2][0], cube[5][1][0], cube[5][0][0], \
                                                                         cube[2][0][2], cube[2][1][2], cube[2][2][2]
    cube[1][0][2], cube[1][1][2], cube[1][2][2], cube[1][0][1], cube[1][2][1], cube[1][0][0], cube[1][1][0], cube[1][2][
        0] = cube[1][0][0], cube[1][0][1], cube[1][0][2], cube[1][1][0], cube[1][1][2], cube[1][2][0], cube[1][2][1], \
             cube[1][2][2]


def invL():
    cube[0][0][0], cube[0][1][0], cube[0][2][0], cube[4][0][0], cube[4][1][0], cube[4][2][0], cube[5][2][0], cube[5][1][
        0], cube[5][0][0], cube[2][2][2], cube[2][1][2], cube[2][0][2] = cube[4][0][0], cube[4][1][0], cube[4][2][0], \
                                                                         cube[5][0][0], cube[5][1][0], cube[5][2][0], \
                                                                         cube[2][0][2], cube[2][1][2], cube[2][2][2], \
                                                                         cube[0][0][0], cube[0][1][0], cube[0][2][0]
    cube[1][0][0], cube[1][0][1], cube[1][0][2], cube[1][1][0], cube[1][1][2], cube[1][2][0], cube[1][2][1], cube[1][2][
        2] = cube[1][0][2], cube[1][1][2], cube[1][2][2], cube[1][0][1], cube[1][2][1], cube[1][0][0], cube[1][1][0], \
             cube[1][2][0]


def B():
    cube[0][0][0], cube[0][0][1], cube[0][0][2], cube[1][2][0], cube[1][1][0], cube[1][0][0], cube[5][2][0], cube[5][2][
        1], cube[5][2][2], cube[3][2][2], cube[3][1][2], cube[3][0][2] = cube[3][0][2], cube[3][1][2], cube[3][2][2], \
                                                                         cube[0][0][0], cube[0][0][1], cube[0][0][2], \
                                                                         cube[1][0][0], cube[1][1][0], cube[1][2][0], \
                                                                         cube[5][2][0], cube[5][2][1], cube[5][2][2]
    cube[2][0][2], cube[2][1][2], cube[2][2][2], cube[2][0][1], cube[2][2][1], cube[2][0][0], cube[2][1][0], cube[2][2][
        0] = cube[2][0][0], cube[2][0][1], cube[2][0][2], cube[2][1][0], cube[2][1][2], cube[2][2][0], cube[2][2][1], \
             cube[2][2][2]


def invB():
    cube[3][0][2], cube[3][1][2], cube[3][2][2], cube[0][0][2], cube[0][0][1], cube[0][0][0], cube[1][0][0], cube[1][1][
        0], cube[1][2][0], cube[5][2][2], cube[5][2][1], cube[5][2][0] = cube[0][0][0], cube[0][0][1], cube[0][0][2], \
                                                                         cube[1][0][0], cube[1][1][0], cube[1][2][0], \
                                                                         cube[5][2][0], cube[5][2][1], cube[5][2][2], \
                                                                         cube[3][0][2], cube[3][1][2], cube[3][2][2]
    cube[2][0][0], cube[2][0][1], cube[2][0][2], cube[2][1][0], cube[2][1][2], cube[2][2][0], cube[2][2][1], cube[2][2][
        2] = cube[2][0][2], cube[2][1][2], cube[2][2][2], cube[2][0][1], cube[2][2][1], cube[2][0][0], cube[2][1][0], \
             cube[2][2][0]


def R():
    cube[0][0][2], cube[0][1][2], cube[0][2][2], cube[2][2][0], cube[2][1][0], cube[2][0][0], cube[5][2][2], cube[5][1][
        2], cube[5][0][2], cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[4][0][2], cube[4][1][2], cube[4][2][2], \
                                                                         cube[0][0][2], cube[0][1][2], cube[0][2][2], \
                                                                         cube[2][0][0], cube[2][1][0], cube[2][2][0], \
                                                                         cube[5][0][2], cube[5][1][2], cube[5][2][2]
    cube[3][0][2], cube[3][1][2], cube[3][2][2], cube[3][0][1], cube[3][2][1], cube[3][0][0], cube[3][1][0], cube[3][2][
        0] = cube[3][0][0], cube[3][0][1], cube[3][0][2], cube[3][1][0], cube[3][1][2], cube[3][2][0], cube[3][2][1], \
             cube[3][2][2]


def invR():
    cube[4][0][2], cube[4][1][2], cube[4][2][2], cube[0][2][2], cube[0][1][2], cube[0][0][2], cube[2][2][0], cube[2][1][
        0], cube[2][0][0], cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[0][0][2], cube[0][1][2], cube[0][2][2], \
                                                                         cube[2][0][0], cube[2][1][0], cube[2][2][0], \
                                                                         cube[5][0][2], cube[5][1][2], cube[5][2][2], \
                                                                         cube[4][0][2], cube[4][1][2], cube[4][2][2]
    cube[3][0][0], cube[3][0][1], cube[3][0][2], cube[3][1][0], cube[3][1][2], cube[3][2][0], cube[3][2][1], cube[3][2][
        2] = cube[3][0][2], cube[3][1][2], cube[3][2][2], cube[3][0][1], cube[3][2][1], cube[3][0][0], cube[3][1][0], \
             cube[3][2][0]


def F():
    cube[3][0][0], cube[3][1][0], cube[3][2][0], cube[0][2][2], cube[0][2][1], cube[0][2][0], cube[1][0][2], cube[1][1][
        2], cube[1][2][2], cube[5][0][2], cube[5][0][1], cube[5][0][0] = cube[0][2][0], cube[0][2][1], cube[0][2][2], \
                                                                         cube[1][0][2], cube[1][1][2], cube[1][2][2], \
                                                                         cube[5][0][0], cube[5][0][1], cube[5][0][2], \
                                                                         cube[3][0][0], cube[3][1][0], cube[3][2][0]
    cube[4][0][2], cube[4][1][2], cube[4][2][2], cube[4][0][1], cube[4][2][1], cube[4][0][0], cube[4][1][0], cube[4][2][
        0] = cube[4][0][0], cube[4][0][1], cube[4][0][2], cube[4][1][0], cube[4][1][2], cube[4][2][0], cube[4][2][1], \
             cube[4][2][2]


def invF():
    cube[0][2][0], cube[0][2][1], cube[0][2][2], cube[1][2][2], cube[1][1][2], cube[1][0][2], cube[5][0][0], cube[5][0][
        1], cube[5][0][2], cube[3][2][0], cube[3][1][0], cube[3][0][0] = cube[3][0][0], cube[3][1][0], cube[3][2][0], \
                                                                         cube[0][2][0], cube[0][2][1], cube[0][2][2], \
                                                                         cube[1][0][2], cube[1][1][2], cube[1][2][2], \
                                                                         cube[5][0][0], cube[5][0][1], cube[5][0][2]
    cube[4][0][0], cube[4][0][1], cube[4][0][2], cube[4][1][0], cube[4][1][2], cube[4][2][0], cube[4][2][1], cube[4][2][
        2] = cube[4][0][2], cube[4][1][2], cube[4][2][2], cube[4][0][1], cube[4][2][1], cube[4][0][0], cube[4][1][0], \
             cube[4][2][0]


# I attempted to use a dictionary for the scrambler and cube_input_alg but the functions wouldn't run through the dictionary
"""parse_dict = {"U":U(),"U'":invU(),"D":D(),"D'":invD(),"L":L(),"L'":invL(),"B":B(),"B'":invB(),"R":R(),"R'":invR(),"F":F(),"F'":invF()}"""


# Scrambler for creating random cube states
# Simply performs 35 random moves
# By using random moves it ensures that it can never create an impossible cube
def scrambler():
    # A dictionary used to convert random numbers into moves
    # This would allow the scrapped parse_dict to be implemented esily if it were to be fixed
    alg_dict = {1: "U", 2: "U'", 3: "D", 4: "D'", 5: "L", 6: "L'", 7: "B", 8: "B'", 9: "R", 10: "R'", 11: "F", 12: "F'"}
    print("Scrambling...")
    # Scramalg to store the moves made
    scramalg = ""
    # for loop to ensure the program makes a 35 move scramble
    for scrambleNO in range(0, 35):
        # random number generator outputs into the dictionary which outputs a move
        choice = alg_dict[randint(1, 12)]
        if choice == "U":
            U()
        elif choice == "U'":
            invU()
        elif choice == "D":
            D()
        elif choice == "D'":
            invD()
        elif choice == "L":
            L()
        elif choice == "L'":
            invL()
        elif choice == "B":
            B()
        elif choice == "B'":
            invB()
        elif choice == "R":
            R()
        elif choice == "R'":
            invR()
        elif choice == "F":
            F()
        elif choice == "F'":
            invF()
        scramalg += f"{choice} "
    print(scramalg)


def cube_input_alg():
    # input alg serves the same function as scram alf
    input_alg = ""
    # .split() creates an array from the users input which the for loop goes through one by one.
    for x in input(
            "Enter the algorithm for the scramble\nDo not use half turns, double turns, slice turns or cube reorientations\nSeperate each move with a space\n>").upper().strip().split():
        # checking if there's a valid input
        if x in ["U", "U'", "D", "D'", "L", "L'", "B", "B'", "R", "R'", "F", "F'"]:
            if x == "U":
                U()
            elif x == "U'":
                invU()
            elif x == "D":
                D()
            elif x == "D'":
                invD()
            elif x == "L":
                L()
            elif x == "L'":
                invL()
            elif x == "B":
                B()
            elif x == "B'":
                invB()
            elif x == "R":
                R()
            elif x == "R'":
                invR()
            elif x == "F":
                F()
            elif x == "F'":
                invF()
            input_alg += f"{x} "
        else:
            # tells the user if an invalid input was ignored
            print(f"Input {x} was ignored")
    print(f"Cube scrambled with {input_alg}")


# Function to allow users to input a cube
def cube_input_array():
    # Dictionary to allow the program to give users dynamic instructions
    row_face_dict = {0: "Top", 1: "Middle", 2: "Bottom", 3: "Up", 4: "Left", 5: "Back", 6: "Right", 7: "Front",
                     8: "Down"}
    print("INSTRUCTIONS")
    print("Please enter the colours on your cube in this order:")
    for z in range(0, 6):
        print(example_cube[z])
    print(
        "The Front Face is the face of the cube that is pointed at you.\nThe Up Face is the face that is pointing upwards.\nThe other faces should be self explanitory.")
    print(
        "You will enter the colours row by row, left to right (3 colours at a time)\nWhere each colour is seperated by a space")
    # An input to make inputting into a 3d array slightly easier for the user
    # Adapted from a 2d array input
    # .upper, .strip and [:3] to reduce user error
    for y in range(0, 6):
        for x in range(0, 3):
            cube[y][x] = list(map(str, input(
                f"enter The colours for the {row_face_dict[x]} Row on the {row_face_dict[y + 3]} Face:\n>").upper().strip().split()))[
                         :3]
        try:
            cube[y][3] = f"{row_face_dict[y + 3]} Face"
        except:
            cube[y].append(f"{row_face_dict[y + 3]} Face")


# A simple function that presents the cube in a more user friendly way
# compared to printing a raw 3d array
def display_cube():
    for z in range(0, 6):
        print(cube[z])
