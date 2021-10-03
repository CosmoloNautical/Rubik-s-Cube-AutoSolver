import rcube
import time


# I will be reffering to pieces of the cube as if it were a standard cube (refference the cube in rcube.py)

# the first step for solving the cube has a lot of different possibilities so for clarity they have been split into several functions
# The first is for if a piece of the white cross is on the yellow Face
def U_cross_Dface():
    # local moves and local alg to count and record the moves made
    local_moves = 0
    local_alg = ""
    # checks if a white piece is on the green side of the yellow face and the white pieces edge corresponds with the side its on
    if rcube.cube[5][0][1] == rcube.cube[0][1][1] and rcube.cube[4][1][1] == rcube.cube[4][2][1]:
        rcube.F()
        rcube.F()
        local_moves += 2
        local_alg += "F F "
    # checks if a white piece is on the orange side of the yellow face and the white pieces edge corresponds with the side its on
    elif rcube.cube[5][1][0] == rcube.cube[0][1][1] and rcube.cube[1][1][1] == rcube.cube[1][2][1]:
        rcube.L()
        rcube.L()
        local_alg += "L L "
        local_moves += 2
        # checks if a white piece is on the red side of the yellow face and the white pieces edge corresponds with the side its on
    elif rcube.cube[5][1][2] == rcube.cube[0][1][1] and rcube.cube[3][1][1] == rcube.cube[3][2][1]:
        rcube.R()
        rcube.R()
        local_alg += "R R "
        local_moves += 2
        # checks if a white piece is on the blue side of the yellow face and the white pieces edge corresponds with the side its on
    elif rcube.cube[5][2][1] == rcube.cube[0][1][1] and rcube.cube[2][1][1] == rcube.cube[2][2][1]:
        rcube.B()
        rcube.B()
        local_alg += "B B "
        local_moves += 2
    # If none of the other possibilities apply then the white piece isn't on the right side so the program performs a D turn to allign the piece
    else:
        rcube.D()
        local_alg += "D "
        local_moves += 1
    return local_moves, local_alg


# The second is for if white piece is on the bottom layer of the cube
def U_cross_bottom_layer():
    # local moves and local alg to count and record the moves made
    local_moves = 0
    local_alg = ""
    # Checks if a white piece is on the bottom layer of the red side and the edge is red
    if rcube.cube[3][2][1] == rcube.cube[0][1][1] and rcube.cube[5][1][2] == rcube.cube[3][1][1]:
        rcube.invD()
        rcube.invF()
        rcube.R()
        rcube.F()
        local_alg += "D' F' R F "
        local_moves += 4
    # Checks if a white piece is on the bottom layer of the green side and the edge is green
    elif rcube.cube[4][2][1] == rcube.cube[0][1][1] and rcube.cube[5][0][1] == rcube.cube[4][1][1]:
        rcube.invD()
        rcube.invL()
        rcube.F()
        rcube.L()
        local_alg += "D' L' F L "
        local_moves += 4
    ##Checks if a white piece is on the bottom layer of the blue side and the edge is blue
    elif rcube.cube[2][2][1] == rcube.cube[0][1][1] and rcube.cube[5][2][1] == rcube.cube[2][1][1]:
        rcube.invD()
        rcube.invR()
        rcube.B()
        rcube.R()
        local_alg += "D' R' B R "
        local_moves += 4
    # Checks if a white piece is on the bottom layer of the orange side and the edge is orange
    elif rcube.cube[1][2][1] == rcube.cube[0][1][1] and rcube.cube[5][1][0] == rcube.cube[1][1][1]:
        rcube.invD()
        rcube.invB()
        rcube.L()
        rcube.B()
        local_alg += "D' B' L B "
        local_moves += 4
    # If the previous cases are not applicable then the white piece is not correctly alligned so a D turn is performed to allign it
    else:
        rcube.D()
        local_alg += "D "
        local_moves += 1
    return local_moves, local_alg


# The third and fourth are for if a white piece in on the middle layer of the cube
# Unlike the previous functions, they do not check is the piece is correctly alligned, only if the piece is white
# This is because it doesn't attempt to solve the piece, it only attempts to move the piece to a place where it can be solved more easily
# The third is for if it's on the right side of the middle layer
def U_cross_middle_layer_right():
    # local moves and local alg to count and record the moves made
    local_moves = 0
    local_alg = ""
    # moves a white piece on the right side of the green middle layer
    if rcube.cube[4][1][2] == rcube.cube[0][1][1]:
        rcube.invR()
        rcube.D()
        rcube.R()
        local_alg += "R' D R "
        local_moves += 3
    # moves a white piece on the right side of the red middle layer
    elif rcube.cube[3][1][2] == rcube.cube[0][1][1]:
        rcube.invB()
        rcube.D()
        rcube.B()
        local_alg += "B' D B "
        local_moves += 3
    # moves a white piece on the right side of the blue middle layer
    elif rcube.cube[2][1][2] == rcube.cube[0][1][1]:
        rcube.invL()
        rcube.D()
        rcube.L()
        local_alg += "L' D L "
        local_moves += 3
    # moves a white piece on the right side of the orange middle layer
    elif rcube.cube[1][1][2] == rcube.cube[0][1][1]:
        rcube.invF()
        rcube.D()
        rcube.F()
        local_alg += "F' D F "
        local_moves += 3
    return local_moves, local_alg


# The third is for if it's on the left side of the midlle layer
def U_cross_middle_layer_left():
    # local moves and local alg to count and record the moves made
    local_moves = 0
    local_alg = ""
    # moves a white piece on the left side of the green middle layer
    if rcube.cube[4][1][0] == rcube.cube[0][1][1]:
        rcube.L()
        rcube.D()
        rcube.invL()
        local_alg += "L D L' "
        local_moves += 3
    # moves a white piece on the left side of the red middle layer
    elif rcube.cube[3][1][0] == rcube.cube[0][1][1]:
        rcube.F()
        rcube.D()
        rcube.invF()
        local_alg += "F D F'"
        local_moves += 3
    # moves a white piece on the left side of the blue middle layer
    elif rcube.cube[2][1][0] == rcube.cube[0][1][1]:
        rcube.R()
        rcube.D()
        rcube.invR()
        local_alg += "R D R' "
        local_moves += 3
    # moves a white piece on the left side of the orange middle layer
    elif rcube.cube[1][1][0] == rcube.cube[0][1][1]:
        rcube.B()
        rcube.D()
        rcube.invB()
        local_alg += "B D B' "
        local_moves += 3
    return local_moves, local_alg


# The fifth is for if the white piece is on the top layer
# Allignment doesn't matter here either as once again it only attempts to move the piece to a place where it can be solved more easily
def U_cross_top_layer():
    # local moves and local alg to count and record the moves made
    local_alg = ""
    local_moves = 0
    # If the white piece in the the top green layer
    if rcube.cube[4][0][1] == rcube.cube[0][1][1]:
        rcube.F()
        rcube.F()
        local_alg += "F F "
        local_moves += 2
    # If the white piece in the the top red layer
    if rcube.cube[3][0][1] == rcube.cube[0][1][1]:
        rcube.R()
        rcube.R()
        local_alg += "R R "
        local_moves += 2
        # If the white piece in the the top blue layer
    if rcube.cube[2][0][1] == rcube.cube[0][1][1]:
        rcube.B()
        rcube.B()
        local_alg += "B B "
        local_moves += 2
    # If the white piece in the the top orange layer
    if rcube.cube[1][0][1] == rcube.cube[0][1][1]:
        rcube.L()
        rcube.L()
        local_alg += "L L "
        local_moves += 2
    return local_moves, local_alg


# The first step of most rubik's cube solving methods
# fairly straight forward
# it attempts to create a white cross on the white face of the cube
# start and impossible are imported here to check if the cube is impossible or not
def U_cross(start, impossible):
    # local moves and local alg to count and record the moves made
    local_alg = ""
    local_moves = 0
    print("\n********************U Cross********************\n")

    # An overarching while loop which checks if the white pieces are in the cross at the top
    # once satisfied, this step will be over
    # It also checks if the cube has been flagged as impossible
    while (rcube.cube[0][0][1] != rcube.cube[0][1][1] or rcube.cube[0][1][0] != rcube.cube[0][1][1] or rcube.cube[0][1][
        2] != rcube.cube[0][1][1] or rcube.cube[0][2][1] != rcube.cube[0][1][1]) and impossible != True:

        # An if statement used to check if the cube has been running for longer than a second
        # The program takes roughly 0.002 or 0.003 on average to solve
        # One second is long enough to ensure the cube is impossible as well as not be annoying for the user
        if (time.time() - start) > 1:
            print("This cube is likely impossible")
            impossible = True
            break

        # A while loop for if the white piece is on the yellow face
        while rcube.cube[5][0][1] == rcube.cube[0][1][1] or rcube.cube[5][1][0] == rcube.cube[0][1][1] or \
                rcube.cube[5][1][2] == rcube.cube[0][1][1] or rcube.cube[5][2][1] == rcube.cube[0][1][1]:
            # Checking if the cube has passed the threshold for being flagged as impossible
            if (time.time() - start) > 1:
                print("This cube is likely impossible")
                impossible = True
                break
            # obtaining the passed values for local_alg and local_moves
            a, b = U_cross_Dface()
            local_moves += a
            local_alg += b

        # A while loop for if the white piece is on the bottom layer
        while rcube.cube[4][2][1] == rcube.cube[0][1][1] or rcube.cube[3][2][1] == rcube.cube[0][1][1] or \
                rcube.cube[2][2][1] == rcube.cube[0][1][1] or rcube.cube[1][2][1] == rcube.cube[0][1][1]:
            # Checking if the cube has passed the threshold for being flagged as impossible
            if (time.time() - start) > 1:
                print("This cube is likely impossible")
                impossible = True
                break
            # obtaining the passed values for local_alg and local_moves
            a, b = U_cross_bottom_layer()
            local_moves += a
            local_alg += b

        # A while loop for if the white piece is on the right side of the midlle layer
        while rcube.cube[4][1][2] == rcube.cube[0][1][1] or rcube.cube[3][1][2] == rcube.cube[0][1][1] or \
                rcube.cube[2][1][2] == rcube.cube[0][1][1] or rcube.cube[1][1][2] == rcube.cube[0][1][1]:
            # Checking if the cube has passed the threshold for being flagged as impossible
            if (time.time() - start) > 1:
                print("This cube is likely impossible")
                impossible = True
                break
            # obtaining the passed values for local_alg and local_moves
            a, b = U_cross_middle_layer_right()
            local_moves += a
            local_alg += b

        # A while loop for if the white piece is on the left side of the middle layer
        while rcube.cube[4][1][0] == rcube.cube[0][1][1] or rcube.cube[3][1][0] == rcube.cube[0][1][1] or \
                rcube.cube[2][1][0] == rcube.cube[0][1][1] or rcube.cube[1][1][0] == rcube.cube[0][1][1]:
            # Checking if the cube has passed the threshold for being flagged as impossible
            if (time.time() - start) > 1:
                print("This cube is likely impossible")
                impossible = True
                break
            # obtaining the passed values for local_alg ad local_moves
            a, b = U_cross_middle_layer_left()
            local_moves += a
            local_alg += b

        # A while loop for if the white piece is on the top layer
        while rcube.cube[4][0][1] == rcube.cube[0][1][1] or rcube.cube[3][0][1] == rcube.cube[0][1][1] or \
                rcube.cube[2][0][1] == rcube.cube[0][1][1] or rcube.cube[1][0][1] == rcube.cube[0][1][1]:
            # Checking if the cube has passed the threshold for being flagged as impossible
            if (time.time() - start) > 1:
                print("This cube is likely impossible")
                impossible = True
                break
            # obtaining the passed values for local_alg ad local_moves
            a, b = U_cross_top_layer()
            local_moves += a
            local_alg += b
    # The program prints the algorithm and number of moves used at the end of each stage
    # as well as returning them for the final results
    print(f"Moves taken: {local_moves}")
    print(local_alg)
    rcube.display_cube()
    return local_moves, local_alg, impossible


# A discarded attemp at F2l
# This method would have ended up being far more complex than what was anticipated
# So it was discarded for a more simple, though also more inneficient, method
"""
def cFop():
  #Easy cases
  if (rcube.cube[5][2][2]) == "B" and (rcube.cube[3][2][2] and rcube.cube[5][1][0]) == "R" and (rcube.cube[2][2][0]) == "W":
    rcube.invB()
    rcube.invD()
    rcube.B()
  elif (rcube.cube[5][0][1] and rcube.cube[2][2][0]) == "B" and (rcube.cube[5][2][2]) == "R" and (rcube.cube[3][2][2]) == "W":
    rcube.R()
    rcube.D()
    rcube.invR()
  elif (rcube.cube[2][2][1] and rcube.cube[2][2][0]) == "B" and (rcube.cube[5][2][1] and rcube.cube[5][2][2]) == "R" and (rcube.cube[3][2][2]) == "W":
    rcube.invD()
    rcube.invB()
    rcube.D()
    rcube.B()
  elif (rcube.cube[5][2][2] and rcube.cube[5][1][2]) == "B" and (rcube.cube[3][2][1] and rcube.cube[3][2][2]) == "R" and (rcube.cube[2][2][0]) == "W":
    rcube.D()
    rcube.R()
    rcube.invD()
    rcube.invR()
  #Corner in bottom, edge in top layer
  elif (rcube.cube[2][2][1] and rcube.cube[2][0][0]) == "B" and (rcube.cube[5][2][2] and rcube.cube[3][0][2]) == "R":
    rcube.D()
    rcube.R()
    rcube.invD()
    rcube.invR()
    rcube.invD()
    rcube.invB()
    rcube.D()
    rcube.B()
  elif (rcube.cube[5][1][2] and rcube.cube[2][0][0]) == "B" and (rcube.cube[3][2][1] and rcube.cube[3][0][2]) == "R":
    rcube.invD()
    rcube.invB()
    rcube.D()
    rcube.B()
    rcube.D()
    rcube.R()
    rcube.invD()
    rcube.invR()
  elif (rcube.cube[2][2][1]) == "B" and (rcube.cube[5][2][1] and rcube.cube[2][0][0]) == "R" and (rcube.cube[3][0][2]) == "W":
    rcube.invB()
    rcube.D()
    rcube.B()
    rcube.invD()
    rcube.invB()
    rcube.D()
    rcube.B()
  elif (rcube.cube[5][1][2]) == "B" and (rcube.cube[3][2][1] and rcube.cube[2][0][0]) == "R" and (rcube.cube[3][0][2]) == "W":
    rcube.R()
    rcube.D()
    rcube.invR()
    rcube.invD()
    rcube.R()
    rcube.D()
    rcube.invR()
  elif (rcube.cube[5][1][2] and rcube.cube[3][0][2]) == "B" and (rcube.cube[3][2][1]) == "R" and (rcube.cube[2][0][0]) == "W":
    rcube.R()
    rcube.invD()
    rcube.invR()
    rcube.D()
    rcube.R()
    rcube.invD()
    rcube.invR()
  elif (rcube.cube[2][2][1] and rcube.cube[3][0][2]) == "B" and (rcube.cube[5][2][1]) == "R" and (rcube.cube[2][0][0]) == "W":
    rcube.invB()
    rcube.invD()
    rcube.B()
    rcube.D()
    rcube.invB()
    rcube.invD()
    rcube.B()
  #Corner in top, edge in middle
  elif (rcube.cube[2][1][0] and rcube.cube[3][2][2]) == "B" and (rcube.cube[2][2][0] and rcube.cube[3][1][2]) == "R" and (rcube.cube[5][2][2]) == "W":
    rcube.R()
    rcube.D()
    rcube.invR()
    rcube.invD()
    rcube.R()
    rcube.D()
    rcube.invR()
    rcube.invD()
    rcube.R()
    rcube.D()
    rcube.invR()
  elif (rcube.cube[2][1][0] and rcube.cube[2][2][0]) == "B" and (rcube.cube[5][2][2] and rcube.cube[3][1][2]) == "R" and (rcube.cube[3][2][2]) == "W":
    rcube.D()
    rcube.invB()
    rcube.D()
    rcube.B()
    rcube.D()
    rcube.invB()
    rcube.D()
    rcube.D()
    rcube.B()
  elif (rcube.cube[2][1][0] and rcube.cube[5][2][2]) == "B" and (rcube.cube[3][2][2] and rcube.cube[3][1][2]) == "R" and (rcube.cube[2][2][0]) == "W":
    rcube.invD()
    rcube.R()
    rcube.invD()
    rcube.invR()
    rcube.invD()
    rcube.R()
    rcube.D()
    rcube.D()
    rcube.invR()
  elif (rcube.cube[3][1][2] and rcube.cube[3][2][2]) == "B" and (rcube.cube[2][2][0] and rcube.cube[2][1][0]) == "R" and (rcube.cube[5][2][2]) == "W":
    rcube.R()
    rcube.invD()
    rcube.invR()
    rcube.invD()
    rcube.invR()
    rcube.D()
    rcube.R()
  elif (rcube.cube[3][1][2] and rcube.cube[2][2][0]) == "B" and (rcube.cube[5][2][2] and rcube.cube[2][1][0]) == "R" and (rcube.cube[3][2][2]) == "W":
    rcube.D()
    rcube.invB()
    rcube.invD()
    rcube.B()
    rcube.D()
    rcube.B()
    rcube.D()
    rcube.invB()
  elif (rcube.cube[3][1][2] and rcube.cube[5][2][2]) == "B" and (rcube.cube[3][2][2] and rcube.cube[2][1][0]) == "R" and (rcube.cube[2][2][0]) == "W":
    rcube.invD()
    rcube.R()
    rcube.D()
    rcube.invR()
    rcube.invD()
    rcube.invR()
    rcube.invD()
    rcube.R()
  #Corner pointing outwards, edge in top layer
  elif (rcube.cube[3][2][1] and rcube.cube[2][2][0]) == "B" and (rcube.cube[5][2][2] and rcube.cube[5][1][2]) == "R" and (rcube.cube[3][2][2]) == "W":
    input()
  elif (rcube.cube[2][2][0]) == "B" and (rcube.cube[5][2][2] and rcube.cube[5][0][1]) == "R" and (rcube.cube[3][2][2]) == "W":
    input()
  elif (rcube.cube[2][2][0]) == "B" and (rcube.cube[5][2][2] and rcube.cube[5][1][0]) == "R" and (rcube.cube[3][2][2]) == "W":
    input()  
  elif (rcube.cube[2][2][0] and rcube.cube[5][1][2]) == "B" and (rcube.cube[5][2][2] and rcube.cube[3][2][1]) == "R" and (rcube.cube[3][2][2]) == "W":
    input()  
  elif (rcube.cube[2][2][0] and rcube.cube[5][1][0]) == "B" and (rcube.cube[5][2][2]) == "R" and (rcube.cube[3][2][2]) == "W":
    input()  
  elif (rcube.cube[2][2][0] and rcube.cube[5][2][1]) == "B" and (rcube.cube[5][2][2] and rcube.cube[2][2][1]) == "R" and (rcube.cube[3][2][2]) == "W":
    input()  
  elif (rcube.cube[5][2][2] and rcube.cube[5][2][1]) == "B" and (rcube.cube[3][2][2] and rcube.cube[2][2][1]) == "R" and (rcube.cube[2][2][0]) == "W":
    input()
  elif (rcube.cube[5][2][2] and rcube.cube[5][1][0]) == "B" and (rcube.cube[3][2][2]) == "R" and (rcube.cube[2][2][0]) == "W":
    input()  
  elif (rcube.cube[5][2][2] and rcube.cube[5][0][1]) == "B" and (rcube.cube[3][2][2]) == "R" and (rcube.cube[2][2][0]) == "W":
    input()
  elif (rcube.cube[5][2][2] and rcube.cube[2][2][1]) == "B" and (rcube.cube[3][2][2] and rcube.cube[5][2][1]) == "R" and (rcube.cube[2][2][0]) == "W":
    input()
  elif (rcube.cube[5][2][2]) == "B" and (rcube.cube[3][2][2] and rcube.cube[5][0][1]) == "R" and (rcube.cube[2][2][0]) == "W":
    input()
  elif (rcube.cube[5][2][2] and rcube.cube[3][2][1]) == "B" and (rcube.cube[3][2][2] and rcube.cube[5][1][2]) == "R" and (rcube.cube[2][2][0]) == "W":
    input()  
  print("\n")
  rcube.display_cube()
"""


# The second attempt splits F2l into 2 steps
# The corners and the second layer
# Start and impossible are imported to check if the cube is impossible
def U_corners(start, impossible):
    # local moves and local alg to count and record the moves made
    local_alg = ""
    local_moves = 0
    print("\n********************U Corners********************\n")
    # a while loop that checks if all the white corners are in the correct position and oriented correctly
    # It also checks if the cube has been flagged as impossible
    while ((rcube.cube[0][0][0] != rcube.cube[0][1][1] or rcube.cube[0][0][2] != rcube.cube[0][1][1] or
            rcube.cube[0][2][0] != rcube.cube[0][1][1] or rcube.cube[0][2][2] != rcube.cube[0][1][1]) or (
                   rcube.cube[4][0][0] or rcube.cube[4][0][2]) != rcube.cube[4][1][1] or (
                   rcube.cube[3][0][0] or rcube.cube[3][0][2]) != rcube.cube[3][1][1] or (
                   rcube.cube[2][0][0] or rcube.cube[2][0][2]) != rcube.cube[2][1][1] or (
                   rcube.cube[1][0][0] or rcube.cube[1][0][2]) != rcube.cube[1][1][1]) and impossible != True:

        # Checking if the cube has passed the threshold for being flagged as impossible
        if (time.time() - start) > 1:
            print("This cube is likely impossible")
            impossible = True
            break

        # A while loop if the white piece is in the bottom layer on the right side
        while rcube.cube[4][2][2] == rcube.cube[0][1][1] or rcube.cube[3][2][2] == rcube.cube[0][1][1] or \
                rcube.cube[2][2][2] == rcube.cube[0][1][1] or rcube.cube[1][2][2] == rcube.cube[0][1][1]:

            # Checking if the cube has passed the threshold for being flagged as impossible
            if (time.time() - start) > 1:
                print("This cube is likely impossible")
                impossible = True
                break

            # If the white piece is in the bottom right of the green face and the piece is correctly alligned
            if rcube.cube[4][2][2] == rcube.cube[0][1][1] and rcube.cube[3][2][0] == rcube.cube[3][1][1]:
                rcube.F()
                rcube.D()
                rcube.invF()
                local_alg += "F D F' "
                local_moves += 3
            # If the white piece is in the bottom right of the red face and the piece is correctly alligned
            elif rcube.cube[3][2][2] == rcube.cube[0][1][1] and rcube.cube[2][2][0] == rcube.cube[2][1][1]:
                rcube.R()
                rcube.D()
                rcube.invR()
                local_alg += "R D R' "
                local_moves += 3
            # If the white piece is in the bottom right of the blue face and the piece is correctly alligned
            elif rcube.cube[2][2][2] == rcube.cube[0][1][1] and rcube.cube[1][2][0] == rcube.cube[1][1][1]:
                rcube.B()
                rcube.D()
                rcube.invB()
                local_alg += "B D B' "
                local_moves += 3
            # If the white piece is in the bottom right of the orange face and the piece is correctly alligned
            elif rcube.cube[1][2][2] == rcube.cube[0][1][1] and rcube.cube[4][2][0] == rcube.cube[4][1][1]:
                rcube.L()
                rcube.D()
                rcube.invL()
                local_alg += "L D L' "
                local_moves += 3
            # If none of the above apply the piece is not correctly alligned so a D turn is performed to allign it
            else:
                rcube.D()
                local_alg += "D "
                local_moves += 1

        # A while loop for if a white piece is in the bottom layer on the left side
        while rcube.cube[4][2][0] == rcube.cube[0][1][1] or rcube.cube[3][2][0] == rcube.cube[0][1][1] or \
                rcube.cube[2][2][0] == rcube.cube[0][1][1] or rcube.cube[1][2][0] == rcube.cube[0][1][1]:

            # Checking if the cube has passed the threshold for being flagged as impossible
            if (time.time() - start) > 1:
                print("This cube is likely impossible")
                impossible = True
                break

            # If the white piece is in the bottom left of the green face and the piece is correctly alligned
            if rcube.cube[4][2][0] == rcube.cube[0][1][1] and rcube.cube[1][2][2] == rcube.cube[1][1][1]:
                rcube.invF()
                rcube.invD()
                rcube.F()
                local_alg += "F' D' F "
                local_moves += 3

            # If the white piece is in the bottom left of the red face and the piece is correctly alligned
            elif rcube.cube[3][2][0] == rcube.cube[0][1][1] and rcube.cube[4][2][2] == rcube.cube[4][1][1]:
                rcube.invR()
                rcube.invD()
                rcube.R()
                local_alg += "R' D' R "
                local_moves += 3
            # If the white piece is in the bottom left of the blue face and the piece is correctly alligned
            elif rcube.cube[2][2][0] == rcube.cube[0][1][1] and rcube.cube[3][2][2] == rcube.cube[3][1][1]:
                rcube.invB()
                rcube.invD()
                rcube.B()
                local_alg += "B' D' B "
                local_moves += 3
            # If the white piece is in the bottom left of the orange face and the piece is correctly alligned
            elif rcube.cube[1][2][0] == rcube.cube[0][1][1] and rcube.cube[2][2][2] == rcube.cube[2][1][1]:
                rcube.invL()
                rcube.invD()
                rcube.L()
                local_alg += "L' D' L "
                local_moves += 3
            # If none of the previous apply then the piece isn't correctly alligned so a D turn is performed to allign the piece
            else:
                rcube.D()
                local_alg += "D "
                local_moves += 1
        # A while loop for if a white piece is on the yellow face
        while rcube.cube[5][0][0] == rcube.cube[0][1][1] or rcube.cube[5][0][2] == rcube.cube[0][1][1] or \
                rcube.cube[5][2][0] == rcube.cube[0][1][1] or rcube.cube[5][2][2] == rcube.cube[0][1][1]:
            # Checking if the cube has passed the threshold for being flagged as impossible
            if (time.time() - start) > 1:
                print("This cube is likely impossible")
                impossible = True
                break

            # If the white piece is on the top right of the yellow face and is correctly alligned
            if rcube.cube[5][0][2] == rcube.cube[0][1][1] and rcube.cube[4][2][2] == rcube.cube[3][1][1] and \
                    rcube.cube[3][2][0] == rcube.cube[4][1][1]:
                rcube.invR()
                rcube.D()
                rcube.D()
                rcube.R()
                rcube.D()
                rcube.invR()
                rcube.invD()
                rcube.R()
                local_alg += "R' D D R D R' D' R "
                local_moves += 8

            # If the white piece is on the bottom right of the yellow face and is correctly alligned
            elif rcube.cube[5][2][2] == rcube.cube[0][1][1] and rcube.cube[3][2][2] == rcube.cube[2][1][1] and \
                    rcube.cube[2][2][0] == rcube.cube[3][1][1]:
                rcube.invB()
                rcube.D()
                rcube.D()
                rcube.B()
                rcube.D()
                rcube.invB()
                rcube.invD()
                rcube.B()
                local_alg += "B' D D B D B' D' B "
                local_moves += 8

            # If the white piece is on the bottom left of the yellow face and is correctly alligned
            elif rcube.cube[5][2][0] == rcube.cube[0][1][1] and rcube.cube[2][2][2] == rcube.cube[1][1][1] and \
                    rcube.cube[1][2][0] == rcube.cube[2][1][1]:
                rcube.invL()
                rcube.D()
                rcube.D()
                rcube.L()
                rcube.D()
                rcube.invL()
                rcube.invD()
                rcube.L()
                local_alg += "L' D D L D L' D' L "
                local_moves += 8

            # If the white piece is on the top left of the yellow face and is correctly alligned
            elif rcube.cube[5][0][0] == rcube.cube[0][1][1] and rcube.cube[1][2][2] == rcube.cube[4][1][1] and \
                    rcube.cube[4][2][0] == rcube.cube[1][1][1]:
                rcube.invF()
                rcube.D()
                rcube.D()
                rcube.F()
                rcube.D()
                rcube.invF()
                rcube.invD()
                rcube.F()
                local_alg += "F' D D F D F' D' F "
                local_moves += 8
            else:
                rcube.D()
                local_alg += "D "
                local_moves += 1
        # While loop for if the white piece isn't oriented correctly
        while rcube.cube[4][0][0] == rcube.cube[0][1][1] or rcube.cube[4][0][2] == rcube.cube[0][1][1] or \
                rcube.cube[3][0][0] == rcube.cube[0][1][1] or rcube.cube[3][0][2] == rcube.cube[0][1][1] or \
                rcube.cube[2][0][0] == rcube.cube[0][1][1] or rcube.cube[2][0][2] == rcube.cube[0][1][1] or \
                rcube.cube[1][0][0] == rcube.cube[0][1][1] or rcube.cube[1][0][2] == rcube.cube[0][1][1]:

            # Checking if the cube has passed the threshold for being flagged as impossible
            if (time.time() - start) > 1:
                print("This cube is likely impossible")
                impossible = True
                break

            # If the white piece is in the top right on the green face or top left on the red face
            if rcube.cube[4][0][2] == rcube.cube[0][1][1] or rcube.cube[3][0][0] == rcube.cube[0][1][1]:
                rcube.invR()
                rcube.D()
                rcube.R()
                local_alg += "R' D R "
                local_moves += 3

            # If the white piece is in the top right on the red face or top left on the blue face
            elif rcube.cube[3][0][2] == rcube.cube[0][1][1] or rcube.cube[2][0][0] == rcube.cube[0][1][1]:
                rcube.invB()
                rcube.D()
                rcube.B()
                local_alg += "B' D B "
                local_moves += 3

            # If the white piece is in the top right on the blue face or top left on the orange face
            elif rcube.cube[2][0][2] == rcube.cube[0][1][1] or rcube.cube[1][0][0] == rcube.cube[0][1][1]:
                rcube.invL()
                rcube.D()
                rcube.L()
                local_alg += "L' D L "
                local_moves += 3

            # If the white piece is in the top right on the orange face or top left on the green face
            # else is used here as it's the only other possibility within the while loop
            else:
                rcube.invF()
                rcube.D()
                rcube.F()
                local_alg += "F' D F "
                local_moves += 3

        # A while loop for if all white pieces are on the white face but are not alligned correctly
        # Methods in here attempt to bring the white piece back down to the bottom layer so it can be re-alligned
        while rcube.cube[0][0][0] == rcube.cube[0][1][1] and rcube.cube[0][0][2] == rcube.cube[0][1][1] and \
                rcube.cube[0][2][0] == rcube.cube[0][1][1] and rcube.cube[0][2][2] == rcube.cube[0][1][1] and (
                rcube.cube[4][0][0] != rcube.cube[4][1][1] or rcube.cube[4][0][2] != rcube.cube[4][1][1] or
                rcube.cube[2][0][0] != rcube.cube[2][1][1] or rcube.cube[2][0][2] != rcube.cube[2][1][1]):

            # Checking if the cube has passed the threshold for being flagged as impossible
            if (time.time() - start) > 1:
                print("This cube is likely impossible")
                impossible = True
                break

            # If the bottom left white corner isn't alligned correctly
            if rcube.cube[0][2][0] == rcube.cube[0][1][1] and rcube.cube[4][0][0] != rcube.cube[4][1][1]:
                rcube.L()
                rcube.D()
                rcube.invL()
                local_alg += "L D L' "
                local_moves += 3

            # If the bottom right white corner isn't alligned correctly
            elif rcube.cube[0][2][2] == rcube.cube[0][1][1] and rcube.cube[4][0][2] != rcube.cube[4][1][1]:
                rcube.invR()
                rcube.D()
                rcube.R()
                local_alg += "R' D R "
                local_moves += 3

            # If the top right white corner isn't alligned correctly
            elif rcube.cube[0][0][2] == rcube.cube[0][1][1] and rcube.cube[4][0][2] != rcube.cube[4][1][1]:
                rcube.R()
                rcube.D()
                rcube.invR()
                local_alg += "R D R' "
                local_moves += 3
            # If the top left white corner isn't alligned correctly
            # Else is used here as it's the only other possibility within this while loop
            else:
                rcube.invL()
                rcube.D()
                rcube.L()
                local_alg += "L' D L "
                local_moves += 3
    # Final algorithm for the step is printed and the move counter and algorithm are returned
    print(f"Moves taken: {local_moves}")
    print(local_alg)
    rcube.display_cube()
    return local_moves, local_alg, impossible


def second_layer(start, impossible):
    # local moves and local alg to count and record the moves made
    local_alg = ""
    local_moves = 0
    print("\n********************Second Layer********************\n")
    # A while loop that checks if all corners are in the correct position and correctly oriented as well as if the cube has been flagged as impossible
    while (rcube.cube[4][1][0] != rcube.cube[4][1][1] or rcube.cube[4][1][2] != rcube.cube[4][1][1] or rcube.cube[3][1][
        0] != rcube.cube[3][1][1] or rcube.cube[3][1][2] != rcube.cube[3][1][1] or rcube.cube[2][1][0] !=
           rcube.cube[2][1][1] or rcube.cube[2][1][2] != rcube.cube[2][1][1] or rcube.cube[1][1][0] != rcube.cube[1][1][
               1] or rcube.cube[1][1][2] != rcube.cube[1][1][1]) and impossible != True:

        # Checking if the cube has passed the threshold for being flagged as impossible
        if (time.time() - start) > 1:
            print("This cube is likely impossible")
            impossible = True
            break

        # A while loop for if an edge is in the bottom layer
        while (rcube.cube[4][2][1] != rcube.cube[5][1][1] and rcube.cube[5][0][1] != rcube.cube[5][1][1]) or (
                rcube.cube[3][2][1] != rcube.cube[5][1][1] and rcube.cube[5][1][2] != rcube.cube[5][1][1]) or (
                rcube.cube[2][2][1] != rcube.cube[5][1][1] and rcube.cube[5][2][1] != rcube.cube[5][1][1]) or (
                rcube.cube[1][2][1] != rcube.cube[5][1][1] and rcube.cube[5][1][0] != rcube.cube[5][1][1]):

            # Checking if the cube has passed the threshold for being flagged as impossible
            if (time.time() - start) > 1:
                print("This cube is likely impossible")
                impossible = True
                break

            # If the edge piece is in the top row of the red face and correctly alligned
            if rcube.cube[4][2][1] == rcube.cube[4][1][1] and rcube.cube[5][0][1] != rcube.cube[5][1][1]:
                local_moves += 8
                # If the edge piece needs to move to the right
                if rcube.cube[5][0][1] == rcube.cube[3][1][1]:
                    rcube.invD()
                    rcube.invR()
                    rcube.D()
                    rcube.R()
                    rcube.D()
                    rcube.F()
                    rcube.invD()
                    rcube.invF()
                    local_alg += "D' R' D R D F D' F' "
                # If the edge piece needs to move to the left
                else:
                    rcube.D()
                    rcube.L()
                    rcube.invD()
                    rcube.invL()
                    rcube.invD()
                    rcube.invF()
                    rcube.D()
                    rcube.F()
                    local_alg += "D L D' L' D' F' D F "
            # If the edge piece is on the right side of the yellow face and correctly alligned
            if rcube.cube[3][2][1] == rcube.cube[3][1][1] and rcube.cube[5][1][2] != rcube.cube[5][1][1]:
                local_moves += 8
                # If the edge piece needs to move to the right
                if rcube.cube[5][1][2] == rcube.cube[2][1][1]:
                    rcube.invD()
                    rcube.invB()
                    rcube.D()
                    rcube.B()
                    rcube.D()
                    rcube.R()
                    rcube.invD()
                    rcube.invR()
                    local_alg += "D' B' D B D R D' R' "
                # If the edge piece needs to move to the left
                else:
                    rcube.D()
                    rcube.F()
                    rcube.invD()
                    rcube.invF()
                    rcube.invD()
                    rcube.invR()
                    rcube.D()
                    rcube.R()
                    local_alg += "D F D' F' D' R' D R "
            # If the edge piece is on the bottom row of the yellow face and correctly alligned
            if rcube.cube[2][2][1] == rcube.cube[2][1][1] and rcube.cube[5][2][1] != rcube.cube[5][1][1]:
                local_moves += 8
                # If the edge piece needs to move to the right
                if rcube.cube[5][2][1] == rcube.cube[1][1][1]:
                    rcube.invD()
                    rcube.invL()
                    rcube.D()
                    rcube.L()
                    rcube.D()
                    rcube.B()
                    rcube.invD()
                    rcube.invB()
                    local_alg += "D' L' D L D B D' B' "
                # If the edge piece needs to move to the left
                else:
                    rcube.D()
                    rcube.R()
                    rcube.invD()
                    rcube.invR()
                    rcube.invD()
                    rcube.invB()
                    rcube.D()
                    rcube.B()
                    local_alg += "D R D' R' D' B' D B "
            # If the edge piece is on the left side of the yellow face and correctly alligned
            if rcube.cube[1][2][1] == rcube.cube[1][1][1] and rcube.cube[5][1][0] != rcube.cube[5][1][1]:
                local_moves += 8
                # If the edge piece needs to move to the right
                if rcube.cube[5][1][0] == rcube.cube[4][1][1]:
                    rcube.invD()
                    rcube.invF()
                    rcube.D()
                    rcube.F()
                    rcube.D()
                    rcube.L()
                    rcube.invD()
                    rcube.invL()
                    local_alg += "D' F' D F D L D' L' "
                # If the edge piece needs to move to the left
                else:
                    rcube.D()
                    rcube.B()
                    rcube.invD()
                    rcube.invB()
                    rcube.invD()
                    rcube.invL()
                    rcube.D()
                    rcube.L()
                    local_alg += "D B D' B' D' L' D L "
            # If none of the previous statements apply then the edge piece is not correctly alligned so a D turn is performed
            else:
                local_moves += 1
                rcube.D()
                local_alg += "D "
        # Initially a while loop was set up here for if the edge pieces where in the wrong place or they were miss oriented, however it is unlikely that more than one of these edges would need to be moved at once so the while state ment was removed
        """while (rcube.cube[4][1][2] != rcube.cube[4][1][1] and rcube.cube[4][1][2] != rcube.cube[5][1][1] and rcube.cube[3][1][0] != rcube.cube[3][1][1] and rcube.cube[3][1][0] != rcube.cube[5][1][1]) or (rcube.cube[3][1][2] != rcube.cube[2][1][1] and rcube.cube[3][1][2] != rcube.cube[5][1][1] and rcube.cube[2][1][0] != rcube.cube[3][1][1] and rcube.cube[2][1][0] != rcube.cube[5][1][1]) or (rcube.cube[2][1][2] != rcube.cube[1][1][1] and rcube.cube[2][1][2] != rcube.cube[5][1][1] and rcube.cube[1][1][0] != rcube.cube[2][1][1] and rcube.cube[1][1][0] != rcube.cube[5][1][1]) or (rcube.cube[1][1][2] != rcube.cube[4][1][1] and rcube.cube[1][1][2] != rcube.cube[5][1][1] and rcube.cube[4][1][0] == rcube.cube[1][1][1] and rcube.cube[4][1][0] != rcube.cube[5][1][1]):"""
        # To fix a wrongly oriented edge piece the program performs the algorithm for moving an edge piece to the left
        # If the edge piece on the right side of the green face is wrong
        if (rcube.cube[4][1][2] != rcube.cube[4][1][1] and rcube.cube[4][1][2] != rcube.cube[5][1][1]) or (
                rcube.cube[3][1][0] != rcube.cube[3][1][1] and rcube.cube[3][1][0] != rcube.cube[5][1][1]):
            local_moves += 8
            rcube.D()
            rcube.F()
            rcube.invD()
            rcube.invF()
            rcube.invD()
            rcube.invR()
            rcube.D()
            rcube.R()
            local_alg += "D F D' F' D' R' D R "
        # If the edge piece on the right side of the red face is wrong
        elif (rcube.cube[3][1][2] != rcube.cube[3][1][1] and rcube.cube[3][1][2] != rcube.cube[5][1][1]) or (
                rcube.cube[2][1][0] != rcube.cube[2][1][1] and rcube.cube[2][1][0] != rcube.cube[5][1][1]):
            local_moves += 8
            rcube.D()
            rcube.R()
            rcube.invD()
            rcube.invR()
            rcube.invD()
            rcube.invB()
            rcube.D()
            rcube.B()
            local_alg += "D R D' R' D' B' D B "
        # If the edge piece on the right side of the blue face is wrong
        elif (rcube.cube[2][1][2] != rcube.cube[2][1][1] and rcube.cube[2][1][2] != rcube.cube[5][1][1]) or (
                rcube.cube[1][1][0] != rcube.cube[1][1][1] and rcube.cube[1][1][0] != rcube.cube[5][1][1]):
            local_moves += 8
            rcube.D()
            rcube.B()
            rcube.invD()
            rcube.invB()
            rcube.invD()
            rcube.invL()
            rcube.D()
            rcube.L()
            local_alg += "D B D' B' D' L' D L "
        # If the edge piece on the right side of the orange face is wrong
        elif (rcube.cube[1][1][2] != rcube.cube[1][1][1] and rcube.cube[1][1][2] != rcube.cube[5][1][1]) or (
                rcube.cube[4][1][0] != rcube.cube[4][1][1] and rcube.cube[4][1][0] != rcube.cube[5][1][1]):
            local_moves += 8
            rcube.D()
            rcube.L()
            rcube.invD()
            rcube.invL()
            rcube.invD()
            rcube.invF()
            rcube.D()
            rcube.F()
            local_alg += "D L D' L' D' F' D F"
    # Final algorithm for the step is printed and the move counter and algorithm are returned
    print(f"Moves taken: {local_moves}")
    print(local_alg)
    rcube.display_cube()
    return local_moves, local_alg, impossible


# A simpler version of OLL is used here called 2-look OLL which reduces the amount of algorithms from 57 to 9(not including different orientations) and splits it into 2 steps
def D_cross(start, impossible):
    # local moves and local alg to count and record the moves made
    local_alg = ""
    local_moves = 0

    print("\n********************D Cross********************\n")

    # No while loop is needed here as only one set of moves has to be performed
    # The program looks to see which pattern (and orientation of pattern) is present and performs a series of moves to create a yellow cross depending on the pattern

    # If the dot pattern is present
    if rcube.cube[4][2][1] == rcube.cube[3][2][1] == rcube.cube[2][2][1] == rcube.cube[1][2][1] == rcube.cube[5][1][1]:
        rcube.F()
        rcube.L()
        rcube.D()
        rcube.invL()
        rcube.invD()
        rcube.invF()
        rcube.B()  # f
        rcube.D()
        rcube.R()
        rcube.invD()
        rcube.invR()
        rcube.invB()
        local_alg += "F L D L' D' F' B D R D' R' B' "
        local_moves += 12

    # If the horizontal line shape is present
    elif rcube.cube[4][2][1] == rcube.cube[2][2][1] == rcube.cube[5][1][0] == rcube.cube[5][1][2] == rcube.cube[5][1][
        1]:
        rcube.F()
        rcube.L()
        rcube.D()
        rcube.invL()
        rcube.invD()
        rcube.invF()
        local_alg += "F L D L' D' F' "
        local_moves += 6

    # If the vertical line shape is present
    elif rcube.cube[3][2][1] == rcube.cube[1][2][1] == rcube.cube[5][0][1] == rcube.cube[5][2][1] == rcube.cube[5][1][
        1]:
        rcube.L()
        rcube.B()
        rcube.D()
        rcube.invB()
        rcube.invD()
        rcube.invL()
        local_alg += "L B D B' D' L' "
        local_moves += 6

    # If a green-orange L shape is present
    elif rcube.cube[5][0][1] == rcube.cube[5][1][0] == rcube.cube[3][2][1] == rcube.cube[2][2][1] == rcube.cube[5][1][
        1]:
        rcube.B()  # f
        rcube.D()
        rcube.R()
        rcube.invD()
        rcube.invR()
        rcube.invB()
        local_alg += "B D R D' R' B' "
        local_moves += 6

    # If a green-red L shape is present
    elif rcube.cube[5][0][1] == rcube.cube[5][1][2] == rcube.cube[2][2][1] == rcube.cube[1][2][1] == rcube.cube[5][1][
        1]:
        rcube.L()  # r
        rcube.D()
        rcube.B()
        rcube.invD()
        rcube.invB()
        rcube.invL()
        local_alg += "L D B D' B' L' "
        local_moves += 6

    # If a red-blue L shape is present
    elif rcube.cube[5][2][1] == rcube.cube[5][1][2] == rcube.cube[4][2][1] == rcube.cube[1][2][1] == rcube.cube[5][1][
        1]:
        rcube.F()  # b
        rcube.D()
        rcube.L()
        rcube.invD()
        rcube.invL()
        rcube.invF()
        local_alg += "F D L D' L' F' "
        local_moves += 6

    # If a blue-orange L shape is present
    elif rcube.cube[5][1][0] == rcube.cube[5][2][1] == rcube.cube[4][2][1] == rcube.cube[3][2][1] == rcube.cube[5][1][
        1]:
        rcube.R()  # l
        rcube.D()
        rcube.F()
        rcube.invD()
        rcube.invF()
        rcube.invR()
        local_alg += "R D F D' F' R' "
        local_moves += 6

    # Final algorithm for the step is printed and the move counter and algorithm are returned
    print(f"Moves taken: {local_moves}")
    print(local_alg)
    rcube.display_cube()
    return local_moves, local_alg, impossible


def D_corners(start, impossible):
    # local moves and local alg to count and record the moves made
    local_alg = ""
    local_moves = 0
    print("\n********************D Corners********************\n")
    # Techincally a while loop is not necessary here as if all orientations are programmed in then the program will only have to sue one of them, however this would take much longer to code and would give negligible amounts of efficiency. Instead a D turn is set up at the end to re-allign the pieces.
    # This step (similairly to the previous step) looks for different possible patterns and performs a set of moves based on which one of these patterns appear
    # While loop to check if the yellow corners are in the right orientation or if the cube has been flagged as impossible
    while (rcube.cube[5][0][0] != rcube.cube[5][1][1] or rcube.cube[5][0][2] != rcube.cube[5][1][1] or rcube.cube[5][2][
        0] != rcube.cube[5][1][1] or rcube.cube[5][2][2] != rcube.cube[5][1][1]) and impossible != True:

        # Checking if the cube has passed the threshold for being flagged as impossible
        if (time.time() - start) > 1:
            print("This cube is likely impossible")
            impossible = True
            break

        # If the Antisune pattern is present
        if rcube.cube[5][2][0] == rcube.cube[4][2][2] == rcube.cube[1][2][2] == rcube.cube[3][2][2] == rcube.cube[5][1][
            1]:
            rcube.L()
            rcube.D()
            rcube.D()
            rcube.invL()
            rcube.invD()
            rcube.L()
            rcube.invD()
            rcube.invL()
            local_alg += "L D D L' D' L D' L' "
            local_moves += 8
        # If the H pattern is present
        elif rcube.cube[3][2][0] == rcube.cube[3][2][2] == rcube.cube[1][2][0] == rcube.cube[1][2][2] == \
                rcube.cube[5][1][1]:
            rcube.L()
            rcube.D()
            rcube.invL()
            rcube.D()
            rcube.L()
            rcube.invD()
            rcube.invL()
            rcube.D()
            rcube.L()
            rcube.D()
            rcube.D()
            rcube.invL()
            local_alg += "L D L' D L D' L' D L D D L' "
            local_moves += 12
        # If the L pattern is present
        elif rcube.cube[5][0][0] == rcube.cube[5][2][2] == rcube.cube[4][2][2] == rcube.cube[1][2][0] == \
                rcube.cube[5][1][1]:
            rcube.F()
            rcube.invL()
            rcube.invF()
            rcube.R()  # l
            rcube.F()
            rcube.L()
            rcube.invF()
            rcube.invR()
            local_alg += "F L' F' R F L F' R' "
            local_moves += 8
        # If the Pi pattern is present
        elif rcube.cube[4][2][0] == rcube.cube[3][2][0] == rcube.cube[3][2][2] == rcube.cube[2][2][2] == \
                rcube.cube[5][1][1]:
            rcube.L()
            rcube.D()
            rcube.D()
            rcube.L()
            rcube.L()
            rcube.invD()
            rcube.L()
            rcube.L()
            rcube.invD()
            rcube.L()
            rcube.L()
            rcube.D()
            rcube.D()
            rcube.L()
            local_alg += "L D D L L D' L L D' L L D D L "
            local_moves += 14
        # If the Sune pattern is present
        elif rcube.cube[5][0][2] == rcube.cube[2][2][0] == rcube.cube[1][2][0] == rcube.cube[4][2][0] == \
                rcube.cube[5][1][1]:
            rcube.L()
            rcube.D()
            rcube.invL()
            rcube.D()
            rcube.L()
            rcube.D()
            rcube.D()
            rcube.invL()
            local_alg += "L D L' D L D D L' "
            local_moves += 8
        # If the T pattern is present
        elif rcube.cube[5][0][0] == rcube.cube[5][2][0] == rcube.cube[2][2][0] == rcube.cube[4][2][2] == \
                rcube.cube[5][1][1]:
            rcube.R()  # l
            rcube.F()
            rcube.invL()
            rcube.invF()
            rcube.invR()
            rcube.F()
            rcube.L()
            rcube.invF()
            local_alg += "R F L' F' R' F L F' "
            local_moves += 8
        # If the U pattern is present
        elif rcube.cube[5][2][0] == rcube.cube[5][2][2] == rcube.cube[4][2][2] == rcube.cube[4][2][0] == \
                rcube.cube[5][1][1]:
            rcube.L()
            rcube.L()
            rcube.U()
            rcube.invL()
            rcube.D()
            rcube.D()
            rcube.L()
            rcube.invU()
            rcube.invL()
            rcube.D()
            rcube.D()
            rcube.invL()
            local_alg += "L L U L' D D L U' L' D D L' "
            local_moves += 12
        # If no pattern is correctly oriented
        else:
            rcube.D()
            local_alg += "D "
            local_moves += 1
    # Final algorithm for the step is printed and the move counter and algorithm are returned
    print(f"Moves taken: {local_moves}")
    print(local_alg)
    rcube.display_cube()
    return local_moves, local_alg, impossible


# The same is done for PLL, going from 21 to 6 algorithms (not including different orientations)
# Though PLL is done in the opposite order, with corners first and edges second.
def PLL1(start, impossible):
    # local moves and local alg to count and record the moves made
    local_alg = ""
    local_moves = 0
    print("\n********************Permute Corners********************\n")
    # This step can require mroe than one pass so a while loop is used
    # The while loop checks if the bottom layer corners are in the correct place or the cube has been flagged as impossible
    while (rcube.cube[4][2][0] != rcube.cube[4][1][1] or rcube.cube[4][2][2] != rcube.cube[4][1][1] or rcube.cube[3][2][
        0] != rcube.cube[3][1][1] or rcube.cube[3][2][2] != rcube.cube[3][1][1] or rcube.cube[2][2][0] !=
           rcube.cube[2][1][1] or rcube.cube[2][2][2] != rcube.cube[2][1][1] or rcube.cube[1][2][0] != rcube.cube[1][1][
               1] or rcube.cube[1][2][2] != rcube.cube[1][1][1]) and impossible != True:

        # Checking if the cube has passed the threshold for being flagged as impossible
        if (time.time() - start) > 1:
            print("This cube is likely impossible")
            impossible = True
            break

        # If the top left yellow corner needs to be swapped with the bottom right corner
        if (rcube.cube[4][2][0] == rcube.cube[2][1][1] and rcube.cube[1][2][2] == rcube.cube[3][1][1]) or (
                rcube.cube[2][2][0] == rcube.cube[4][1][1] and rcube.cube[3][2][2] == rcube.cube[1][1][1]):
            rcube.F()
            rcube.L()
            rcube.invD()
            rcube.invL()
            rcube.invD()
            rcube.L()
            rcube.D()
            rcube.invL()
            rcube.invF()
            rcube.L()
            rcube.D()
            rcube.invL()
            rcube.invD()
            rcube.invL()
            rcube.F()
            rcube.L()
            rcube.invF()
            local_alg += "F L D' L' D' L D L' F' L D L' D' L' F L F' "
            local_moves += 17
        # If the top right yellow corner needs to be swapped with the bottom left corner
        elif (rcube.cube[4][2][2] == rcube.cube[2][1][1] and rcube.cube[3][2][0] == rcube.cube[1][1][1]) or (
                rcube.cube[2][2][2] == rcube.cube[4][1][1] and rcube.cube[1][2][0] == rcube.cube[3][1][1]):
            rcube.R()
            rcube.F()
            rcube.invD()
            rcube.invF()
            rcube.invD()
            rcube.F()
            rcube.D()
            rcube.invF()
            rcube.invR()
            rcube.F()
            rcube.D()
            rcube.invF()
            rcube.invD()
            rcube.invF()
            rcube.R()
            rcube.F()
            rcube.invR()
            local_alg += "R F D' F' D' F D F' R' F D F' D' F' R F R' "
            local_moves += 17
        # If the top left yellow corner needs to be swapped with the bottom left corner
        elif (rcube.cube[4][2][0] == rcube.cube[1][1][1] and rcube.cube[1][2][2] == rcube.cube[2][1][1]) or (
                rcube.cube[2][2][2] == rcube.cube[1][1][1] and rcube.cube[1][2][0] == rcube.cube[4][1][1]):
            rcube.L()
            rcube.D()
            rcube.invL()
            rcube.invD()
            rcube.invL()
            rcube.F()
            rcube.L()
            rcube.L()
            rcube.invD()
            rcube.invL()
            rcube.invD()
            rcube.L()
            rcube.D()
            rcube.invL()
            rcube.invF()
            local_alg += "L D L' D' L' F L L D' L' D' L D L' F' "
            local_moves += 15
        # If the bottom left yellow corner needs to be swapped with the bottom right corner
        elif (rcube.cube[1][2][0] == rcube.cube[2][1][1] and rcube.cube[2][2][2] == rcube.cube[3][1][1]) or (
                rcube.cube[3][2][2] == rcube.cube[2][1][1] and rcube.cube[2][2][0] == rcube.cube[1][1][1]):
            rcube.B()
            rcube.D()
            rcube.invB()
            rcube.invD()
            rcube.invB()
            rcube.L()
            rcube.B()
            rcube.B()
            rcube.invD()
            rcube.invB()
            rcube.invD()
            rcube.B()
            rcube.D()
            rcube.invB()
            rcube.invL()
            local_alg += "B D B' D' B' L B B D' B' D' B D B' L' "
            local_moves += 15
        # If the bottom right yellow corner needs to be swapped with the top right corner
        elif (rcube.cube[2][2][0] == rcube.cube[3][1][1] and rcube.cube[3][2][2] == rcube.cube[4][1][1]) or (
                rcube.cube[4][2][2] == rcube.cube[3][1][1] and rcube.cube[3][2][0] == rcube.cube[2][1][1]):
            rcube.R()
            rcube.D()
            rcube.invR()
            rcube.invD()
            rcube.invR()
            rcube.B()
            rcube.R()
            rcube.R()
            rcube.invD()
            rcube.invR()
            rcube.invD()
            rcube.R()
            rcube.D()
            rcube.invR()
            rcube.invB()
            local_alg += "R D R' D' R' B R R D' R' D' R D R' B' "
            local_moves += 15
        # If the top right yellow corner needs to be swapped with the top left corner
        elif (rcube.cube[3][2][0] == rcube.cube[4][1][1] and rcube.cube[4][2][2] == rcube.cube[1][1][1]) or (
                rcube.cube[1][2][2] == rcube.cube[4][1][1] and rcube.cube[4][2][0] == rcube.cube[3][1][1]):
            rcube.F()
            rcube.D()
            rcube.invF()
            rcube.invD()
            rcube.invF()
            rcube.R()
            rcube.F()
            rcube.F()
            rcube.invD()
            rcube.invF()
            rcube.invD()
            rcube.F()
            rcube.D()
            rcube.invF()
            rcube.invR()
            local_alg += "F D F' D' F' R F F D' F' D' F D F' R' "
            local_moves += 15
    # Final algorithm for the step is printed and the move counter and algorithm are returned
    print(f"Moves taken: {local_moves}")
    print(local_alg)
    rcube.display_cube()
    return local_moves, local_alg, impossible


def PLL2(start, impossible):
    # local moves and local alg to count and record the moves made
    local_alg = ""
    local_moves = 0
    print("\n********************Permute Edges********************\n")
    # This step is very similar to D_cross as it also only has to complete one set of moves and therefor doesn't need a while loop. Similarly to D_cross, again, is that this step attempts to find different orientations of patterns
    # The H pattern only has one possible orientation
    if rcube.cube[4][2][1] == rcube.cube[2][1][1] and rcube.cube[2][2][1] == rcube.cube[4][1][1]:
        rcube.L()
        rcube.invR()
        rcube.L()
        rcube.invR()
        rcube.U()
        rcube.L()
        rcube.invR()
        rcube.L()
        rcube.invR()
        rcube.D()
        rcube.D()
        rcube.L()
        rcube.invR()
        rcube.L()
        rcube.invR()
        rcube.U()
        rcube.L()
        rcube.invR()
        rcube.L()
        rcube.invR()
        local_alg += "L R' L R' U L R' L R' D D L R' L R' U L R' L R' "
        local_moves += 20
    # The Ua pattern has 4 possible orientations
    # If red, green and orange need to be swapped anticlockwise
    elif rcube.cube[4][2][1] == rcube.cube[1][1][1] and rcube.cube[1][2][1] == rcube.cube[3][1][1]:
        rcube.L()
        rcube.invD()
        rcube.L()
        rcube.D()
        rcube.L()
        rcube.D()
        rcube.L()
        rcube.invD()
        rcube.invL()
        rcube.invD()
        rcube.L()
        rcube.L()
        local_alg += "L D' L D L D L  D' L' D' L L "
        local_moves += 12
    # If blue, green and orange need to be swapped anticlockwise
    elif rcube.cube[1][2][1] == rcube.cube[2][1][1] and rcube.cube[2][2][1] == rcube.cube[4][1][1]:
        rcube.B()
        rcube.invD()
        rcube.B()
        rcube.D()
        rcube.B()
        rcube.D()
        rcube.B()
        rcube.invD()
        rcube.invB()
        rcube.invD()
        rcube.B()
        rcube.B()
        local_alg += "B D' B D B D B D' B' D' B B "
        local_moves += 12
    # If red, blue and orange need to be swapped anticlockwise
    elif rcube.cube[2][2][1] == rcube.cube[3][1][1] and rcube.cube[3][2][1] == rcube.cube[1][1][1]:
        rcube.R()
        rcube.invD()
        rcube.R()
        rcube.D()
        rcube.R()
        rcube.D()
        rcube.R()
        rcube.invD()
        rcube.invR()
        rcube.invD()
        rcube.R()
        rcube.R()
        local_alg += "R D' R D R D R D' R' D' R R "
        local_moves += 12
    # If red, green and blue need to be swapped anticlockwise
    elif rcube.cube[3][2][1] == rcube.cube[4][1][1] and rcube.cube[4][2][1] == rcube.cube[2][1][1]:
        rcube.F()
        rcube.invD()
        rcube.F()
        rcube.D()
        rcube.F()
        rcube.D()
        rcube.F()
        rcube.invD()
        rcube.invF()
        rcube.invD()
        rcube.F()
        rcube.F()
        local_alg += "F D' F D F D F D' F' D' F F "
        local_moves += 12
    # The Ub pattern also has 4
    # If red, green and orange need to be swapped clockwise
    elif rcube.cube[4][2][1] == rcube.cube[3][1][1] and rcube.cube[3][2][1] == rcube.cube[1][1][1]:
        rcube.L()
        rcube.L()
        rcube.D()
        rcube.L()
        rcube.D()
        rcube.invL()
        rcube.invD()
        rcube.invL()
        rcube.invD()
        rcube.invL()
        rcube.D()
        rcube.invL()
        local_alg += "L L D L D L' D' L' D' L' D L' "
        local_moves += 12
    # If red, blue and orange need to be swapped clockwise
    elif rcube.cube[3][2][1] == rcube.cube[2][1][1] and rcube.cube[2][2][1] == rcube.cube[4][1][1]:
        rcube.F()
        rcube.F()
        rcube.D()
        rcube.F()
        rcube.D()
        rcube.invF()
        rcube.invD()
        rcube.invF()
        rcube.invD()
        rcube.invF()
        rcube.D()
        rcube.invF()
        local_alg += "F F D F D F' D' F' D' F' D F' "
        local_moves += 12
    # If red, green and orange need to be swapped clockwise
    elif rcube.cube[2][2][1] == rcube.cube[1][1][1] and rcube.cube[1][2][1] == rcube.cube[3][1][1]:
        rcube.R()
        rcube.R()
        rcube.D()
        rcube.R()
        rcube.D()
        rcube.invR()
        rcube.invD()
        rcube.invR()
        rcube.invD()
        rcube.invR()
        rcube.D()
        rcube.invR()
        local_alg += "R R D R D R' D' R' D' R' D R' "
        local_moves += 12
    # If blue, green and orange need to be swapped clockwise
    elif rcube.cube[1][2][1] == rcube.cube[4][1][1] and rcube.cube[4][2][1] == rcube.cube[2][1][1]:
        rcube.B()
        rcube.B()
        rcube.D()
        rcube.B()
        rcube.D()
        rcube.invB()
        rcube.invD()
        rcube.invB()
        rcube.invD()
        rcube.invB()
        rcube.D()
        rcube.invB()
        local_alg += "B B D B D B' D' B' D' B' D B' "
        local_moves += 12
    # The Z pattern has 2 possible orientations
    # if green and red need to swap and orange and blue need to swap
    elif rcube.cube[1][2][1] == rcube.cube[2][1][1] and rcube.cube[4][2][1] == rcube.cube[3][1][1]:
        rcube.invL()
        rcube.R()
        rcube.F()
        rcube.invL()
        rcube.R()
        rcube.invL()
        rcube.R()
        rcube.B()
        rcube.invL()
        rcube.R()
        rcube.invL()
        rcube.R()
        rcube.F()
        rcube.invL()
        rcube.R()
        rcube.U()
        rcube.U()
        rcube.invL()
        rcube.R()
        rcube.invL()
        rcube.R()
        rcube.invD()
        local_alg += "L' R F L' R L' R B L' R L' F L' R U U L' R L' R D' "
        local_moves += 22
    # if green and orange need to swap and red and blue need to swap
    elif rcube.cube[4][2][1] == rcube.cube[1][1][1] and rcube.cube[3][2][1] == rcube.cube[2][1][1]:
        rcube.invF()
        rcube.B()
        rcube.R()
        rcube.invF()
        rcube.B()
        rcube.invF()
        rcube.B()
        rcube.L()
        rcube.invF()
        rcube.B()
        rcube.invF()
        rcube.B()
        rcube.R()
        rcube.invF()
        rcube.B()
        rcube.U()
        rcube.U()
        rcube.invF()
        rcube.B()
        rcube.invF()
        rcube.B()
        rcube.invD()
        local_alg += "F' B R F' B F' B L F' B F' B R F' B U U F' B F' B D' "
        local_moves += 22
    # Final algorithm for the step is printed and the move counter and algorithm are returned
    print(f"Moves taken: {local_moves}")
    print(local_alg)
    rcube.display_cube()
    return local_moves, local_alg, impossible


def CFOP(impossible):
    # A final function to group all the steps together as well as accumulate the time and moves
    # the try except loop tests if the cube was inputted fully, as empty spaces would lead to an out of bounds error
    try:
        # solve_alg and total_moves to accumulate the returned local_algs and local_moves
        solve_alg = ""
        total_moves = 0
        # start is defined here to record the time taken so that it can be put in the final output as well as being used to test if the cube is impossible
        start = time.time()
        # returned values have to be split before beign accumulated
        a, b, impossible = U_cross(start, impossible)
        total_moves += a
        solve_alg += b
        a, b, impossible = U_corners(start, impossible)
        total_moves += a
        solve_alg += b
        a, b, impossible = second_layer(start, impossible)
        total_moves += a
        solve_alg += b
        a, b, impossible = D_cross(start, impossible)
        total_moves += a
        solve_alg += b
        a, b, impossible = D_corners(start, impossible)
        total_moves += a
        solve_alg += b
        a, b, impossible = PLL1(start, impossible)
        total_moves += a
        solve_alg += b
        a, b, impossible = PLL2(start, impossible)
        total_moves += a
        solve_alg += b
        if impossible == False:
            print("Cube solved in", round(time.time() - start, 3), "seconds and", total_moves, "moves")
            print("Moves used:\n", solve_alg)

        else:
            print("An impossible cube was likely inputted and the program cannot solve it")
    except:
        print("An error has occured, it's likely that you have inputted the cube wrong")
