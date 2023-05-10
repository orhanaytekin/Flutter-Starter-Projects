letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
lt = ["a", "b", "c", "d", "e", "f", "g", "h", "i"
      "k", "l", "m", "n", "o", "p", "q", "r", "s",
      "u", "v", "w", "x", "y", "z"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
is_Valid = True


def program(kh, kv, bh, bv):

    is_attack_happened = False
    kh = numbers[letters.index(kh)]
    bh = numbers[letters.index(bh)]
    real_bh = bh
    real_bv = bv

    if kh == bh and kv == bv:
        print("They can't be in the same square")
        return

    possible_attacks_of_knight = [
        (kh+2, kv+1),
        (kh+2, kv-1),
        (kh-2, kv+1),
        (kh-2, kv-1),
        (kh+1, kv+2),
        (kh+1, kv-2),
        (kh-1, kv+2),
        (kh-1, kv-2),
    ]

    possible_attacks_of_bishop = []

    while bh-1 > 0 and bv-1 > 0:
        possible_attacks_of_bishop.append((bh-1, bv-1))
        bh = bh-1
        bv = bv-1
    while bh+1 < 9 and bv+1 < 9:
        possible_attacks_of_bishop.append((bh+1, bv+1))
        bh = bh+1
        bv = bv+1

    if (real_bh, real_bv) in possible_attacks_of_knight:
        print("Knight can attack bishop")
        is_attack_happened = True

    if (kh, kv) in possible_attacks_of_bishop:
        print("Bishop can attack knight")
        is_attack_happened = True

    if not is_attack_happened:
        print("Neither of them can attack each other")


def valid(inp, knight_or_bishop, is_horizontal):
    global is_Valid
    piece = knight_or_bishop
    if is_horizontal:
        if inp not in lt:
            print(f"Horizontal input for {knight_or_bishop} is not a letter")
            is_Valid = False
            return
        elif inp not in letters:
            print(
                f"Horizontal input for {knight_or_bishop} is not a proper letter")
            is_Valid = False
            return

    else:
        try:
            a = int(inp)
            if a not in numbers:
                print(
                    f"Vertical input for {knight_or_bishop} is not a proper number")
                is_Valid = False
                return

        except Exception:
            print(f"Vertical input for {knight_or_bishop} is not a number")
            is_Valid = False
            return


knight_hor, knight_ver, bishop_hor, bishop_ver = "", "", "", ""

if is_Valid:
    knight_hor = input(
        "Please enter horizontal position of the knight (a,b,c,d,e,f,g,h): ").lower()
    valid(knight_hor, "knight", True)
if is_Valid:
    knight_ver = input(
        "Please enter vertical position of the knight (1,2,3,4,5,6,7,8): ")
    valid(knight_ver, "knight", False)
if is_Valid:
    bishop_hor = input(
        "Please enter horizontal position of the bishop (a,b,c,d,e,f,g,h): ").lower()
    valid(bishop_hor, "bishop", True)
if is_Valid:
    bishop_ver = input(
        "Please enter vertical position of the bishop (1,2,3,4,5,6,7,8): ")
    valid(bishop_ver, "bishop", False)

if is_Valid:
    program(knight_hor, int(knight_ver), bishop_hor, int(bishop_ver))
