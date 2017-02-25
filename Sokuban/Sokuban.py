#map
m_col = 5
m_row = 5

#point
pt_x = 3
pt_y = 3

#player start
px = 1
py = 2

#box start
bx = 2
by = 2

#player new position
n_px = px
n_py = py

#box new position
n_bx = bx
n_by = by

def move (x_po,y_po,control):
    if control == "W":
         y_po -=1
    elif control == "S":
        y_po +=1
    elif control == "A":
        x_po -=1
    elif control == "D":
        x_po +=1
    return (x_po,y_po)

def checkmap (n_px, n_py, n_bx, n_by):
    if n_px < 0 or n_py < 0 or n_bx < 0 or n_by < 0 or n_px > m_row -1 or n_py > m_col -1 or n_bx > m_row -1 or n_by > m_col -1:
        print("Out of map, please try again: ")
    else:
        px = n_px
        py = n_py
        bx = n_bx
        by = n_by
    return (px, py, bx, by)

while True:
    for row in range (m_row):
        for col in range (m_col):
            if row == px and col == py:
                print("T ", end='')
            elif row == bx  and col == by:
                print("B ", end='')
            elif row == pt_x  and col== pt_y :
                print(". ", end='')
            else:
                print("_ ", end='')
        print()
    choice = input("What do you want? W,S,A,D: ").upper()
    if choice == "W":
        checkmap(n_py, n_px, n_bx, n_by)
        move(n_px, n_py,choice)
    else:
        print("Choose again: ")

