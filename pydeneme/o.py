import sys
wp =["p1","p2","p3","p4","p5","p6","p7","p8"]
bp =["P1","P2","P3","P4","P5","P6","P7","P8"]
white =["p1","p2","p3","p4","p5","p6","p7","p8","r1","n1","b1","qu","ki","b2","n2","r2"]
black =["P1","P2","P3","P4","P5","P6","P7","P8","R1","N1","B1","QU","KI","B2","N2","R2"]
wbishops=["b1","b2"]
bbishops=["B1","B2"]
combine = white+black
f=open(sys.argv[1],"r")
commands=[line.split() for line in f.readlines()]
f.close()
showmoves=["a1","a2","a3","a4","a5","a6","a7","a8","b1","b2","b3","b4","b5","b6","b7","b8","c1","c2","c3","c4","c5","c6","c7","c8","d1","d2","d3","d4","d5","d6","d7","d8","e1","e2","e3","e4","e5","e6","e7","e8","f1","f2","f3","f4","f5","f6","f7","f8","g1","g2","g3","g4","g5","g6","g7","g8","h1","h2","h3","h4","h5","h6","h7","h8"]

dict_all={"r1":"a1","n1":"b1x","b1":"c1","qu":"d1","ki":"e1","b2":"f1","n2":"g1","r2":"h1",
          "p1":"a2","p2":"b2x","p3":"c2","p4":"d2","p5":"e2","p6":"f2","p7":"g2","p8":"h2",
          "XP":"a3","XR":"b3","XS":"c3","XT":"d3","XU":"e3","XV":"f3","XY":"g3","XZ":"h3",
          "XH":"a4","XI":"b4","XJ":"c4","XK":"d4","XL":"e4","XM":"f4","XN":"g4","XO":"h4",
          "X9":"a5","XA":"b5","XB":"c5","XC":"d5","XD":"e5","XE":"f5","XF":"g5","XG":"h5",
          "X1":"a6","X2":"b6","X3":"c6","X4":"d6","X5":"e6","X6":"f6","X7":"g6","X8":"h6",
          "P1":"a7","P2":"b7","P3":"c7","P4":"d7","P5":"e7","P6":"f7","P7":"g7","P8":"h7",
          "R1":"a8","N1":"b8","B1":"c8","QU":"d8","KI":"e8","B2":"f8","N2":"g8","R2":"h8"}
dict_copy = {"r1":"a1","n1":"b1x","b1":"c1","qu":"d1","ki":"e1","b2":"f1","n2":"g1","r2":"h1",
          "p1":"a2","p2":"b2x","p3":"c2","p4":"d2","p5":"e2","p6":"f2","p7":"g2","p8":"h2",
          "XP":"a3","XR":"b3","XS":"c3","XT":"d3","XU":"e3","XV":"f3","XY":"g3","XZ":"h3",
          "XH":"a4","XI":"b4","XJ":"c4","XK":"d4","XL":"e4","XM":"f4","XN":"g4","XO":"h4",
          "X9":"a5","XA":"b5","XB":"c5","XC":"d5","XD":"e5","XE":"f5","XF":"g5","XG":"h5",
          "X1":"a6","X2":"b6","X3":"c6","X4":"d6","X5":"e6","X6":"f6","X7":"g6","X8":"h6",
          "P1":"a7","P2":"b7","P3":"c7","P4":"d7","P5":"e7","P6":"f7","P7":"g7","P8":"h7",
          "R1":"a8","N1":"b8","B1":"c8","QU":"d8","KI":"e8","B2":"f8","N2":"g8","R2":"h8"}
lst=["a1","a2","a3","a4","a5","a6","a7","a8","b1","b2","b3","b4","b5","b6","b7","b8","c1","c2","c3","c4","c5","c6","c7","c8","d1","d2","d3","d4","d5","d6","d7","d8","e1","e2","e3","e4","e5","e6","e7","e8","f1","f2","f3","f4","f5","f6","f7","f8","g1","g2","g3","g4","g5","g6","g7","g8","h1","h2","h3","h4","h5","h6","h7","h8"]

def finder(string):
    global dikey
    global yatay
    for i in range(8):
        for j in range(8):
            if board[i][j]==string:
                y = i
                x = j
                dikey,yatay = y,x
    return dikey,yatay

valid_moves_for_wp={"p1":"a3","p2":"b3","p3":"c3","p4":"d3",
                    "p5":"e3","p6":"f3","p7":"g3","p8":"h3"}
copy3 = {"p1":"a3","p2":"b3","p3":"c3","p4":"d3",
                    "p5":"e3","p6":"f3","p7":"g3","p8":"h3"}
copy4 = {"P1":"a6","P2":"b6","P3":"c6","P4":"d6",
                    "P5":"e6","P6":"f6","P7":"g6","P8":"h6"}
valid_moves_for_bp={"P1":"a6","P2":"b6","P3":"c6","P4":"d6",
                    "P5":"e6","P6":"f6","P7":"g6","P8":"h6"}
valid_moves_for_b1=[]
valid_moves_for_b2=[]
valid_moves_for_B1=[]
valid_moves_for_B2=[]
valid_moves_for_n1=[]
valid_moves_for_n2=[]
valid_moves_for_N1=[]
valid_moves_for_N2=[]
valid_moves_for_r1=[]
valid_moves_for_r2=[]
valid_moves_for_R1=[]
valid_moves_for_R2=[]
valid_moves_for_qu=[]
valid_moves_for_QU=[]
valid_moves_for_ki=[]
valid_moves_for_KI=[]
board=[["R1","N1","B1","QU","KI","B2","N2","R2"],
       ["P1","P2","P3","P4","P5","P6","P7","P8"],
       ["X1","X2","X3","X4","X5","X6","X7","X8"],
       ["X9","XA","XB","XC","XD","XE","XF","XG"],
       ["XH","XI","XJ","XK","XL","XM","XN","XO"],
       ["XP","XR","XS","XT","XU","XV","XY","XZ"],
       ["p1","p2","p3","p4","p5","p6","p7","p8"],
       ["r1","n1","b1","qu","ki","b2","n2","r2"]]
copy2 = [row[:] for row in board]

def is_valid(piece):
    global valid_moves_for_bp
    global valid_moves_for_wp
    global valid_moves_for_b1
    global valid_moves_for_b2
    global valid_moves_for_B1
    global valid_moves_for_B2
    global valid_moves_for_n1
    global valid_moves_for_n2
    global valid_moves_for_N1
    global valid_moves_for_N2
    global valid_moves_for_r1
    global valid_moves_for_r2
    global valid_moves_for_R1
    global valid_moves_for_R2
    global valid_moves_for_qu
    global valid_moves_for_QU
    global valid_moves_for_ki
    global valid_moves_for_KI
    finder(piece)
    #
    
    if piece=="b1" and dict_all["b1"]=="c1":
        if board[dikey-1][yatay-1] not in white  :
            valid_moves_for_b1.extend(["b2", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_b1.extend(["a3",board[dikey-2][yatay-2]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_b1.extend(["d2",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_b1.extend(["e3",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_b1.extend(["f4",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white:
            valid_moves_for_b1.extend(["g5",board[dikey-4][yatay+4]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white and board[dikey-5][yatay+5] not in white:
            valid_moves_for_b1.extend(["h6",board[dikey-5][yatay+5]])
    #
    if piece=="b1" and dict_all["b1"]=="b2":
        if board[dikey-1][yatay-1] not in white  :
            valid_moves_for_b1.extend(["a3", board[dikey-1][yatay-1]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_b1.extend(["c3",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_b1.extend(["d4",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_b1.extend(["e5",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white:
            valid_moves_for_b1.extend(["f6",board[dikey-4][yatay+4]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white and board[dikey-5][yatay+5] not in white:
            valid_moves_for_b1.extend(["g7",board[dikey-5][yatay+5]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white and board[dikey-5][yatay+5] not in white and board[dikey-6][yatay+6] not in white and board[dikey-5][yatay+5] not in black:
            valid_moves_for_b1.extend(["h8",board[dikey-6][yatay+6]])
    #
    if piece=="b1" and dict_all["b1"]=="a3":
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_b1.extend(["b4",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_b1.extend(["c5",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_b1.extend(["d6",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white:
            valid_moves_for_b1.extend(["e7",board[dikey-4][yatay+4]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white  and board[dikey-4][yatay+4] not in black and board[dikey-5][yatay+5] not in white:
            valid_moves_for_b1.extend(["f8",board[dikey-5][yatay+5]])
    #
    if piece=="b1" and dict_all["b1"]=="c3":
        if board[dikey-1][yatay-1] not in white  :
            valid_moves_for_b1.extend(["b4", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_b1.extend(["a5",board[dikey-2][yatay-2]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_b1.extend(["d4",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_b1.extend(["e5",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_b1.extend(["f6",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white:
            valid_moves_for_b1.extend(["g7",board[dikey-4][yatay+4]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white and board[dikey-4][yatay+4] not in black and board[dikey-5][yatay+5] not in white:
            valid_moves_for_b1.extend(["h8",board[dikey-5][yatay+5]])
    #
    if piece=="b1" and dict_all["b1"]=="d2":
        if board[dikey-1][yatay-1] not in white  :
            valid_moves_for_b1.extend(["c3", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_b1.extend(["b4",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_b1.extend(["a5",board[dikey-3][yatay-3]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_b1.extend(["e3",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_b1.extend(["f4",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_b1.extend(["g5",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white:
            valid_moves_for_b1.extend(["h6",board[dikey-4][yatay+4]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] in ate:
            valid_moves_for_b1.extend(["h6",board[dikey-4][yatay+4]])
    #
    if piece=="b1" and dict_all["b1"]=="e3":
        if board[dikey-1][yatay-1] not in white  :
            valid_moves_for_b1.extend(["d4", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_b1.extend(["c5",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_b1.extend(["b6",board[dikey-3][yatay-3]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_b1.extend(["f4",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_b1.extend(["g5",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_b1.extend(["h6",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white:
            valid_moves_for_b1.extend(["a7",board[dikey-4][yatay-4]])
    ###
    if piece=="b2" and dict_all["b2"]=="f1":
        if board[dikey-1][yatay+1] not in white  :
            valid_moves_for_b2.extend(["g2", board[dikey-1][yatay+1]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_b2.extend(["h3",board[dikey-2][yatay+2]])
        if  board[dikey-1][yatay-1] not in white :
            valid_moves_for_b2.extend(["e2",board[dikey-1][yatay-1]])
        if  board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_b2.extend(["d3",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_b2.extend(["c4",board[dikey-3][yatay-3]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white:
            valid_moves_for_b2.extend(["b5",board[dikey-4][yatay-4]])
        if  board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white and board[dikey-5][yatay-5] not in white:
            valid_moves_for_b2.extend(["a6",board[dikey-5][yatay-5]])
    #   
    if piece=="b2" and dict_all["b2"]=="g2":
        if board[dikey-1][yatay+1] not in white :
            valid_moves_for_b2.extend(["h3", board[dikey-1][yatay+1]])    
        if  board[dikey-1][yatay-1] not in white :
            valid_moves_for_b2.extend(["f3",board[dikey-1][yatay-1]])
        if  board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_b2.extend(["e4",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_b2.extend(["d5",board[dikey-3][yatay-3]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white:
            valid_moves_for_b2.extend(["c6",board[dikey-4][yatay-4]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white and board[dikey-5][yatay-5] not in white:
            valid_moves_for_b2.extend(["b7",board[dikey-5][yatay-5]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white and board[dikey-5][yatay-5] not in white and board[dikey-5][yatay-5] not in black and board[dikey-6][yatay-6] not in white :
            valid_moves_for_b2.extend(["a8",board[dikey-6][yatay-6]])
    #
    if piece=="b2" and dict_all["b2"]=="h3":
        if  board[dikey-1][yatay-1] not in white :
            valid_moves_for_b2.extend(["g4",board[dikey-1][yatay-1]])
        if  board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_b2.extend(["f5",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_b2.extend(["e6",board[dikey-3][yatay-3]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white:
            valid_moves_for_b2.extend(["d7",board[dikey-4][yatay-4]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white and board[dikey-5][yatay-5] not in white and board[dikey-4][yatay-4] not in black:
            valid_moves_for_b2.extend(["c8",board[dikey-5][yatay-5]])
    #
    if piece=="b2" and dict_all["b2"]=="f3":
        if board[dikey-1][yatay+1] not in white  :
            valid_moves_for_b2.extend(["g4", board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_b2.extend(["h5",board[dikey-2][yatay+2]])
        if  board[dikey-1][yatay-1] not in white :
            valid_moves_for_b2.extend(["e4",board[dikey-1][yatay-1]])
        if  board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_b2.extend(["d5",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_b2.extend(["c6",board[dikey-3][yatay-3]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white:
            valid_moves_for_b2.extend(["b7",board[dikey-4][yatay-4]])
        if  board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white and board[dikey-4][yatay-4] not in black and board[dikey-5][yatay-5] not in white:
            valid_moves_for_b2.extend(["a8",board[dikey-5][yatay-5]])
    #
    if piece=="b2" and dict_all["b2"]=="e2":
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_b2.extend(["f3",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_b2.extend(["g4",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_b2.extend(["h5",board[dikey-3][yatay+3]])
        if  board[dikey-1][yatay-1] not in white :
            valid_moves_for_b2.extend(["d3",board[dikey-1][yatay-1]])
        if  board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_b2.extend(["c4",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_b2.extend(["b5",board[dikey-3][yatay-3]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white:
            valid_moves_for_b2.extend(["a6",board[dikey-4][yatay-4]])
    #
    if piece=="b2" and dict_all["b2"]=="d3":
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_b2.extend(["e4",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_b2.extend(["f5",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_b2.extend(["g6",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white:
            valid_moves_for_b2.extend(["h7",board[dikey-4][yatay+4]])
        if  board[dikey-1][yatay-1] not in white :
            valid_moves_for_b2.extend(["c4",board[dikey-1][yatay-1]])
        if  board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_b2.extend(["b5",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_b2.extend(["a6",board[dikey-3][yatay-3]])
    ###
    if piece=="B1" and dict_all["B1"]=="c8":
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_B1.extend(["b7", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_B1.extend(["a6",board[dikey+2][yatay-2]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_B1.extend(["d7",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_B1.extend(["e6",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_B1.extend(["f5",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black:
            valid_moves_for_B1.extend(["g4",board[dikey+4][yatay+4]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black and board[dikey+5][yatay+5] not in black:
            valid_moves_for_B1.extend(["h3",board[dikey+5][yatay+5]])
    #
    if piece=="B1" and dict_all["B1"]=="b7":
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_B1.extend(["a6", board[dikey+1][yatay-1]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_B1.extend(["c6",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_B1.extend(["d5",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_B1.extend(["e4",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black:
            valid_moves_for_B1.extend(["f3",board[dikey+4][yatay+4]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black and board[dikey+5][yatay+5] not in black:
            valid_moves_for_B1.extend(["g2",board[dikey+5][yatay+5]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black and board[dikey+5][yatay+5] not in black and board[dikey+6][yatay+6] not in black and board[dikey+5][yatay+5] not in white:
            valid_moves_for_B1.extend(["h1",board[dikey+6][yatay+6]])
    #
    if piece=="B1" and dict_all["B1"]=="a6":
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_B1.extend(["b5",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_B1.extend(["c4",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_B1.extend(["d3",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black:
            valid_moves_for_B1.extend(["e2",board[dikey+4][yatay+4]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black  and board[dikey+4][yatay+4] not in white and board[dikey+5][yatay+5] not in black:
            valid_moves_for_B1.extend(["f1",board[dikey+5][yatay+5]])
    #
    if piece=="B1" and dict_all["B1"]=="c6":
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_B1.extend(["b5", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_B1.extend(["a4",board[dikey+2][yatay-2]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_B1.extend(["d5",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_B1.extend(["e4",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_B1.extend(["f3",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black:
            valid_moves_for_B1.extend(["g2",board[dikey+4][yatay+4]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black and board[dikey+4][yatay+4] not in white and board[dikey+5][yatay+5] not in black:
            valid_moves_for_B1.extend(["h1",board[dikey+5][yatay+5]])
    #
    if piece=="B1" and dict_all["B1"]=="d7":
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_B1.extend(["c6", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_B1.extend(["b5",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_B1.extend(["a4",board[dikey+3][yatay-3]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_B1.extend(["e6",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_B1.extend(["f5",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_B1.extend(["g4",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black:
            valid_moves_for_B1.extend(["h3",board[dikey+4][yatay+4]])
    #
    if piece=="B1" and dict_all["B1"]=="e6":
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_B1.extend(["d5", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_B1.extend(["c4",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_B1.extend(["b3",board[dikey+3][yatay-3]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_B1.extend(["f5",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_B1.extend(["g4",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_B1.extend(["h3",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black:
            valid_moves_for_B1.extend(["a2",board[dikey+4][yatay-4]])
    
    #
    if piece=="B1" and dict_all["B1"]=="g4":
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_B1.extend(["h3",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_B1.extend(["f3", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay-1] not in combine and board[dikey+2][yatay-2] not in black:
            valid_moves_for_B1.extend(["e2",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in combine and board[dikey+3][yatay-3] not in black:
            valid_moves_for_B1.extend(["1",board[dikey+3][yatay-3]])


    ##
    if piece=="B2" and dict_all["B2"]=="f8":
        if board[dikey+1][yatay+1] not in black  :
            valid_moves_for_B2.extend(["g7", board[dikey+1][yatay+1]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_B2.extend(["h6",board[dikey+2][yatay+2]])
        if  board[dikey+1][yatay-1] not in black :
            valid_moves_for_B2.extend(["e7",board[dikey+1][yatay-1]])
        if  board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_B2.extend(["d6",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_B2.extend(["c5",board[dikey+3][yatay-3]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black:
            valid_moves_for_B2.extend(["b4",board[dikey+4][yatay-4]])
        if  board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black and board[dikey+5][yatay-5] not in black:
            valid_moves_for_B2.extend(["a3",board[dikey+5][yatay-5]])
    #   
    if piece=="B2" and dict_all["B2"]=="g7":
        if board[dikey+1][yatay+1] not in black  :
            valid_moves_for_B2.extend(["h6", board[dikey+1][yatay+1]])    
        if  board[dikey+1][yatay-1] not in black :
            valid_moves_for_B2.extend(["f6",board[dikey+1][yatay-1]])
        if  board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_B2.extend(["e5",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_B2.extend(["d4",board[dikey+3][yatay-3]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black:
            valid_moves_for_B2.extend(["c3",board[dikey+4][yatay-4]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black and board[dikey+5][yatay-5] not in black:
            valid_moves_for_B2.extend(["b2",board[dikey+5][yatay-5]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black and board[dikey+5][yatay-5] not in black and board[dikey+5][yatay-5] not in white and board[dikey+6][yatay-6] not in black :
            valid_moves_for_B2.extend(["a1",board[dikey+6][yatay-6]])
    #
    if piece=="B2" and dict_all["B2"]=="h6":
        if  board[dikey+1][yatay-1] not in black :
            valid_moves_for_B2.extend(["g5",board[dikey+1][yatay-1]])
        if  board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_B2.extend(["f4",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_B2.extend(["e3",board[dikey+3][yatay-3]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black:
            valid_moves_for_B2.extend(["d2",board[dikey+4][yatay-4]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black and board[dikey+5][yatay-5] not in black and board[dikey+4][yatay-4] not in white:
            valid_moves_for_B2.extend(["c1",board[dikey+5][yatay-5]])
    #
    if piece=="B2" and dict_all["B2"]=="f6":
        if board[dikey+1][yatay+1] not in black  :
            valid_moves_for_B2.extend(["g5", board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_B2.extend(["h4",board[dikey+2][yatay+2]])
        if  board[dikey+1][yatay-1] not in black :
            valid_moves_for_B2.extend(["e5",board[dikey+1][yatay-1]])
        if  board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_B2.extend(["d4",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_B2.extend(["c3",board[dikey+3][yatay-3]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black:
            valid_moves_for_B2.extend(["b2",board[dikey+4][yatay-4]])
        if  board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black and board[dikey+4][yatay-4] not in white and board[dikey+5][yatay-5] not in black:
            valid_moves_for_B2.extend(["a1",board[dikey+5][yatay-5]])
    #
    if piece=="B2" and dict_all["B2"]=="e7":
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_B2.extend(["f6",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_B2.extend(["g5",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_B2.extend(["h4",board[dikey+3][yatay+3]])
        if  board[dikey+1][yatay-1] not in black :
            valid_moves_for_B2.extend(["d6",board[dikey+1][yatay-1]])
        if  board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_B2.extend(["c5",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_B2.extend(["b4",board[dikey+3][yatay-3]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black:
            valid_moves_for_B2.extend(["a3",board[dikey+4][yatay-4]])
    #
    if piece=="B2" and dict_all["B2"]=="d6":
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_B2.extend(["e5",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_B2.extend(["f4",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_B2.extend(["g3",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black:
            valid_moves_for_B2.extend(["h2",board[dikey+4][yatay+4]])
        if  board[dikey+1][yatay-1] not in black :
            valid_moves_for_B2.extend(["c5",board[dikey+1][yatay-1]])
        if  board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_B2.extend(["b4",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_B2.extend(["a3",board[dikey+3][yatay-3]])
    ###
    if piece=="n1" and dict_all["n1"]=="b1x":
        if board[dikey-2][yatay-1] not in white:
            valid_moves_for_n1.extend(["a3",board[dikey-2][yatay-1]])
        if board[dikey-2][yatay+1] not in white:
            valid_moves_for_n1.extend(["c3",board[dikey-2][yatay+1]])
        if board[dikey-1][yatay+2] not in white:
            valid_moves_for_n1.extend(["d2",board[dikey-1][yatay+2]])
        if board[dikey-1][yatay-1] not in combine :
            valid_moves_for_n1.extend(["a2",board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_n1.extend(["c2",board[dikey-1][yatay+1]])
    #
    if piece=="n1" and dict_all["n1"]=="a2":
        if board[dikey-2][yatay+1] not in white:
            valid_moves_for_n1.extend(["b4",board[dikey-2][yatay+1]])
        if board[dikey-1][yatay+2] not in white:
            valid_moves_for_n1.extend(["c3",board[dikey-1][yatay+2]])
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_n1.extend(["b3",board[dikey-1][yatay+1]])
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_n1.extend(["b1",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay+2] not in white:
            valid_moves_for_n1.extend(["c1",board[dikey+1][yatay+2]])
    #
    if piece=="n1" and dict_all["n1"]=="c2":
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_n1.extend(["d3",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_n1.extend(["b3",board[dikey-1][yatay-1]])
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_n1.extend(["d1",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_n1.extend(["b1",board[dikey+1][yatay-1]])
        if board[dikey-2][yatay+1] not in white:
            valid_moves_for_n1.extend(["d4",board[dikey-2][yatay+1]])
        if board[dikey-1][yatay+2] not in white:
            valid_moves_for_n1.extend(["e3",board[dikey-1][yatay+2]])
        if board[dikey-2][yatay-1] not in white:
            valid_moves_for_n1.extend(["b4",board[dikey-2][yatay-1]])
        if board[dikey+1][yatay+2] not in white:
            valid_moves_for_n1.extend(["e1",board[dikey+1][yatay+2]])
        if board[dikey-1][yatay-2] not in white:
            valid_moves_for_n1.extend(["a3",board[dikey-1][yatay-2]])
        if board[dikey+1][yatay-2] not in white:
            valid_moves_for_n1.extend(["a1",board[dikey+1][yatay-2]])
    #
    if piece=="n1" and dict_all["n1"]=="a3":
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_n1.extend(["b4",board[dikey-1][yatay+1]])
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_n1.extend(["b2",board[dikey+1][yatay+1]])
        if board[dikey-2][yatay+1] not in white:
            valid_moves_for_n1.extend(["b5",board[dikey-2][yatay+1]])
        if board[dikey+2][yatay+1] not in white:
            valid_moves_for_n1.extend(["b1",board[dikey+2][yatay+1]])
        if board[dikey-1][yatay+2] not in white:
            valid_moves_for_n1.extend(["c4",board[dikey-1][yatay+2]])
        if board[dikey+1][yatay+2] not in white:
            valid_moves_for_n1.extend(["c2",board[dikey+1][yatay+2]])
    #
    if piece=="n1" and dict_all["n1"]=="c3":
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_n1.extend(["d4",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_n1.extend(["b4",board[dikey-1][yatay-1]])
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_n1.extend(["d2",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_n1.extend(["b2",board[dikey+1][yatay-1]])
        if board[dikey-2][yatay+1] not in white:
            valid_moves_for_n1.extend(["d5",board[dikey-2][yatay+1]])
        if board[dikey-1][yatay+2] not in white:
            valid_moves_for_n1.extend(["e4",board[dikey-1][yatay+2]])
        if board[dikey-2][yatay-1] not in white:
            valid_moves_for_n1.extend(["b5",board[dikey-2][yatay-1]])
        if board[dikey+1][yatay+2] not in white:
            valid_moves_for_n1.extend(["e2",board[dikey+1][yatay+2]])
        if board[dikey-1][yatay-2] not in white:
            valid_moves_for_n1.extend(["a4",board[dikey-1][yatay-2]])
        if board[dikey+1][yatay-2] not in white:
            valid_moves_for_n1.extend(["a2",board[dikey+1][yatay-2]])
        if board[dikey+2][yatay+1] not in white:
            valid_moves_for_n1.extend(["d1",board[dikey+2][yatay+1]])
        if board[dikey+2][yatay-1] not in white:
            valid_moves_for_n1.extend(["b1",board[dikey+2][yatay-1]])
    #
    if piece=="n1" and dict_all["n1"]=="d2":
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_n1.extend(["e3",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_n1.extend(["c3",board[dikey-1][yatay-1]])
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_n1.extend(["e1",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_n1.extend(["c1",board[dikey+1][yatay-1]])
        if board[dikey-2][yatay+1] not in white:
            valid_moves_for_n1.extend(["e4",board[dikey-2][yatay+1]])
        if board[dikey-1][yatay+2] not in white:
            valid_moves_for_n1.extend(["f3",board[dikey-1][yatay+2]])
        if board[dikey-2][yatay-1] not in white:
            valid_moves_for_n1.extend(["c4",board[dikey-2][yatay-1]])
        if board[dikey+1][yatay+2] not in white:
            valid_moves_for_n1.extend(["f1",board[dikey+1][yatay+2]])
        if board[dikey-1][yatay-2] not in white:
            valid_moves_for_n1.extend(["b3",board[dikey-1][yatay-2]])
        if board[dikey+1][yatay-2] not in white:
            valid_moves_for_n1.extend(["b1",board[dikey+1][yatay-2]])
    ###
    if piece=="n2" and dict_all["n2"]=="g1":
        if board[dikey-2][yatay-1] not in white:
            valid_moves_for_n2.extend(["f3",board[dikey-2][yatay-1]])
        if board[dikey-2][yatay+1] not in white:
            valid_moves_for_n2.extend(["h3",board[dikey-2][yatay+1]])
        if board[dikey-1][yatay-2] not in white:
            valid_moves_for_n2.extend(["e2",board[dikey-1][yatay-2]])
        if board[dikey-1][yatay-1] not in combine :
            valid_moves_for_n2.extend(["f2",board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_n2.extend(["h2",board[dikey-1][yatay+1]])
    #
    if piece=="n2" and dict_all["n2"]=="h2":
        if board[dikey-2][yatay-1] not in white:
            valid_moves_for_n2.extend(["g4",board[dikey-2][yatay-1]])
        if board[dikey-1][yatay-2] not in white:
            valid_moves_for_n2.extend(["f3",board[dikey-1][yatay-2]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_n2.extend(["g3",board[dikey-1][yatay-1]])
        if board[dikey+1][yatay-1] not in combine :
            valid_moves_for_n2.extend(["g1",board[dikey+1][yatay-1]])
        if board[dikey+1][yatay-2] not in white:
            valid_moves_for_n2.extend(["f1",board[dikey+1][yatay-2]])
    #
    if piece=="n2" and dict_all["n2"]=="f2":
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_n2.extend(["g3",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_n2.extend(["e3",board[dikey-1][yatay-1]])
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_n2.extend(["g1",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_n2.extend(["e1",board[dikey+1][yatay-1]])
        if board[dikey-2][yatay+1] not in white:
            valid_moves_for_n2.extend(["g4",board[dikey-2][yatay+1]])
        if board[dikey-1][yatay+2] not in white:
            valid_moves_for_n2.extend(["h3",board[dikey-1][yatay+2]])
        if board[dikey-2][yatay-1] not in white:
            valid_moves_for_n2.extend(["e4",board[dikey-2][yatay-1]])
        if board[dikey+1][yatay+2] not in white:
            valid_moves_for_n2.extend(["h1",board[dikey+1][yatay+2]])
        if board[dikey-1][yatay-2] not in white:
            valid_moves_for_n2.extend(["d3",board[dikey-1][yatay-2]])
        if board[dikey+1][yatay-2] not in white:
            valid_moves_for_n2.extend(["d1",board[dikey+1][yatay-2]])
    #
    if piece=="n2" and dict_all["n2"]=="h3":
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_n2.extend(["g4",board[dikey-1][yatay-1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_n2.extend(["g2",board[dikey+1][yatay-1]])
        if board[dikey-2][yatay-1] not in white:
            valid_moves_for_n2.extend(["g5",board[dikey-2][yatay-1]])
        if board[dikey+2][yatay-1] not in white:
            valid_moves_for_n2.extend(["g1",board[dikey+2][yatay-1]])
        if board[dikey-1][yatay-2] not in white:
            valid_moves_for_n2.extend(["f4",board[dikey-1][yatay-2]])
        if board[dikey+1][yatay-2] not in white:
            valid_moves_for_n2.extend(["f2",board[dikey+1][yatay-2]])
    #
    if piece=="n2" and dict_all["n2"]=="f3":
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_n2.extend(["g4",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_n2.extend(["e4",board[dikey-1][yatay-1]])
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_n2.extend(["g2",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_n2.extend(["e2",board[dikey+1][yatay-1]])
        if board[dikey-2][yatay+1] not in white:
            valid_moves_for_n2.extend(["g5",board[dikey-2][yatay+1]])
        if board[dikey-1][yatay+2] not in white:
            valid_moves_for_n2.extend(["h4",board[dikey-1][yatay+2]])
        if board[dikey-2][yatay-1] not in white:
            valid_moves_for_n2.extend(["e5",board[dikey-2][yatay-1]])
        if board[dikey+1][yatay+2] not in white:
            valid_moves_for_n2.extend(["h2",board[dikey+1][yatay+2]])
        if board[dikey-1][yatay-2] not in white:
            valid_moves_for_n2.extend(["d4",board[dikey-1][yatay-2]])
        if board[dikey+1][yatay-2] not in white:
            valid_moves_for_n2.extend(["d2",board[dikey+1][yatay-2]])
        if board[dikey+2][yatay+1] not in white:
            valid_moves_for_n2.extend(["g1",board[dikey+2][yatay+1]])
        if board[dikey+2][yatay-1] not in white:
            valid_moves_for_n2.extend(["e1",board[dikey+2][yatay-1]])
    #
    if piece=="n2" and dict_all["n2"]=="e2":
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_n2.extend(["f3",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_n2.extend(["d3",board[dikey-1][yatay-1]])
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_n2.extend(["f1",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_n2.extend(["d1",board[dikey+1][yatay-1]])
        if board[dikey-2][yatay+1] not in white:
            valid_moves_for_n2.extend(["f4",board[dikey-2][yatay+1]])
        if board[dikey-1][yatay+2] not in white:
            valid_moves_for_n2.extend(["g3",board[dikey-1][yatay+2]])
        if board[dikey-2][yatay-1] not in white:
            valid_moves_for_n2.extend(["d4",board[dikey-2][yatay-1]])
        if board[dikey+1][yatay+2] not in white:
            valid_moves_for_n2.extend(["g1",board[dikey+1][yatay+2]])
        if board[dikey-1][yatay-2] not in white:
            valid_moves_for_n2.extend(["c3",board[dikey-1][yatay-2]])
        if board[dikey+1][yatay-2] not in white:
            valid_moves_for_n2.extend(["c1",board[dikey+1][yatay-2]])
    ###
    if piece=="N1" and dict_all["N1"]=="b8":
        if board[dikey+2][yatay-1] not in black:
            valid_moves_for_N1.extend(["a6",board[dikey+2][yatay-1]])
        if board[dikey+2][yatay+1] not in black:
            valid_moves_for_N1.extend(["c6",board[dikey+2][yatay+1]])
        if board[dikey+1][yatay+2] not in black:
            valid_moves_for_N1.extend(["d7",board[dikey+1][yatay+2]])
        if board[dikey+1][yatay-1] not in combine :
            valid_moves_for_N1.extend(["a7",board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_N1.extend(["c7",board[dikey+1][yatay+1]])
    #
    if piece=="N1" and dict_all["N1"]=="a7":
        if board[dikey+2][yatay+1] not in black:
            valid_moves_for_N1.extend(["b5",board[dikey+2][yatay+1]])
        if board[dikey+1][yatay+2] not in black:
            valid_moves_for_N1.extend(["c6",board[dikey+1][yatay+2]])
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_N1.extend(["b6",board[dikey+1][yatay+1]])
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_N1.extend(["b8",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay+2] not in black:
            valid_moves_for_N1.extend(["c8",board[dikey-1][yatay+2]])
    #
    if piece=="N1" and dict_all["N1"]=="c7":
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_N1.extend(["d6",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_N1.extend(["b6",board[dikey+1][yatay-1]])
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_N1.extend(["d8",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_N1.extend(["b8",board[dikey-1][yatay-1]])
        if board[dikey+2][yatay+1] not in black:
            valid_moves_for_N1.extend(["d5",board[dikey+2][yatay+1]])
        if board[dikey+1][yatay+2] not in black:
            valid_moves_for_N1.extend(["e6",board[dikey+1][yatay+2]])
        if board[dikey+2][yatay-1] not in black:
            valid_moves_for_N1.extend(["b5",board[dikey+2][yatay-1]])
        if board[dikey-1][yatay+2] not in black:
            valid_moves_for_N1.extend(["e8",board[dikey-1][yatay+2]])
        if board[dikey+1][yatay-2] not in black:
            valid_moves_for_N1.extend(["a6",board[dikey-1][yatay-2]])
        if board[dikey-1][yatay-2] not in black:
            valid_moves_for_N1.extend(["a8",board[dikey-1][yatay-2]])
    #
    if piece=="N1" and dict_all["N1"]=="a6":
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_N1.extend(["b5",board[dikey+1][yatay+1]])
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_N1.extend(["b7",board[dikey-1][yatay+1]])
        if board[dikey+2][yatay+1] not in black:
            valid_moves_for_N1.extend(["b4",board[dikey+2][yatay+1]])
        if board[dikey-2][yatay+1] not in black:
            valid_moves_for_N1.extend(["b8",board[dikey-2][yatay+1]])
        if board[dikey+1][yatay+2] not in black:
            valid_moves_for_N1.extend(["c5",board[dikey+1][yatay+2]])
        if board[dikey-1][yatay+2] not in black:
            valid_moves_for_N1.extend(["c7",board[dikey-1][yatay+2]])
    #
    if piece=="N1" and dict_all["N1"]=="c6":
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_N1.extend(["d5",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_N1.extend(["b5",board[dikey+1][yatay-1]])
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_N1.extend(["d7",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_N1.extend(["b7",board[dikey-1][yatay-1]])
        if board[dikey+2][yatay+1] not in black:
            valid_moves_for_N1.extend(["d4",board[dikey+2][yatay+1]])
        if board[dikey+1][yatay+2] not in black:
            valid_moves_for_N1.extend(["e5",board[dikey+1][yatay+2]])
        if board[dikey+2][yatay-1] not in black:
            valid_moves_for_N1.extend(["b4",board[dikey+2][yatay-1]])
        if board[dikey-1][yatay+2] not in black:
            valid_moves_for_N1.extend(["e7",board[dikey-1][yatay+2]])
        if board[dikey+1][yatay-2] not in black:
            valid_moves_for_N1.extend(["a5",board[dikey+1][yatay-2]])
        if board[dikey-1][yatay-2] not in black:
            valid_moves_for_N1.extend(["a7",board[dikey-1][yatay-2]])
        if board[dikey-2][yatay+1] not in black:
            valid_moves_for_N1.extend(["d8",board[dikey-2][yatay+1]])
        if board[dikey-2][yatay-1] not in black:
            valid_moves_for_N1.extend(["b8",board[dikey-2][yatay-1]])
    #
    if piece=="N1" and dict_all["N1"]=="d7":
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_N1.extend(["e6",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_N1.extend(["c6",board[dikey+1][yatay-1]])
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_N1.extend(["e8",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_N1.extend(["c8",board[dikey-1][yatay-1]])
        if board[dikey+2][yatay+1] not in black:
            valid_moves_for_N1.extend(["e5",board[dikey+2][yatay+1]])
        if board[dikey+1][yatay+2] not in black:
            valid_moves_for_N1.extend(["f6",board[dikey+1][yatay+2]])
        if board[dikey+2][yatay-1] not in black:
            valid_moves_for_N1.extend(["c5",board[dikey+2][yatay-1]])
        if board[dikey-1][yatay+2] not in black:
            valid_moves_for_N1.extend(["f8",board[dikey-1][yatay+2]])
        if board[dikey+1][yatay-2] not in black:
            valid_moves_for_N1.extend(["b6",board[dikey+1][yatay-2]])
        if board[dikey-1][yatay-2] not in black:
            valid_moves_for_N1.extend(["b8",board[dikey-1][yatay-2]])
    #ex
    if piece=="N1" and dict_all["N1"]=="c5":
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_N1.extend(["d4",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_N1.extend(["b4",board[dikey+1][yatay-1]])
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_N1.extend(["d6",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_N1.extend(["b6",board[dikey-1][yatay-1]])
        if board[dikey+2][yatay+1] not in black:
            valid_moves_for_N1.extend(["d3",board[dikey+2][yatay+1]])
        if board[dikey+1][yatay+2] not in black:
            valid_moves_for_N1.extend(["e4",board[dikey+1][yatay+2]])
        if board[dikey+2][yatay-1] not in black:
            valid_moves_for_N1.extend(["b3",board[dikey+2][yatay-1]])
        if board[dikey-1][yatay+2] not in black:
            valid_moves_for_N1.extend(["e6",board[dikey-1][yatay+2]])
        if board[dikey+1][yatay-2] not in black:
            valid_moves_for_N1.extend(["a4",board[dikey+1][yatay-2]])
        if board[dikey-1][yatay-2] not in black:
            valid_moves_for_N1.extend(["a6",board[dikey-1][yatay-2]])
        if board[dikey-2][yatay+1] not in black:
            valid_moves_for_N1.extend(["d7",board[dikey-2][yatay+1]])
        if board[dikey-2][yatay-1] not in black:
            valid_moves_for_N1.extend(["b7",board[dikey-2][yatay-1]])
    ###
    
    if piece=="N2" and dict_all["N2"]=="g8":
        if board[dikey+2][yatay-1] not in black:
            valid_moves_for_N2.extend(["f6",board[dikey+2][yatay-1]])
        if board[dikey+2][yatay+1] not in black:
            valid_moves_for_N2.extend(["h6",board[dikey+2][yatay+1]])
        if board[dikey+2][yatay-2] not in black:
            valid_moves_for_N2.extend(["e7",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in combine :
            valid_moves_for_N2.extend(["f7",board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_N2.extend(["h7",board[dikey+1][yatay+1]])
    #
    if piece=="N2" and dict_all["N2"]=="h7":
        if board[dikey+2][yatay-1] not in black:
            valid_moves_for_N2.extend(["g5",board[dikey+2][yatay-1]])
        if board[dikey+2][yatay-2] not in black:
            valid_moves_for_N2.extend(["f6",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_N2.extend(["g6",board[dikey+1][yatay-1]])
        if board[dikey-1][yatay-1] not in combine :
            valid_moves_for_N2.extend(["g8",board[dikey-1][yatay-1]])
        if board[dikey-1][yatay-2] not in black:
            valid_moves_for_N2.extend(["f8",board[dikey-1][yatay-2]])
    #
    if piece=="N2" and dict_all["N2"]=="f7":
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_N2.extend(["g6",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_N2.extend(["e6",board[dikey+1][yatay-1]])
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_N2.extend(["g8",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_N2.extend(["e8",board[dikey-1][yatay-1]])
        if board[dikey+2][yatay+1] not in black:
            valid_moves_for_N2.extend(["g5",board[dikey+2][yatay+1]])
        if board[dikey+2][yatay+2] not in black:
            valid_moves_for_N2.extend(["h6",board[dikey+2][yatay+2]])
        if board[dikey+2][yatay-1] not in black:
            valid_moves_for_N2.extend(["e5",board[dikey+2][yatay-1]])
        if board[dikey-1][yatay+2] not in black:
            valid_moves_for_N2.extend(["h8",board[dikey-1][yatay+2]])
        if board[dikey+2][yatay-2] not in black:
            valid_moves_for_N2.extend(["d6",board[dikey+2][yatay-2]])
        if board[dikey-1][yatay-2] not in black:
            valid_moves_for_N2.extend(["d8",board[dikey-1][yatay-2]])
    #
    if piece=="N2" and dict_all["N2"]=="h6":
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_N2.extend(["g5",board[dikey+1][yatay-1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_N2.extend(["g7",board[dikey-1][yatay-1]])
        if board[dikey+2][yatay-1] not in black:
            valid_moves_for_N2.extend(["g4",board[dikey+2][yatay-1]])
        if board[dikey-2][yatay-1] not in black:
            valid_moves_for_N2.extend(["g8",board[dikey-2][yatay-1]])
        if board[dikey+2][yatay-2] not in black:
            valid_moves_for_N2.extend(["f5",board[dikey+2][yatay-2]])
        if board[dikey-1][yatay-2] not in black:
            valid_moves_for_N2.extend(["f7",board[dikey-1][yatay-2]])
    #
    if piece=="N2" and dict_all["N2"]=="f6":
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_N2.extend(["g5",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_N2.extend(["e5",board[dikey+1][yatay-1]])
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_N2.extend(["g7",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_N2.extend(["e7",board[dikey-1][yatay-1]])
        if board[dikey+2][yatay+1] not in black:
            valid_moves_for_N2.extend(["g4",board[dikey+2][yatay+1]])
        if board[dikey+2][yatay+2] not in black:
            valid_moves_for_N2.extend(["h5",board[dikey+2][yatay+2]])
        if board[dikey+2][yatay-1] not in black:
            valid_moves_for_N2.extend(["e4",board[dikey+2][yatay-1]])
        if board[dikey-1][yatay+2] not in black:
            valid_moves_for_N2.extend(["h7",board[dikey-1][yatay+2]])
        if board[dikey+2][yatay-2] not in black:
            valid_moves_for_N2.extend(["d5",board[dikey+2][yatay-2]])
        if board[dikey-1][yatay-2] not in black:
            valid_moves_for_N2.extend(["d7",board[dikey-1][yatay-2]])
        if board[dikey-2][yatay+1] not in black:
            valid_moves_for_N2.extend(["g8",board[dikey-2][yatay+1]])
        if board[dikey-2][yatay-1] not in black:
            valid_moves_for_N2.extend(["e8",board[dikey-2][yatay-1]])
    #
    if piece=="N2" and dict_all["N2"]=="e7":
        if board[dikey+1][yatay+1] not in combine:
            valid_moves_for_N2.extend(["f6",board[dikey+1][yatay+1]])
        if board[dikey+1][yatay-1] not in combine:
            valid_moves_for_N2.extend(["d6",board[dikey+1][yatay-1]])
        if board[dikey-1][yatay+1] not in combine:
            valid_moves_for_N2.extend(["f8",board[dikey-1][yatay+1]])
        if board[dikey-1][yatay-1] not in combine:
            valid_moves_for_N2.extend(["d8",board[dikey-1][yatay-1]])
        if board[dikey+2][yatay+1] not in black:
            valid_moves_for_N2.extend(["f5",board[dikey+2][yatay+1]])
        if board[dikey+2][yatay+2] not in black:
            valid_moves_for_N2.extend(["g6",board[dikey+2][yatay+2]])
        if board[dikey+2][yatay-1] not in black:
            valid_moves_for_N2.extend(["d5",board[dikey+2][yatay-1]])
        if board[dikey-1][yatay+2] not in black:
            valid_moves_for_N2.extend(["g8",board[dikey-1][yatay+2]])
        if board[dikey+2][yatay-2] not in black:
            valid_moves_for_N2.extend(["c6",board[dikey+2][yatay-2]])
        if board[dikey-1][yatay-2] not in black:
            valid_moves_for_N2.extend(["c8",board[dikey-1][yatay-2]])
    ###
    
    if piece=="r1" and dict_all["r1"]=="a1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r1.extend(["a2",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_r1.extend(["a3",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_r1.extend(["a4",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_r1.extend(["a5",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in white:
            valid_moves_for_r1.extend(["a6",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_r1.extend(["a7",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in combine and board[dikey-7][yatay] not in white:
            valid_moves_for_r1.extend(["a8",board[dikey-7][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_r1.extend(["b1",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_r1.extend(["c1",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_r1.extend(["d1",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_r1.extend(["e1",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in white:
            valid_moves_for_r1.extend(["f1",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in white:
            valid_moves_for_r1.extend(["g1",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in white:
            valid_moves_for_r1.extend(["h1",board[dikey][yatay+7]])
        
    if piece=="r1" and dict_all["r1"]=="a2":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r1.extend(["a3",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_r1.extend(["a4",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_r1.extend(["a5",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_r1.extend(["a6",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in combine and board[dikey-5][yatay] not in white:
            valid_moves_for_r1.extend(["a7",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_r1.extend(["a8",board[dikey-6][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_r1.extend(["a1",board[dikey+1][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_r1.extend(["b2",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_r1.extend(["c2",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_r1.extend(["d2",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_r1.extend(["e2",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in white:
            valid_moves_for_r1.extend(["f2",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in white:
            valid_moves_for_r1.extend(["g2",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in white:
            valid_moves_for_r1.extend(["h2",board[dikey][yatay+7]])
        
    if piece=="r1" and dict_all["r1"]=="a3":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r1.extend(["a4",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_r1.extend(["a5",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_r1.extend(["a6",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in combine and board[dikey-4][yatay] not in white:
            valid_moves_for_r1.extend(["a7",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in combine and board[dikey-5][yatay] not in white:
            valid_moves_for_r1.extend(["a8",board[dikey-5][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white:
            valid_moves_for_r1.extend(["a1",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_r1.extend(["a2",board[dikey+1][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_r1.extend(["b3",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_r1.extend(["c3",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_r1.extend(["d3",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_r1.extend(["e3",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in white:
            valid_moves_for_r1.extend(["f3",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in white:
            valid_moves_for_r1.extend(["g3",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in white:
            valid_moves_for_r1.extend(["h3",board[dikey][yatay+7]])
    
    if piece=="r1" and dict_all["r1"]=="a4":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r1.extend(["a5",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_r1.extend(["a6",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in combine and board[dikey-3][yatay] not in white:
            valid_moves_for_r1.extend(["a7",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in combine and board[dikey-4][yatay] not in white:
            valid_moves_for_r1.extend(["a8",board[dikey-4][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay] not in white:
            valid_moves_for_r1.extend(["a1",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white:
            valid_moves_for_r1.extend(["a2",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_r1.extend(["a3",board[dikey+1][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_r1.extend(["b4",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_r1.extend(["c4",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_r1.extend(["d4",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_r1.extend(["e4",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in white:
            valid_moves_for_r1.extend(["f4",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in white:
            valid_moves_for_r1.extend(["g4",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in white:
            valid_moves_for_r1.extend(["h4",board[dikey][yatay+7]])
    
    if piece=="r1" and dict_all["r1"]=="a5":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r1.extend(["a6",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in combine and board[dikey-2][yatay] not in white:
            valid_moves_for_r1.extend(["a7",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in combine and board[dikey-3][yatay] not in white:
            valid_moves_for_r1.extend(["a8",board[dikey-3][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay]  not in white and board[dikey+4][yatay] not in white:
            valid_moves_for_r1.extend(["a1",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay] not in white:
            valid_moves_for_r1.extend(["a2",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white:
            valid_moves_for_r1.extend(["a3",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_r1.extend(["a4",board[dikey+1][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_r1.extend(["b5",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_r1.extend(["c5",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_r1.extend(["d5",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_r1.extend(["e5",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in white:
            valid_moves_for_r1.extend(["f5",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in white:
            valid_moves_for_r1.extend(["g5",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in white:
            valid_moves_for_r1.extend(["h5",board[dikey][yatay+7]])
        
    if piece=="r1" and dict_all["r1"]=="a6":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r1.extend(["a7",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in combine and board[dikey-2][yatay] not in white:
            valid_moves_for_r1.extend(["a8",board[dikey-2][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay]  not in white and board[dikey+4][yatay] not in white and board[dikey+5][yatay] not in white:
            valid_moves_for_r1.extend(["a1",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay]  not in white and board[dikey+4][yatay] not in white:
            valid_moves_for_r1.extend(["a2",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay] not in white:
            valid_moves_for_r1.extend(["a3",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white:
            valid_moves_for_r1.extend(["a4",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_r1.extend(["a5",board[dikey+1][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_r1.extend(["b6",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_r1.extend(["c6",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_r1.extend(["d6",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_r1.extend(["e6",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in white:
            valid_moves_for_r1.extend(["f6",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in white:
            valid_moves_for_r1.extend(["g6",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in white:
            valid_moves_for_r1.extend(["h6",board[dikey][yatay+7]])
        
    if piece=="r1" and dict_all["r1"]=="a7":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r1.extend(["a8",board[dikey-1][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay]  not in white and board[dikey+4][yatay] not in white and board[dikey+5][yatay] not in white and board[dikey+6][yatay] not in white:
            valid_moves_for_r1.extend(["a1",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay]  not in white and board[dikey+4][yatay] not in white and board[dikey+5][yatay] not in white:
            valid_moves_for_r1.extend(["a2",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay]  not in white and board[dikey+4][yatay] not in white:
            valid_moves_for_r1.extend(["a3",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay] not in white:
            valid_moves_for_r1.extend(["a4",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white:
            valid_moves_for_r1.extend(["a5",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_r1.extend(["a6",board[dikey+1][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_r1.extend(["b7",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_r1.extend(["c7",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_r1.extend(["d7",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_r1.extend(["e7",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in white:
            valid_moves_for_r1.extend(["f7",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in white:
            valid_moves_for_r1.extend(["g7",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in white:
            valid_moves_for_r1.extend(["h7",board[dikey][yatay+7]])

    if piece=="r1" and dict_all["r1"]=="b1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r1.extend(["b2",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_r1.extend(["b3",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_r1.extend(["b4",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_r1.extend(["b5",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in white:
            valid_moves_for_r1.extend(["b6",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_r1.extend(["b7",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in combine and board[dikey-7][yatay] not in white:
            valid_moves_for_r1.extend(["b8",board[dikey-7][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_r1.extend(["c1",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_r1.extend(["d1",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_r1.extend(["e1",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_r1.extend(["f1",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in white:
            valid_moves_for_r1.extend(["g1",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in white:
            valid_moves_for_r1.extend(["h1",board[dikey][yatay+6]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_r1.extend(["a1",board[dikey][yatay-1]])
    
    if piece=="r1" and dict_all["r1"]=="c1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r1.extend(["c2",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_r1.extend(["c3",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_r1.extend(["c4",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_r1.extend(["c5",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in white:
            valid_moves_for_r1.extend(["c6",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_r1.extend(["c7",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in combine and board[dikey-7][yatay] not in white:
            valid_moves_for_r1.extend(["c8",board[dikey-7][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_r1.extend(["d1",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_r1.extend(["e1",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_r1.extend(["f1",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_r1.extend(["g1",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in white:
            valid_moves_for_r1.extend(["h1",board[dikey][yatay+5]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_r1.extend(["a1",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_r1.extend(["b1",board[dikey][yatay-1]])
    
    if piece=="r1" and dict_all["r1"]=="d1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r1.extend(["d2",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_r1.extend(["d3",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_r1.extend(["d4",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_r1.extend(["d5",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in white:
            valid_moves_for_r1.extend(["d6",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_r1.extend(["d7",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in combine and board[dikey-7][yatay] not in white:
            valid_moves_for_r1.extend(["d8",board[dikey-7][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_r1.extend(["e1",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_r1.extend(["f1",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_r1.extend(["g1",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_r1.extend(["h1",board[dikey][yatay+4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_r1.extend(["a1",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_r1.extend(["b1",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_r1.extend(["c1",board[dikey][yatay-1]])
    ###

    if piece=="r2" and dict_all["r2"]=="h1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r2.extend(["h2",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_r2.extend(["h3",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_r2.extend(["h4",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_r2.extend(["h5",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in white:
            valid_moves_for_r2.extend(["h6",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_r2.extend(["h7",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in combine and board[dikey-7][yatay] not in white:
            valid_moves_for_r2.extend(["h8",board[dikey-7][yatay]])   
        if board[dikey][yatay-1] not in white:
            valid_moves_for_r2.extend(["g1",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_r2.extend(["f1",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_r2.extend(["e1",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white:
            valid_moves_for_r2.extend(["d1",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in white:
            valid_moves_for_r2.extend(["c1",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in white:
            valid_moves_for_r2.extend(["b1",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in white:
            valid_moves_for_r2.extend(["a1",board[dikey][yatay-7]])
    
    if piece=="r2" and dict_all["r2"]=="h2":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r2.extend(["h3",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_r2.extend(["h4",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_r2.extend(["h5",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_r2.extend(["h6",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in combine and board[dikey-5][yatay] not in white:
            valid_moves_for_r2.extend(["h7",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_r2.extend(["h8",board[dikey-6][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_r2.extend(["h1",board[dikey+1][yatay]])    
        if board[dikey][yatay-1] not in white:
            valid_moves_for_r2.extend(["g2",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_r2.extend(["f2",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_r2.extend(["e2",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white:
            valid_moves_for_r2.extend(["d2",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in white:
            valid_moves_for_r2.extend(["c2",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in white:
            valid_moves_for_r2.extend(["b2",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in white:
            valid_moves_for_r2.extend(["a2",board[dikey][yatay-7]])
    
    if piece=="r2" and dict_all["r2"]=="h3":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r2.extend(["h4",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_r2.extend(["h5",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_r2.extend(["h6",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in combine and board[dikey-4][yatay] not in white:
            valid_moves_for_r2.extend(["h7",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in combine and board[dikey-5][yatay] not in white:
            valid_moves_for_r2.extend(["h8",board[dikey-5][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white:
            valid_moves_for_r2.extend(["h1",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_r2.extend(["h2",board[dikey+1][yatay]])    
        if board[dikey][yatay-1] not in white:
            valid_moves_for_r2.extend(["g3",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_r2.extend(["f3",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_r2.extend(["e3",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white:
            valid_moves_for_r2.extend(["d3",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in white:
            valid_moves_for_r2.extend(["c3",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in white:
            valid_moves_for_r2.extend(["b3",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in white:
            valid_moves_for_r2.extend(["a3",board[dikey][yatay-7]])
    
    if piece=="r2" and dict_all["r2"]=="h4":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r2.extend(["h5",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_r2.extend(["h6",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in combine and board[dikey-3][yatay] not in white:
            valid_moves_for_r2.extend(["h7",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in combine and board[dikey-4][yatay] not in white:
            valid_moves_for_r2.extend(["h8",board[dikey-4][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay] not in white:
            valid_moves_for_r2.extend(["h1",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white:
            valid_moves_for_r2.extend(["h2",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_r2.extend(["h3",board[dikey+1][yatay]])    
        if board[dikey][yatay-1] not in white:
            valid_moves_for_r2.extend(["g4",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_r2.extend(["f4",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_r2.extend(["e4",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white:
            valid_moves_for_r2.extend(["d4",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in white:
            valid_moves_for_r2.extend(["c4",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in white:
            valid_moves_for_r2.extend(["b4",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in white:
            valid_moves_for_r2.extend(["a4",board[dikey][yatay-7]])
        
    if piece=="r2" and dict_all["r2"]=="h5":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r2.extend(["h6",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in combine and board[dikey-2][yatay] not in white:
            valid_moves_for_r2.extend(["h7",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in combine and board[dikey-3][yatay] not in white:
            valid_moves_for_r2.extend(["h8",board[dikey-3][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay]  not in white and board[dikey+4][yatay] not in white:
            valid_moves_for_r2.extend(["h1",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay] not in white:
            valid_moves_for_r2.extend(["h2",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white:
            valid_moves_for_r2.extend(["h3",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_r2.extend(["h4",board[dikey+1][yatay]])    
        if board[dikey][yatay-1] not in white:
            valid_moves_for_r2.extend(["g5",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_r2.extend(["f5",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_r2.extend(["e5",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white:
            valid_moves_for_r2.extend(["d5",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in white:
            valid_moves_for_r2.extend(["c5",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in white:
            valid_moves_for_r2.extend(["b5",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in white:
            valid_moves_for_r2.extend(["a5",board[dikey][yatay-7]])
    
    if piece=="r2" and dict_all["r2"]=="h6":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r2.extend(["h7",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in combine and board[dikey-2][yatay] not in white:
            valid_moves_for_r2.extend(["h8",board[dikey-2][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay]  not in white and board[dikey+4][yatay] not in white and board[dikey+5][yatay] not in white:
            valid_moves_for_r2.extend(["h1",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay]  not in white and board[dikey+4][yatay] not in white:
            valid_moves_for_r2.extend(["h2",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay] not in white:
            valid_moves_for_r2.extend(["h3",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white:
            valid_moves_for_r2.extend(["h4",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_r2.extend(["h5",board[dikey+1][yatay]])    
        if board[dikey][yatay-1] not in white:
            valid_moves_for_r2.extend(["g6",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_r2.extend(["f6",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_r2.extend(["e6",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white:
            valid_moves_for_r2.extend(["d6",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in white:
            valid_moves_for_r2.extend(["c6",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in white:
            valid_moves_for_r2.extend(["b6",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in white:
            valid_moves_for_r2.extend(["a6",board[dikey][yatay-7]])
    



    if piece=="r2" and dict_all["r2"]=="h7":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r2.extend(["h8",board[dikey-1][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay]  not in white and board[dikey+4][yatay] not in white and board[dikey+5][yatay] not in white and board[dikey+6][yatay] not in white:
            valid_moves_for_r2.extend(["h1",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay]  not in white and board[dikey+4][yatay] not in white and board[dikey+5][yatay] not in white:
            valid_moves_for_r2.extend(["h2",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay]  not in white and board[dikey+4][yatay] not in white:
            valid_moves_for_r2.extend(["h3",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay] not in white:
            valid_moves_for_r2.extend(["h4",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white:
            valid_moves_for_r2.extend(["h5",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_r2.extend(["h6",board[dikey+1][yatay]])    
        if board[dikey][yatay-1] not in white:
            valid_moves_for_r2.extend(["g7",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_r2.extend(["f7",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_r2.extend(["e7",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white:
            valid_moves_for_r2.extend(["d7",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in white:
            valid_moves_for_r2.extend(["c7",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in white:
            valid_moves_for_r2.extend(["b7",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in white:
            valid_moves_for_r2.extend(["a7",board[dikey][yatay-7]])
    
    if piece=="r2" and dict_all["r2"]=="g1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r2.extend(["g2",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_r2.extend(["g3",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_r2.extend(["g4",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_r2.extend(["g5",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in white:
            valid_moves_for_r2.extend(["g6",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_r2.extend(["g7",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in combine and board[dikey-7][yatay] not in white:
            valid_moves_for_r2.extend(["g8",board[dikey-7][yatay]])   
        if board[dikey][yatay-1] not in white:
            valid_moves_for_r2.extend(["f1",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_r2.extend(["e1",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_r2.extend(["d1",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white:
            valid_moves_for_r2.extend(["c1",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in white:
            valid_moves_for_r2.extend(["b1",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in white:
            valid_moves_for_r2.extend(["a1",board[dikey][yatay-6]])
        if board[dikey][yatay+1] not in white:
            valid_moves_for_r2.extend(["h1",board[dikey][yatay+1]])
    
    if piece=="r2" and dict_all["r2"]=="f1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_r2.extend(["f2",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_r2.extend(["f3",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_r2.extend(["f4",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_r2.extend(["f5",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in white:
            valid_moves_for_r2.extend(["f6",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_r2.extend(["f7",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in combine and board[dikey-7][yatay] not in white:
            valid_moves_for_r2.extend(["f8",board[dikey-7][yatay]])   
        if board[dikey][yatay-1] not in white:
            valid_moves_for_r2.extend(["e1",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_r2.extend(["d1",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_r2.extend(["c1",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white:
            valid_moves_for_r2.extend(["b1",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in white:
            valid_moves_for_r2.extend(["a1",board[dikey][yatay-5]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_r2.extend(["h1",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white:
            valid_moves_for_r2.extend(["g1",board[dikey][yatay+1]])
    ###

    
    if piece=="R1" and dict_all["R1"]=="a8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R1.extend(["a7",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_R1.extend(["a6",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_R1.extend(["a5",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_R1.extend(["a4",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in black:
            valid_moves_for_R1.extend(["a3",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_R1.extend(["a2",board[dikey++6][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in combine and board[dikey+7][yatay] not in black:
            valid_moves_for_R1.extend(["a1",board[dikey+7][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_R1.extend(["b8",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_R1.extend(["c8",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_R1.extend(["d8",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_R1.extend(["e8",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in black:
            valid_moves_for_R1.extend(["f8",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in black:
            valid_moves_for_R1.extend(["g8",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in black:
            valid_moves_for_R1.extend(["h8",board[dikey][yatay+7]])
        
    if piece=="R1" and dict_all["R1"]=="a7":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R1.extend(["a6",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_R1.extend(["a5",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_R1.extend(["a4",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_R1.extend(["a3",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in combine and board[dikey+5][yatay] not in black:
            valid_moves_for_R1.extend(["a2",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_R1.extend(["a1",board[dikey+6][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_R1.extend(["a8",board[dikey-1][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_R1.extend(["b7",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_R1.extend(["c7",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_R1.extend(["d7",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_R1.extend(["e7",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in black:
            valid_moves_for_R1.extend(["f7",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in black:
            valid_moves_for_R1.extend(["g7",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in black:
            valid_moves_for_R1.extend(["h7",board[dikey][yatay+7]])
        
    if piece=="R1" and dict_all["R1"]=="a6":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R1.extend(["a5",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_R1.extend(["a4",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_R1.extend(["a3",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in combine and board[dikey+4][yatay] not in black:
            valid_moves_for_R1.extend(["a2",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in combine and board[dikey+5][yatay] not in black:
            valid_moves_for_R1.extend(["a1",board[dikey+5][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black:
            valid_moves_for_R1.extend(["a8",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_R1.extend(["a7",board[dikey-1][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_R1.extend(["b6",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_R1.extend(["c6",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_R1.extend(["d6",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_R1.extend(["e6",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in black:
            valid_moves_for_R1.extend(["f6",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in black:
            valid_moves_for_R1.extend(["g6",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in black:
            valid_moves_for_R1.extend(["h6",board[dikey][yatay+7]])
    
    if piece=="R1" and dict_all["R1"]=="a5":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R1.extend(["a4",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_R1.extend(["a3",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in combine and board[dikey+3][yatay] not in black:
            valid_moves_for_R1.extend(["a2",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in combine and board[dikey+4][yatay] not in black:
            valid_moves_for_R1.extend(["a1",board[dikey+4][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay] not in black:
            valid_moves_for_R1.extend(["a8",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black:
            valid_moves_for_R1.extend(["a7",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_R1.extend(["a6",board[dikey-1][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_R1.extend(["b5",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_R1.extend(["c5",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_R1.extend(["d5",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_R1.extend(["e5",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in black:
            valid_moves_for_R1.extend(["f5",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in black:
            valid_moves_for_R1.extend(["g5",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in black:
            valid_moves_for_R1.extend(["h5",board[dikey][yatay+7]])
    
    if piece=="R1" and dict_all["R1"]=="a4":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R1.extend(["a3",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in combine and board[dikey+2][yatay] not in black:
            valid_moves_for_R1.extend(["a2",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in combine and board[dikey+3][yatay] not in black:
            valid_moves_for_R1.extend(["a1",board[dikey+3][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay]  not in black and board[dikey-4][yatay] not in black:
            valid_moves_for_R1.extend(["a8",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay] not in black:
            valid_moves_for_R1.extend(["a7",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black:
            valid_moves_for_R1.extend(["a6",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_R1.extend(["a5",board[dikey-1][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_R1.extend(["b4",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_R1.extend(["c4",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_R1.extend(["d4",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_R1.extend(["e4",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in black:
            valid_moves_for_R1.extend(["f4",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in black:
            valid_moves_for_R1.extend(["g4",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in black:
            valid_moves_for_R1.extend(["h4",board[dikey][yatay+7]])
        
    if piece=="R1" and dict_all["R1"]=="a3":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R1.extend(["a2",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in combine and board[dikey+2][yatay] not in black:
            valid_moves_for_R1.extend(["a1",board[dikey+2][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay]  not in black and board[dikey-4][yatay] not in black and board[dikey-5][yatay] not in black:
            valid_moves_for_R1.extend(["a8",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay]  not in black and board[dikey-4][yatay] not in black:
            valid_moves_for_R1.extend(["a7",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay] not in black:
            valid_moves_for_R1.extend(["a6",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black:
            valid_moves_for_R1.extend(["a5",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_R1.extend(["a4",board[dikey-1][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_R1.extend(["b3",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_R1.extend(["c3",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_R1.extend(["d3",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_R1.extend(["e3",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in black:
            valid_moves_for_R1.extend(["f3",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in black:
            valid_moves_for_R1.extend(["g3",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in black:
            valid_moves_for_R1.extend(["h3",board[dikey][yatay+7]])
        
    if piece=="R1" and dict_all["R1"]=="a2":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R1.extend(["a1",board[dikey+1][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay]  not in black and board[dikey-4][yatay] not in black and board[dikey-5][yatay] not in black and board[dikey-6][yatay] not in black:
            valid_moves_for_R1.extend(["a8",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay]  not in black and board[dikey-4][yatay] not in black and board[dikey-5][yatay] not in black:
            valid_moves_for_R1.extend(["a7",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay]  not in black and board[dikey-4][yatay] not in black:
            valid_moves_for_R1.extend(["a6",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay] not in black:
            valid_moves_for_R1.extend(["a5",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black:
            valid_moves_for_R1.extend(["a4",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_R1.extend(["a3",board[dikey-1][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_R1.extend(["b2",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_R1.extend(["c1",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_R1.extend(["d2",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_R1.extend(["e2",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in black:
            valid_moves_for_R1.extend(["f2",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in black:
            valid_moves_for_R1.extend(["g2",board[dikey][yatay+6]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in combine and board[dikey][yatay+7] not in black:
            valid_moves_for_R1.extend(["h2",board[dikey][yatay+7]])

    if piece=="R1" and dict_all["R1"]=="b8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R1.extend(["b7",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_R1.extend(["b6",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_R1.extend(["b5",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_R1.extend(["b4",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in black:
            valid_moves_for_R1.extend(["b3",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_R1.extend(["b2",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in combine and board[dikey+7][yatay] not in black:
            valid_moves_for_R1.extend(["b1",board[dikey+7][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_R1.extend(["c8",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_R1.extend(["d8",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_R1.extend(["e8",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_R1.extend(["f8",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in black:
            valid_moves_for_R1.extend(["g8",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in black:
            valid_moves_for_R1.extend(["h8",board[dikey][yatay+6]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_R1.extend(["a8",board[dikey][yatay-1]])
    
    if piece=="R1" and dict_all["R1"]=="c8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R1.extend(["c7",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_R1.extend(["c6",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_R1.extend(["c5",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_R1.extend(["c4",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in black:
            valid_moves_for_R1.extend(["c3",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_R1.extend(["c2",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in combine and board[dikey+7][yatay] not in black:
            valid_moves_for_R1.extend(["c1",board[dikey+7][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_R1.extend(["d8",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_R1.extend(["e8",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_R1.extend(["f8",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_R1.extend(["g8",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in black:
            valid_moves_for_R1.extend(["h8",board[dikey][yatay+5]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_R1.extend(["a8",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_R1.extend(["b8",board[dikey][yatay-1]])
    
    if piece=="R1" and dict_all["R1"]=="d8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R1.extend(["d7",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_R1.extend(["d6",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_R1.extend(["d5",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_R1.extend(["d4",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in black:
            valid_moves_for_R1.extend(["d3",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_R1.extend(["d2",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in combine and board[dikey+7][yatay] not in black:
            valid_moves_for_R1.extend(["d1",board[dikey+7][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_R1.extend(["e8",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_R1.extend(["f8",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_R1.extend(["g8",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_R1.extend(["h8",board[dikey][yatay+4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_R1.extend(["a8",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_R1.extend(["b8",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_R1.extend(["c8",board[dikey][yatay-1]])

    if piece=="R2" and dict_all["R2"]=="h8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R2.extend(["h7",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_R2.extend(["h6",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_R2.extend(["h5",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_R2.extend(["h4",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in black:
            valid_moves_for_R2.extend(["h3",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_R2.extend(["h2",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in combine and board[dikey+7][yatay] not in black:
            valid_moves_for_R2.extend(["h1",board[dikey+7][yatay]])   
        if board[dikey][yatay-1] not in black:
            valid_moves_for_R2.extend(["g8",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_R2.extend(["f8",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_R2.extend(["e8",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black:
            valid_moves_for_R2.extend(["d8",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in black:
            valid_moves_for_R2.extend(["c8",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in black:
            valid_moves_for_R2.extend(["b8",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in black:
            valid_moves_for_R2.extend(["a8",board[dikey][yatay-7]])
    
    if piece=="R2" and dict_all["R2"]=="h7":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R2.extend(["h6",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_R2.extend(["h5",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_R2.extend(["h4",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_R2.extend(["h3",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in combine and board[dikey+5][yatay] not in black:
            valid_moves_for_R2.extend(["h2",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_R2.extend(["h1",board[dikey+6][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_R2.extend(["h8",board[dikey-1][yatay]])    
        if board[dikey][yatay-1] not in black:
            valid_moves_for_R2.extend(["g7",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_R2.extend(["f7",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_R2.extend(["e7",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black:
            valid_moves_for_R2.extend(["d7",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in black:
            valid_moves_for_R2.extend(["c7",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in black:
            valid_moves_for_R2.extend(["b7",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in black:
            valid_moves_for_R2.extend(["a7",board[dikey][yatay-7]])
    
    if piece=="R2" and dict_all["R2"]=="h6":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R2.extend(["h5",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_R2.extend(["h4",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_R2.extend(["h3",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in combine and board[dikey+4][yatay] not in black:
            valid_moves_for_R2.extend(["h2",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in combine and board[dikey+5][yatay] not in black:
            valid_moves_for_R2.extend(["h1",board[dikey+5][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black:
            valid_moves_for_R2.extend(["h8",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_R2.extend(["h7",board[dikey-1][yatay]])    
        if board[dikey][yatay-1] not in black:
            valid_moves_for_R2.extend(["g6",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_R2.extend(["f6",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_R2.extend(["e6",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black:
            valid_moves_for_R2.extend(["d6",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in black:
            valid_moves_for_R2.extend(["c6",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in black:
            valid_moves_for_R2.extend(["b6",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in black:
            valid_moves_for_R2.extend(["a6",board[dikey][yatay-7]])
    
    if piece=="R2" and dict_all["R2"]=="h5":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R2.extend(["h4",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_R2.extend(["h3",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in combine and board[dikey+3][yatay] not in black:
            valid_moves_for_R2.extend(["h2",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in combine and board[dikey+4][yatay] not in black:
            valid_moves_for_R2.extend(["h1",board[dikey+4][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay] not in black:
            valid_moves_for_R2.extend(["h8",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black:
            valid_moves_for_R2.extend(["h7",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_R2.extend(["h6",board[dikey-1][yatay]])    
        if board[dikey][yatay-1] not in black:
            valid_moves_for_R2.extend(["g5",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_R2.extend(["f5",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_R2.extend(["e5",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black:
            valid_moves_for_R2.extend(["d5",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in black:
            valid_moves_for_R2.extend(["c5",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in black:
            valid_moves_for_R2.extend(["b5",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in black:
            valid_moves_for_R2.extend(["a5",board[dikey][yatay-7]])
        
    if piece=="R2" and dict_all["R2"]=="h4":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R2.extend(["h3",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in combine and board[dikey+2][yatay] not in black:
            valid_moves_for_R2.extend(["h2",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in combine and board[dikey+3][yatay] not in black:
            valid_moves_for_R2.extend(["h1",board[dikey+3][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay]  not in black and board[dikey-4][yatay] not in black:
            valid_moves_for_R2.extend(["h8",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay] not in black:
            valid_moves_for_R2.extend(["h7",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black:
            valid_moves_for_R2.extend(["h6",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_R2.extend(["h5",board[dikey-1][yatay]])    
        if board[dikey][yatay-1] not in black:
            valid_moves_for_R2.extend(["g4",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_R2.extend(["f4",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_R2.extend(["e4",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black:
            valid_moves_for_R2.extend(["d4",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in black:
            valid_moves_for_R2.extend(["c4",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in black:
            valid_moves_for_R2.extend(["b4",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in black:
            valid_moves_for_R2.extend(["a4",board[dikey][yatay-7]])
    
    if piece=="R2" and dict_all["R2"]=="h3":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R2.extend(["h2",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in combine and board[dikey+2][yatay] not in black:
            valid_moves_for_R2.extend(["h1",board[dikey+2][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay]  not in black and board[dikey-4][yatay] not in black and board[dikey-5][yatay] not in black:
            valid_moves_for_R2.extend(["h8",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay]  not in black and board[dikey-4][yatay] not in black:
            valid_moves_for_R2.extend(["h7",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay] not in black:
            valid_moves_for_R2.extend(["h6",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black:
            valid_moves_for_R2.extend(["h5",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_R2.extend(["h4",board[dikey-1][yatay]])    
        if board[dikey][yatay-1] not in black:
            valid_moves_for_R2.extend(["g3",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_R2.extend(["f3",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_R2.extend(["e3",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black:
            valid_moves_for_R2.extend(["d3",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in black:
            valid_moves_for_R2.extend(["c3",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in black:
            valid_moves_for_R2.extend(["b3",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in black:
            valid_moves_for_R2.extend(["a3",board[dikey][yatay-7]])
    



    if piece=="R2" and dict_all["R2"]=="h2":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R2.extend(["h1",board[dikey+1][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay]  not in black and board[dikey-4][yatay] not in black and board[dikey-5][yatay] not in black and board[dikey-6][yatay] not in black:
            valid_moves_for_R2.extend(["h8",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay]  not in black and board[dikey-4][yatay] not in black and board[dikey-5][yatay] not in black:
            valid_moves_for_R2.extend(["h7",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay]  not in black and board[dikey-4][yatay] not in black:
            valid_moves_for_R2.extend(["h6",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay] not in black:
            valid_moves_for_R2.extend(["h5",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black:
            valid_moves_for_R2.extend(["h4",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_R2.extend(["h3",board[dikey-1][yatay]])    
        if board[dikey][yatay-1] not in black:
            valid_moves_for_R2.extend(["g2",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_R2.extend(["f2",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_R2.extend(["e2",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black:
            valid_moves_for_R2.extend(["d2",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in black:
            valid_moves_for_R2.extend(["c2",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in black:
            valid_moves_for_R2.extend(["b2",board[dikey][yatay-6]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in combine and board[dikey][yatay-7] not in black:
            valid_moves_for_R2.extend(["a2",board[dikey][yatay-7]])
    
    if piece=="R2" and dict_all["R2"]=="g8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R2.extend(["g7",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_R2.extend(["g6",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_R2.extend(["g5",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_R2.extend(["g4",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in black:
            valid_moves_for_R2.extend(["g3",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_R2.extend(["g2",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in combine and board[dikey+7][yatay] not in black:
            valid_moves_for_R2.extend(["g1",board[dikey+7][yatay]])   
        if board[dikey][yatay-1] not in black:
            valid_moves_for_R2.extend(["f8",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_R2.extend(["e8",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_R2.extend(["d8",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black:
            valid_moves_for_R2.extend(["c8",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in black:
            valid_moves_for_R2.extend(["b8",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in black:
            valid_moves_for_R2.extend(["a8",board[dikey][yatay-6]])
        if board[dikey][yatay+1] not in black:
            valid_moves_for_R2.extend(["h8",board[dikey][yatay+1]])
    
    if piece=="R2" and dict_all["R2"]=="f8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_R2.extend(["f7",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_R2.extend(["f6",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_R2.extend(["f5",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_R2.extend(["f4",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in black:
            valid_moves_for_R2.extend(["f3",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_R2.extend(["f2",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in combine and board[dikey+7][yatay] not in black:
            valid_moves_for_R2.extend(["f1",board[dikey+7][yatay]])   
        if board[dikey][yatay-1] not in black:
            valid_moves_for_R2.extend(["e8",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_R2.extend(["d8",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_R2.extend(["c8",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black:
            valid_moves_for_R2.extend(["b8",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in black:
            valid_moves_for_R2.extend(["a8",board[dikey][yatay-5]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_R2.extend(["h8",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black:
            valid_moves_for_R2.extend(["g8",board[dikey][yatay+1]])
    
    if piece=="qu" and dict_all["qu"]=="d1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_qu.extend(["d2",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_qu.extend(["d3",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_qu.extend(["d4",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_qu.extend(["d5",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in white:
            valid_moves_for_qu.extend(["d6",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_qu.extend(["d7",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in combine and board[dikey-7][yatay] not in white:
            valid_moves_for_qu.extend(["d8",board[dikey-7][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_qu.extend(["e1",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_qu.extend(["f1",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_qu.extend(["g1",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_qu.extend(["h1",board[dikey][yatay+4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_qu.extend(["a1",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_qu.extend(["b1",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_qu.extend(["c1",board[dikey][yatay-1]])
        if board[dikey-1][yatay-1] not in white  :
            valid_moves_for_qu.extend(["c2", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_qu.extend(["b3",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_qu.extend(["a4",board[dikey-3][yatay-3]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_qu.extend(["e2",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_qu.extend(["f3",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_qu.extend(["g4",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white:
            valid_moves_for_qu.extend(["h5",board[dikey-4][yatay+4]])

    if piece=="qu" and dict_all["qu"]=="d2":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_qu.extend(["d3",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_qu.extend(["d4",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_qu.extend(["d5",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_qu.extend(["d6",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in combine and board[dikey-5][yatay] not in white:
            valid_moves_for_qu.extend(["d7",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_qu.extend(["d8",board[dikey-6][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_qu.extend(["d2",board[dikey+1][yatay]])  
        if board[dikey][yatay+1] not in white:
            valid_moves_for_qu.extend(["e3",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_qu.extend(["f3",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_qu.extend(["g3",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_qu.extend(["h3",board[dikey][yatay+4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_qu.extend(["a3",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_qu.extend(["b3",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_qu.extend(["c3",board[dikey][yatay-1]])
        if board[dikey-1][yatay-1] not in white  :
            valid_moves_for_qu.extend(["c3", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_qu.extend(["b4",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_qu.extend(["a5",board[dikey-3][yatay-3]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_qu.extend(["e3",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_qu.extend(["f4",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_qu.extend(["g5",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white:
            valid_moves_for_qu.extend(["h6",board[dikey-4][yatay+4]])
        if board[dikey+1][yatay-1] not in white  :
            valid_moves_for_qu.extend(["c1", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in white  :
            valid_moves_for_qu.extend(["e1", board[dikey+1][yatay+1]]) 
        
    if piece=="qu" and dict_all["qu"]=="d3":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_qu.extend(["d4",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_qu.extend(["d5",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_qu.extend(["d6",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in combine and board[dikey-4][yatay] not in white:
            valid_moves_for_qu.extend(["d7",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in combine and board[dikey-5][yatay] not in white:
            valid_moves_for_qu.extend(["d8",board[dikey-5][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white:
            valid_moves_for_qu.extend(["d1",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_qu.extend(["d2",board[dikey+1][yatay]])  
        if board[dikey][yatay+1] not in white:
            valid_moves_for_qu.extend(["e3",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_qu.extend(["f3",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_qu.extend(["g3",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_qu.extend(["h3",board[dikey][yatay+4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_qu.extend(["a3",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_qu.extend(["b3",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_qu.extend(["c3",board[dikey][yatay-1]])
        if board[dikey-1][yatay-1] not in white  :
            valid_moves_for_qu.extend(["c4", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_qu.extend(["b5",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_qu.extend(["a6",board[dikey-3][yatay-3]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_qu.extend(["e4",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_qu.extend(["f5",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_qu.extend(["g6",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white:
            valid_moves_for_qu.extend(["h7",board[dikey-4][yatay+4]])
        if board[dikey+1][yatay-1] not in white  :
            valid_moves_for_qu.extend(["c2", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in white  :
            valid_moves_for_qu.extend(["e2", board[dikey+1][yatay+1]]) 
        if board[dikey+1][yatay+1] not in white and board[dikey+2][yatay+2] not in white:
            valid_moves_for_qu.extend(["f1",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay-1] not in white and board[dikey+2][yatay-2] not in white:
            valid_moves_for_qu.extend(["b1",board[dikey+2][yatay-2]])
    
    if piece=="qu" and dict_all["qu"]=="d4":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_qu.extend(["d5",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_qu.extend(["d6",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in combine and board[dikey-3][yatay] not in white:
            valid_moves_for_qu.extend(["d7",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in combine and board[dikey-4][yatay] not in white:
            valid_moves_for_qu.extend(["d8",board[dikey-4][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay] not in white:
            valid_moves_for_qu.extend(["d1",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white:
            valid_moves_for_qu.extend(["d2",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_qu.extend(["d3",board[dikey+1][yatay]]) 
        if board[dikey][yatay+1] not in white:
            valid_moves_for_qu.extend(["e4",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_qu.extend(["f4",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_qu.extend(["g4",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_qu.extend(["h4",board[dikey][yatay+4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_qu.extend(["a4",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_qu.extend(["b4",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_qu.extend(["c4",board[dikey][yatay-1]])
        if board[dikey-1][yatay-1] not in white  :
            valid_moves_for_qu.extend(["c5", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_qu.extend(["b6",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_qu.extend(["a7",board[dikey-3][yatay-3]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_qu.extend(["e5",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_qu.extend(["f6",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_qu.extend(["g7",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in combine and board[dikey-4][yatay+4] not in white:
            valid_moves_for_qu.extend(["h8",board[dikey-4][yatay+4]])
        if board[dikey+1][yatay-1] not in white  :
            valid_moves_for_qu.extend(["c3", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in white  :
            valid_moves_for_qu.extend(["e3", board[dikey+1][yatay+1]]) 
        if board[dikey+1][yatay+1] not in white and board[dikey+2][yatay+2] not in white:
            valid_moves_for_qu.extend(["f2",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay-1] not in white and board[dikey+2][yatay-2] not in white:
            valid_moves_for_qu.extend(["b2",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay+1] not in white and board[dikey+2][yatay+2] not in white and board[dikey+3][yatay+3] not in white:
            valid_moves_for_qu.extend(["g1",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay-1] not in white and board[dikey+2][yatay-2] not in white and board[dikey+3][yatay-3] not in white:
            valid_moves_for_qu.extend(["a1",board[dikey+3][yatay-3]])
    
    if piece=="qu" and dict_all["qu"]=="d5":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_qu.extend(["d6",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in combine:
            valid_moves_for_qu.extend(["d7",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in combine and board[dikey-3][yatay] not in white:
            valid_moves_for_qu.extend(["d8",board[dikey-3][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay]  not in combine and board[dikey+4][yatay] not in white:
            valid_moves_for_qu.extend(["d1",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white and board[dikey+3][yatay] not in white:
            valid_moves_for_qu.extend(["d2",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in white and board[dikey+2][yatay] not in white:
            valid_moves_for_qu.extend(["d3",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_qu.extend(["d4",board[dikey+1][yatay]]) 
        if board[dikey][yatay+1] not in white:
            valid_moves_for_qu.extend(["e5",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_qu.extend(["f5",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_qu.extend(["g5",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_qu.extend(["h5",board[dikey][yatay+4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_qu.extend(["a5",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_qu.extend(["b5",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_qu.extend(["c5",board[dikey][yatay-1]])
        if board[dikey-1][yatay-1] not in white  :
            valid_moves_for_qu.extend(["c6", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_qu.extend(["b7",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_qu.extend(["a8",board[dikey-3][yatay-3]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_qu.extend(["e6",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in combine and board[dikey-2][yatay+2] not in white:
            valid_moves_for_qu.extend(["f7",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in combine and board[dikey-3][yatay+3] not in white:
            valid_moves_for_qu.extend(["g8",board[dikey-3][yatay+3]])
        if board[dikey+1][yatay-1] not in white  :
            valid_moves_for_qu.extend(["c4", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in white  :
            valid_moves_for_qu.extend(["e4", board[dikey+1][yatay+1]]) 
        if board[dikey+1][yatay+1] not in white and board[dikey+2][yatay+2] not in white:
            valid_moves_for_qu.extend(["f3",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay-1] not in white and board[dikey+2][yatay-2] not in white:
            valid_moves_for_qu.extend(["b3",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay+1] not in white and board[dikey+2][yatay+2] not in white and board[dikey+3][yatay+3] not in white:
            valid_moves_for_qu.extend(["g2",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay-1] not in white and board[dikey+2][yatay-2] not in white and board[dikey+3][yatay-3] not in white:
            valid_moves_for_qu.extend(["a2",board[dikey+3][yatay-3]])
        if board[dikey+1][yatay+1] not in white and board[dikey+2][yatay+2] not in white and board[dikey+3][yatay+3] not in combine and board[dikey+4][yatay+4] not in white:
            valid_moves_for_qu.extend(["h1",board[dikey+4][yatay+4]])
    
    if piece=="qu" and dict_all["qu"]=="c1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_qu.extend(["c2",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_qu.extend(["c3",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_qu.extend(["c4",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_qu.extend(["c5",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in white:
            valid_moves_for_qu.extend(["c6",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_qu.extend(["c7",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in combine and board[dikey-7][yatay] not in white:
            valid_moves_for_qu.extend(["c8",board[dikey-7][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_qu.extend(["d1",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_qu.extend(["e1",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_qu.extend(["f1",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_qu.extend(["g1",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in white:
            valid_moves_for_qu.extend(["h1",board[dikey][yatay+5]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_qu.extend(["a1",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_qu.extend(["b1",board[dikey][yatay-1]])
        if board[dikey-1][yatay-1] not in white  :
            valid_moves_for_qu.extend(["b2", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_qu.extend(["a3",board[dikey-2][yatay-2]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_qu.extend(["d2",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_qu.extend(["e3",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_qu.extend(["f4",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white:
            valid_moves_for_qu.extend(["g5",board[dikey-4][yatay+4]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white and board[dikey-5][yatay+5] not in white:
            valid_moves_for_qu.extend(["h6",board[dikey-5][yatay+5]])
         
    if piece=="qu" and dict_all["qu"]=="b1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_qu.extend(["b2",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_qu.extend(["b3",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_qu.extend(["b4",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_qu.extend(["b5",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in white:
            valid_moves_for_qu.extend(["b6",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_qu.extend(["b7",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in combine and board[dikey-7][yatay] not in white:
            valid_moves_for_qu.extend(["b8",board[dikey-7][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_qu.extend(["c1",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_qu.extend(["d1",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_qu.extend(["e1",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_qu.extend(["f1",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in white:
            valid_moves_for_qu.extend(["g1",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in white:
            valid_moves_for_qu.extend(["h1",board[dikey][yatay+6]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_qu.extend(["a1",board[dikey][yatay-1]])
        if board[dikey-1][yatay-1] not in white  :
            valid_moves_for_qu.extend(["a2", board[dikey-1][yatay-1]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_qu.extend(["c2",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_qu.extend(["d3",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_qu.extend(["e4",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white:
            valid_moves_for_qu.extend(["f5",board[dikey-4][yatay+4]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in combine and board[dikey-5][yatay+5] not in white:
            valid_moves_for_qu.extend(["g6",board[dikey-5][yatay+5]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white and board[dikey-5][yatay+5] not in combine and board[dikey-6][yatay+6] not in white :
            valid_moves_for_qu.extend(["h7",board[dikey-6][yatay+6]])
    
    if piece=="qu" and dict_all["qu"]=="e1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_qu.extend(["e2",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_qu.extend(["e3",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_qu.extend(["e4",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_qu.extend(["e5",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in white:
            valid_moves_for_qu.extend(["e6",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_qu.extend(["e7",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in combine and board[dikey-7][yatay] not in white:
            valid_moves_for_qu.extend(["e8",board[dikey-7][yatay]])   
        if board[dikey][yatay-1] not in white:
            valid_moves_for_qu.extend(["d1",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_qu.extend(["c1",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_qu.extend(["b1",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white:
            valid_moves_for_qu.extend(["a1",board[dikey][yatay-4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white :
            valid_moves_for_qu.extend(["h1",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_qu.extend(["g1",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white:
            valid_moves_for_qu.extend(["f1",board[dikey][yatay+1]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_qu.extend(["f2",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_qu.extend(["g3",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_qu.extend(["h4",board[dikey-3][yatay+3]])
        if  board[dikey-1][yatay-1] not in white :
            valid_moves_for_qu.extend(["d2",board[dikey-1][yatay-1]])
        if  board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_qu.extend(["c3",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_qu.extend(["b4",board[dikey-3][yatay-3]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white:
            valid_moves_for_qu.extend(["a5",board[dikey-4][yatay-4]])
    
    if piece=="qu" and dict_all["qu"]=="f1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_qu.extend(["f2",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_qu.extend(["f3",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_qu.extend(["f4",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_qu.extend(["f5",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in white:
            valid_moves_for_qu.extend(["f6",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_qu.extend(["f7",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in combine and board[dikey-7][yatay] not in white:
            valid_moves_for_qu.extend(["f8",board[dikey-7][yatay]])   
        if board[dikey][yatay-1] not in white:
            valid_moves_for_qu.extend(["e1",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_qu.extend(["d1",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_qu.extend(["c1",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white:
            valid_moves_for_qu.extend(["b1",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in white:
            valid_moves_for_qu.extend(["a1",board[dikey][yatay-5]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_qu.extend(["h1",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white:
            valid_moves_for_qu.extend(["g1",board[dikey][yatay+1]])
        if board[dikey-1][yatay+1] not in white  :
            valid_moves_for_qu.extend(["g2", board[dikey-1][yatay+1]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_qu.extend(["h3",board[dikey-2][yatay+2]])
        if  board[dikey-1][yatay-1] not in white :
            valid_moves_for_qu.extend(["e2",board[dikey-1][yatay-1]])
        if  board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_qu.extend(["d3",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_qu.extend(["c4",board[dikey-3][yatay-3]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white:
            valid_moves_for_qu.extend(["b5",board[dikey-4][yatay-4]])
        if  board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white and board[dikey-5][yatay-5] not in white:
            valid_moves_for_qu.extend(["a6",board[dikey-5][yatay-5]])
    
    if piece=="qu" and dict_all["qu"]=="g1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_qu.extend(["g2",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_qu.extend(["g3",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_qu.extend(["g4",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_qu.extend(["g5",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in white:
            valid_moves_for_qu.extend(["g6",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_qu.extend(["g7",board[dikey-6][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in combine and board[dikey-7][yatay] not in white:
            valid_moves_for_qu.extend(["g8",board[dikey-7][yatay]])   
        if board[dikey][yatay-1] not in white:
            valid_moves_for_qu.extend(["f1",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_qu.extend(["e1",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_qu.extend(["d1",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white:
            valid_moves_for_qu.extend(["c1",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in white:
            valid_moves_for_qu.extend(["b1",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in white:
            valid_moves_for_qu.extend(["a1",board[dikey][yatay-6]])
        if board[dikey][yatay+1] not in white:
            valid_moves_for_qu.extend(["h1",board[dikey][yatay+1]])
        if board[dikey-1][yatay+1] not in white :
            valid_moves_for_qu.extend(["h2", board[dikey-1][yatay+1]])    
        if  board[dikey-1][yatay-1] not in white :
            valid_moves_for_qu.extend(["f2",board[dikey-1][yatay-1]])
        if  board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_qu.extend(["e3",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_qu.extend(["d4",board[dikey-3][yatay-3]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white:
            valid_moves_for_qu.extend(["c5",board[dikey-4][yatay-4]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white and board[dikey-5][yatay-5] not in white:
            valid_moves_for_qu.extend(["b6",board[dikey-5][yatay-5]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white and board[dikey-5][yatay-5] not in combine and board[dikey-6][yatay-6] not in white :
            valid_moves_for_qu.extend(["a7",board[dikey-6][yatay-6]])

    if piece=="qu" and dict_all["qu"]=="c2":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_qu.extend(["c3",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_qu.extend(["c4",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_qu.extend(["c5",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_qu.extend(["c6",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in combine and board[dikey-5][yatay] not in white:
            valid_moves_for_qu.extend(["c7",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_qu.extend(["c8",board[dikey-6][yatay]])
        if board[dikey+1][yatay] not in white :
            valid_moves_for_qu.extend(["c1",board[dikey+1][yatay]])   
        if board[dikey][yatay+1] not in white:
            valid_moves_for_qu.extend(["d2",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_qu.extend(["e2",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3] not in white:
            valid_moves_for_qu.extend(["f2",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white:
            valid_moves_for_qu.extend(["g2",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white and board[dikey][yatay+4] not in white and board[dikey][yatay+5] not in white:
            valid_moves_for_qu.extend(["h2",board[dikey][yatay+5]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_qu.extend(["a2",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_qu.extend(["b2",board[dikey][yatay-1]])
        if board[dikey-1][yatay-1] not in white  :
            valid_moves_for_qu.extend(["b3", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_qu.extend(["a4",board[dikey-2][yatay-2]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_qu.extend(["d3",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_qu.extend(["e4",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_qu.extend(["f5",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white:
            valid_moves_for_qu.extend(["g6",board[dikey-4][yatay+4]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white and board[dikey-4][yatay+4] not in white and board[dikey-5][yatay+5] not in white:
            valid_moves_for_qu.extend(["h7",board[dikey-5][yatay+5]])
    
    if piece=="qu" and dict_all["qu"]=="e2":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_qu.extend(["e3",board[dikey-1][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white:
            valid_moves_for_qu.extend(["e4",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay] not in white:
            valid_moves_for_qu.extend(["e5",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white:
            valid_moves_for_qu.extend(["e6",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in combine and board[dikey-5][yatay] not in white:
            valid_moves_for_qu.extend(["e7",board[dikey-5][yatay]])
        if board[dikey-1][yatay] not in white and board[dikey-2][yatay] not in white and board[dikey-3][yatay]  not in white and board[dikey-4][yatay] not in white and board[dikey-5][yatay] not in combine and board[dikey-6][yatay] not in white:
            valid_moves_for_qu.extend(["e8",board[dikey-6][yatay]])
        if board[dikey+1][yatay] not in white:
            valid_moves_for_qu.extend(["e2",board[dikey+1][yatay]])   
        if board[dikey][yatay-1] not in white:
            valid_moves_for_qu.extend(["d2",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white:
            valid_moves_for_qu.extend(["c2",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3] not in white:
            valid_moves_for_qu.extend(["b2",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in white and board[dikey][yatay-2] not in white and board[dikey][yatay-3]  not in white and board[dikey][yatay-4] not in white:
            valid_moves_for_qu.extend(["a2",board[dikey][yatay-4]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white and board[dikey][yatay+3]  not in white :
            valid_moves_for_qu.extend(["h2",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in white and board[dikey][yatay+2] not in white:
            valid_moves_for_qu.extend(["g2",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in white:
            valid_moves_for_qu.extend(["f2",board[dikey][yatay+1]])
        if  board[dikey-1][yatay+1] not in white :
            valid_moves_for_qu.extend(["f3",board[dikey-1][yatay+1]])
        if  board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white:
            valid_moves_for_qu.extend(["g4",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay+1] not in white and board[dikey-2][yatay+2] not in white and board[dikey-3][yatay+3] not in white:
            valid_moves_for_qu.extend(["h5",board[dikey-3][yatay+3]])
        if  board[dikey-1][yatay-1] not in white :
            valid_moves_for_qu.extend(["d3",board[dikey-1][yatay-1]])
        if  board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white:
            valid_moves_for_qu.extend(["c4",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white:
            valid_moves_for_qu.extend(["b5",board[dikey-3][yatay-3]])
        if board[dikey-1][yatay-1] not in white and board[dikey-2][yatay-2] not in white and board[dikey-3][yatay-3] not in white and board[dikey-4][yatay-4] not in white:
            valid_moves_for_qu.extend(["a6",board[dikey-4][yatay-4]])

    

    if piece=="QU" and dict_all["QU"]=="d8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_QU.extend(["d7",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_QU.extend(["d6",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_QU.extend(["d5",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_QU.extend(["d4",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in black:
            valid_moves_for_QU.extend(["d3",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_QU.extend(["d2",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in combine and board[dikey+7][yatay] not in black:
            valid_moves_for_QU.extend(["d1",board[dikey+7][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_QU.extend(["e8",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_QU.extend(["f8",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_QU.extend(["g8",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_QU.extend(["h8",board[dikey][yatay+4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_QU.extend(["a8",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_QU.extend(["b8",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_QU.extend(["c8",board[dikey][yatay-1]])
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_QU.extend(["c7", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_QU.extend(["b6",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_QU.extend(["a5",board[dikey+3][yatay-3]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_QU.extend(["e7",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_QU.extend(["f6",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_QU.extend(["g5",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black:
            valid_moves_for_QU.extend(["h4",board[dikey+4][yatay+4]])

    if piece=="QU" and dict_all["QU"]=="d7":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_QU.extend(["d6",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_QU.extend(["d5",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_QU.extend(["d4",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_QU.extend(["d3",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in combine and board[dikey+5][yatay] not in black:
            valid_moves_for_QU.extend(["d2",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_QU.extend(["d1",board[dikey+6][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_QU.extend(["d8",board[dikey-1][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_QU.extend(["e7",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_QU.extend(["f7",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_QU.extend(["g7",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_QU.extend(["h7",board[dikey][yatay+4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_QU.extend(["a7",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_QU.extend(["b7",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_QU.extend(["c7",board[dikey][yatay-1]])
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_QU.extend(["c6", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_QU.extend(["b5",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_QU.extend(["a4",board[dikey+3][yatay-3]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_QU.extend(["e6",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_QU.extend(["f5",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_QU.extend(["g4",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black:
            valid_moves_for_QU.extend(["h3",board[dikey+4][yatay+4]])
        if board[dikey-1][yatay-1] not in black  :
            valid_moves_for_QU.extend(["c8", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in black  :
            valid_moves_for_QU.extend(["e8", board[dikey-1][yatay+1]]) 
        
    if piece=="QU" and dict_all["QU"]=="d6":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_QU.extend(["d5",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_QU.extend(["d4",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_QU.extend(["d3",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in combine and board[dikey+4][yatay] not in black:
            valid_moves_for_QU.extend(["d2",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in combine and board[dikey+5][yatay] not in black:
            valid_moves_for_QU.extend(["d1",board[dikey+5][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black:
            valid_moves_for_QU.extend(["d8",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_QU.extend(["d7",board[dikey-1][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_QU.extend(["e6",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_QU.extend(["f6",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_QU.extend(["g6",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_QU.extend(["h6",board[dikey][yatay+4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_QU.extend(["a6",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_QU.extend(["b6",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_QU.extend(["c6",board[dikey][yatay-1]])
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_QU.extend(["c5", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_QU.extend(["b4",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_QU.extend(["a3",board[dikey+3][yatay-3]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_QU.extend(["e5",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_QU.extend(["f4",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_QU.extend(["g3",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black:
            valid_moves_for_QU.extend(["h2",board[dikey+4][yatay+4]])
        if board[dikey-1][yatay-1] not in black  :
            valid_moves_for_QU.extend(["c7", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in black  :
            valid_moves_for_QU.extend(["e7", board[dikey-1][yatay+1]]) 
        if board[dikey-1][yatay+1] not in black and board[dikey-2][yatay+2] not in black:
            valid_moves_for_QU.extend(["f8",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay-1] not in black and board[dikey-2][yatay-2] not in black:
            valid_moves_for_QU.extend(["b8",board[dikey+-2][yatay-2]])
    
    if piece=="QU" and dict_all["QU"]=="d5":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_QU.extend(["d4",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_QU.extend(["d3",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in combine and board[dikey+3][yatay] not in black:
            valid_moves_for_QU.extend(["d2",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in combine and board[dikey+4][yatay] not in black:
            valid_moves_for_QU.extend(["d1",board[dikey+4][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay] not in black:
            valid_moves_for_QU.extend(["d8",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black:
            valid_moves_for_QU.extend(["d7",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_QU.extend(["d6",board[dikey-1][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_QU.extend(["e5",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_QU.extend(["f5",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_QU.extend(["g5",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_QU.extend(["h5",board[dikey][yatay+4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_QU.extend(["a5",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_QU.extend(["b5",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_QU.extend(["c5",board[dikey][yatay-1]])
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_QU.extend(["c4", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_QU.extend(["b3",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_QU.extend(["a2",board[dikey+3][yatay-3]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_QU.extend(["e4",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_QU.extend(["f3",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_QU.extend(["g2",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in combine and board[dikey+4][yatay+4] not in black:
            valid_moves_for_QU.extend(["h1",board[dikey+4][yatay+4]])
        if board[dikey-1][yatay-1] not in black  :
            valid_moves_for_QU.extend(["c6", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in black  :
            valid_moves_for_QU.extend(["e6", board[dikey-1][yatay+1]]) 
        if board[dikey-1][yatay+1] not in black and board[dikey-2][yatay+2] not in black:
            valid_moves_for_QU.extend(["f7",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay-1] not in black and board[dikey-2][yatay-2] not in black:
            valid_moves_for_QU.extend(["b7",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay+1] not in black and board[dikey-2][yatay+2] not in black and board[dikey-3][yatay+3] not in black:
            valid_moves_for_QU.extend(["g8",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay-1] not in black and board[dikey-2][yatay-2] not in black and board[dikey-3][yatay-3] not in black:
            valid_moves_for_QU.extend(["a8",board[dikey-3][yatay-3]])
    
    if piece=="QU" and dict_all["QU"]=="d4":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_QU.extend(["d3",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in combine:
            valid_moves_for_QU.extend(["d2",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in combine and board[dikey+3][yatay] not in black:
            valid_moves_for_QU.extend(["d1",board[dikey+3][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay]  not in combine and board[dikey-4][yatay] not in black:
            valid_moves_for_QU.extend(["d8",board[dikey-4][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black and board[dikey-3][yatay] not in black:
            valid_moves_for_QU.extend(["d7",board[dikey-3][yatay]])
        if board[dikey-1][yatay] not in black and board[dikey-2][yatay] not in black:
            valid_moves_for_QU.extend(["d6",board[dikey-2][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_QU.extend(["d5",board[dikey-1][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_QU.extend(["e4",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_QU.extend(["f4",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_QU.extend(["g4",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_QU.extend(["h4",board[dikey][yatay+4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_QU.extend(["a4",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_QU.extend(["b4",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_QU.extend(["c4",board[dikey][yatay-1]])
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_QU.extend(["c3", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_QU.extend(["b2",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_QU.extend(["a1",board[dikey+3][yatay-3]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_QU.extend(["e3",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in combine and board[dikey+2][yatay+2] not in black:
            valid_moves_for_QU.extend(["f2",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in combine and board[dikey+3][yatay+3] not in black:
            valid_moves_for_QU.extend(["g1",board[dikey+3][yatay+3]])
        if board[dikey-1][yatay-1] not in black  :
            valid_moves_for_QU.extend(["c5", board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in black  :
            valid_moves_for_QU.extend(["e5", board[dikey-1][yatay+1]]) 
        if board[dikey-1][yatay+1] not in black and board[dikey-2][yatay+2] not in black:
            valid_moves_for_QU.extend(["f6",board[dikey-2][yatay+2]])
        if board[dikey-1][yatay-1] not in black and board[dikey-2][yatay-2] not in black:
            valid_moves_for_QU.extend(["b6",board[dikey-2][yatay-2]])
        if board[dikey-1][yatay+1] not in black and board[dikey-2][yatay+2] not in black and board[dikey-3][yatay+3] not in black:
            valid_moves_for_QU.extend(["g7",board[dikey-3][yatay+3]])
        if board[dikey-1][yatay-1] not in black and board[dikey-2][yatay-2] not in black and board[dikey-3][yatay-3] not in black:
            valid_moves_for_QU.extend(["a7",board[dikey-3][yatay-3]])
        if board[dikey-1][yatay+1] not in black and board[dikey-2][yatay+2] not in black and board[dikey-3][yatay+3] not in combine and board[dikey-4][yatay+4] not in black:
            valid_moves_for_QU.extend(["h8",board[dikey-4][yatay+4]])
    
    if piece=="QU" and dict_all["QU"]=="c8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_QU.extend(["c7",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_QU.extend(["c6",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_QU.extend(["c5",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_QU.extend(["c4",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in black:
            valid_moves_for_QU.extend(["c3",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_QU.extend(["c2",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in combine and board[dikey+7][yatay] not in black:
            valid_moves_for_QU.extend(["c1",board[dikey+7][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_QU.extend(["d8",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_QU.extend(["e8",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_QU.extend(["f8",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_QU.extend(["g8",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in black:
            valid_moves_for_QU.extend(["h8",board[dikey][yatay+5]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_QU.extend(["a8",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_QU.extend(["b8",board[dikey][yatay-1]])
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_QU.extend(["b7", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_QU.extend(["a6",board[dikey+2][yatay-2]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_QU.extend(["d7",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_QU.extend(["e6",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_QU.extend(["f5",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black:
            valid_moves_for_QU.extend(["g4",board[dikey+4][yatay+4]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black and board[dikey+5][yatay+5] not in black:
            valid_moves_for_QU.extend(["h3",board[dikey+5][yatay+5]])
         
    if piece=="QU" and dict_all["QU"]=="b8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_QU.extend(["b7",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_QU.extend(["b6",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_QU.extend(["b5",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_QU.extend(["b4",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in black:
            valid_moves_for_QU.extend(["b3",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_QU.extend(["b2",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in combine and board[dikey+7][yatay] not in black:
            valid_moves_for_QU.extend(["b1",board[dikey+7][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_QU.extend(["c8",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_QU.extend(["d8",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_QU.extend(["e8",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_QU.extend(["f8",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in black:
            valid_moves_for_QU.extend(["g8",board[dikey][yatay+5]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in combine and board[dikey][yatay+6] not in black:
            valid_moves_for_QU.extend(["h8",board[dikey][yatay+6]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_QU.extend(["a8",board[dikey][yatay-1]])
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_QU.extend(["a7", board[dikey+1][yatay-1]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_QU.extend(["c7",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_QU.extend(["d6",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_QU.extend(["e5",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black:
            valid_moves_for_QU.extend(["f4",board[dikey+4][yatay+4]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in combine and board[dikey+5][yatay+5] not in black:
            valid_moves_for_QU.extend(["g3",board[dikey+5][yatay+5]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black and board[dikey+5][yatay+5] not in combine and board[dikey+6][yatay+6] not in black :
            valid_moves_for_QU.extend(["h2",board[dikey+6][yatay+6]])
    
    if piece=="QU" and dict_all["QU"]=="e8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_QU.extend(["e7",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_QU.extend(["e6",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_QU.extend(["e5",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_QU.extend(["e4",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in black:
            valid_moves_for_QU.extend(["e3",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_QU.extend(["e2",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in combine and board[dikey+7][yatay] not in black:
            valid_moves_for_QU.extend(["e1",board[dikey+7][yatay]])   
        if board[dikey][yatay-1] not in black:
            valid_moves_for_QU.extend(["d8",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_QU.extend(["c8",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_QU.extend(["b8",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black:
            valid_moves_for_QU.extend(["a8",board[dikey][yatay-4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black :
            valid_moves_for_QU.extend(["h8",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_QU.extend(["g8",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black:
            valid_moves_for_QU.extend(["f8",board[dikey][yatay+1]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_QU.extend(["f7",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_QU.extend(["g6",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_QU.extend(["h5",board[dikey+3][yatay+3]])
        if  board[dikey+1][yatay-1] not in black :
            valid_moves_for_QU.extend(["d7",board[dikey+1][yatay-1]])
        if  board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_QU.extend(["c6",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_QU.extend(["b5",board[dikey+3][yatay-3]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black:
            valid_moves_for_QU.extend(["a4",board[dikey+4][yatay-4]])
    
    if piece=="QU" and dict_all["QU"]=="f8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_QU.extend(["f7",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_QU.extend(["f6",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_QU.extend(["f5",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_QU.extend(["f4",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in black:
            valid_moves_for_QU.extend(["f3",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_QU.extend(["f2",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in combine and board[dikey+7][yatay] not in black:
            valid_moves_for_QU.extend(["f1",board[dikey+7][yatay]])   
        if board[dikey][yatay-1] not in black:
            valid_moves_for_QU.extend(["e8",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_QU.extend(["d8",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_QU.extend(["c8",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black:
            valid_moves_for_QU.extend(["b8",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in black:
            valid_moves_for_QU.extend(["a8",board[dikey][yatay-5]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_QU.extend(["h8",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black:
            valid_moves_for_QU.extend(["g8",board[dikey][yatay+1]])
        if board[dikey+1][yatay+1] not in black  :
            valid_moves_for_QU.extend(["g7", board[dikey+1][yatay+1]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_QU.extend(["h6",board[dikey+2][yatay+2]])
        if  board[dikey+1][yatay-1] not in black :
            valid_moves_for_QU.extend(["e7",board[dikey+1][yatay-1]])
        if  board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_QU.extend(["d6",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_QU.extend(["c5",board[dikey+3][yatay-3]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black:
            valid_moves_for_QU.extend(["b4",board[dikey+4][yatay-4]])
        if  board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black and board[dikey+5][yatay-5] not in black:
            valid_moves_for_QU.extend(["a3",board[dikey+5][yatay-5]])
    
    if piece=="QU" and dict_all["QU"]=="g8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_QU.extend(["g7",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_QU.extend(["g6",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_QU.extend(["g5",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_QU.extend(["g4",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in black:
            valid_moves_for_QU.extend(["g3",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_QU.extend(["g2",board[dikey+6][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in combine and board[dikey+7][yatay] not in black:
            valid_moves_for_QU.extend(["g1",board[dikey+7][yatay]])   
        if board[dikey][yatay-1] not in black:
            valid_moves_for_QU.extend(["f8",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_QU.extend(["e8",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_QU.extend(["d8",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black:
            valid_moves_for_QU.extend(["c8",board[dikey][yatay-4]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in black:
            valid_moves_for_QU.extend(["b8",board[dikey][yatay-5]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black and board[dikey][yatay-5] not in combine and board[dikey][yatay-6] not in black:
            valid_moves_for_QU.extend(["a8",board[dikey][yatay-6]])
        if board[dikey][yatay+1] not in black:
            valid_moves_for_QU.extend(["h8",board[dikey][yatay+1]])
        if board[dikey+1][yatay+1] not in black :
            valid_moves_for_QU.extend(["h7", board[dikey+1][yatay+1]])    
        if  board[dikey+1][yatay-1] not in black :
            valid_moves_for_QU.extend(["f7",board[dikey+1][yatay-1]])
        if  board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_QU.extend(["e6",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_QU.extend(["d5",board[dikey+3][yatay-3]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black:
            valid_moves_for_QU.extend(["c4",board[dikey+4][yatay-4]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black and board[dikey+5][yatay-5] not in black:
            valid_moves_for_QU.extend(["b3",board[dikey+5][yatay-5]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black and board[dikey+5][yatay-5] not in combine and board[dikey+6][yatay-6] not in black :
            valid_moves_for_QU.extend(["a2",board[dikey+6][yatay-6]])
    
    if piece=="QU" and dict_all["QU"]=="c7":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_QU.extend(["c6",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_QU.extend(["c5",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_QU.extend(["c4",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_QU.extend(["c3",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in combine and board[dikey+5][yatay] not in black:
            valid_moves_for_QU.extend(["c2",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_QU.extend(["c1",board[dikey+6][yatay]])
        if board[dikey-1][yatay] not in black:
            valid_moves_for_QU.extend(["c7",board[dikey-1][yatay]])   
        if board[dikey][yatay+1] not in black:
            valid_moves_for_QU.extend(["d7",board[dikey][yatay+1]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_QU.extend(["e7",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3] not in black:
            valid_moves_for_QU.extend(["f7",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black:
            valid_moves_for_QU.extend(["g7",board[dikey][yatay+4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black and board[dikey][yatay+4] not in black and board[dikey][yatay+5] not in black:
            valid_moves_for_QU.extend(["h7",board[dikey][yatay+5]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_QU.extend(["a7",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_QU.extend(["b7",board[dikey][yatay-1]])
        if board[dikey+1][yatay-1] not in black  :
            valid_moves_for_QU.extend(["b6", board[dikey+1][yatay-1]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_QU.extend(["a5",board[dikey+2][yatay-2]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_QU.extend(["d6",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_QU.extend(["e5",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_QU.extend(["f4",board[dikey+3][yatay+3]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black:
            valid_moves_for_QU.extend(["g3",board[dikey+4][yatay+4]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black and board[dikey+4][yatay+4] not in black and board[dikey+5][yatay+5] not in black:
            valid_moves_for_QU.extend(["h2",board[dikey+5][yatay+5]])
         
    if piece=="QU" and dict_all["QU"]=="e7":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_QU.extend(["e6",board[dikey+1][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black:
            valid_moves_for_QU.extend(["e5",board[dikey+2][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay] not in black:
            valid_moves_for_QU.extend(["e4",board[dikey+3][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black:
            valid_moves_for_QU.extend(["e3",board[dikey+4][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in combine and board[dikey+5][yatay] not in black:
            valid_moves_for_QU.extend(["e2",board[dikey+5][yatay]])
        if board[dikey+1][yatay] not in black and board[dikey+2][yatay] not in black and board[dikey+3][yatay]  not in black and board[dikey+4][yatay] not in black and board[dikey+5][yatay] not in combine and board[dikey+6][yatay] not in black:
            valid_moves_for_QU.extend(["e1",board[dikey+6][yatay]])
        if board[dikey-1][yatay] not in black :
            valid_moves_for_QU.extend(["e8",board[dikey+-1][yatay]])   
        if board[dikey][yatay-1] not in black:
            valid_moves_for_QU.extend(["d7",board[dikey][yatay-1]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black:
            valid_moves_for_QU.extend(["c7",board[dikey][yatay-2]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3] not in black:
            valid_moves_for_QU.extend(["b7",board[dikey][yatay-3]])
        if board[dikey][yatay-1] not in black and board[dikey][yatay-2] not in black and board[dikey][yatay-3]  not in black and board[dikey][yatay-4] not in black:
            valid_moves_for_QU.extend(["a7",board[dikey][yatay-4]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black and board[dikey][yatay+3]  not in black :
            valid_moves_for_QU.extend(["h7",board[dikey][yatay+3]])
        if board[dikey][yatay+1] not in black and board[dikey][yatay+2] not in black:
            valid_moves_for_QU.extend(["g7",board[dikey][yatay+2]])
        if board[dikey][yatay+1] not in black:
            valid_moves_for_QU.extend(["f7",board[dikey][yatay+1]])
        if  board[dikey+1][yatay+1] not in black :
            valid_moves_for_QU.extend(["f6",board[dikey+1][yatay+1]])
        if  board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black:
            valid_moves_for_QU.extend(["g5",board[dikey+2][yatay+2]])
        if board[dikey+1][yatay+1] not in black and board[dikey+2][yatay+2] not in black and board[dikey+3][yatay+3] not in black:
            valid_moves_for_QU.extend(["h4",board[dikey+3][yatay+3]])
        if  board[dikey+1][yatay-1] not in black :
            valid_moves_for_QU.extend(["d6",board[dikey+1][yatay-1]])
        if  board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black:
            valid_moves_for_QU.extend(["c5",board[dikey+2][yatay-2]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black:
            valid_moves_for_QU.extend(["b4",board[dikey+3][yatay-3]])
        if board[dikey+1][yatay-1] not in black and board[dikey+2][yatay-2] not in black and board[dikey+3][yatay-3] not in black and board[dikey+4][yatay-4] not in black:
            valid_moves_for_QU.extend(["a3",board[dikey+4][yatay-4]])
    
    if piece=="ki" and dict_all["ki"]=="e1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_ki.extend(["e2",board[dikey-1][yatay]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_ki.extend(["d1",board[dikey][yatay-1]])
        if board[dikey][yatay+1] not in white:
            valid_moves_for_ki.extend(["f1",board[dikey][yatay+1]])
        if board[dikey-1][yatay-1] not in white:
            valid_moves_for_ki.extend(["d2",board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in white:
            valid_moves_for_ki.extend(["f2",board[dikey-1][yatay+1]])
        
    if piece=="ki" and dict_all["ki"]=="d1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_ki.extend(["d2",board[dikey-1][yatay]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_ki.extend(["c1",board[dikey][yatay-1]])
        if board[dikey][yatay+1] not in white:
            valid_moves_for_ki.extend(["e1",board[dikey][yatay+1]])
        if board[dikey-1][yatay-1] not in white:
            valid_moves_for_ki.extend(["c2",board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in white:
            valid_moves_for_ki.extend(["e2",board[dikey-1][yatay+1]])
    
    if piece=="ki" and dict_all["ki"]=="f1":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_ki.extend(["f2",board[dikey-1][yatay]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_ki.extend(["e1",board[dikey][yatay-1]])
        if board[dikey][yatay+1] not in white:
            valid_moves_for_ki.extend(["g1",board[dikey][yatay+1]])
        if board[dikey-1][yatay-1] not in white:
            valid_moves_for_ki.extend(["e2",board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in white:
            valid_moves_for_ki.extend(["g2",board[dikey-1][yatay+1]])
    
    if piece=="ki" and dict_all["ki"]=="d2":
        if board[dikey+1][yatay] not in white:
            valid_moves_for_ki.extend(["d1",board[dikey+1][yatay]])
        if board[dikey-1][yatay] not in white:
            valid_moves_for_ki.extend(["d3",board[dikey-1][yatay]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_ki.extend(["c2",board[dikey][yatay-1]])
        if board[dikey][yatay+1] not in white:
            valid_moves_for_ki.extend(["e2",board[dikey][yatay+1]])
        if board[dikey-1][yatay-1] not in white:
            valid_moves_for_ki.extend(["c3",board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in white:
            valid_moves_for_ki.extend(["e3",board[dikey-1][yatay+1]])
        if board[dikey+1][yatay-1] not in white:
            valid_moves_for_ki.extend(["c1",board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in white:
            valid_moves_for_ki.extend(["e1",board[dikey+1][yatay+1]])
    
    if piece=="ki" and dict_all["ki"]=="f2":
        if board[dikey+1][yatay] not in white:
            valid_moves_for_ki.extend(["f1",board[dikey+1][yatay]])
        if board[dikey-1][yatay] not in white:
            valid_moves_for_ki.extend(["f3",board[dikey-1][yatay]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_ki.extend(["e2",board[dikey][yatay-1]])
        if board[dikey][yatay+1] not in white:
            valid_moves_for_ki.extend(["g2",board[dikey][yatay+1]])
        if board[dikey-1][yatay-1] not in white:
            valid_moves_for_ki.extend(["e3",board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in white:
            valid_moves_for_ki.extend(["g3",board[dikey-1][yatay+1]])
        if board[dikey+1][yatay-1] not in white:
            valid_moves_for_ki.extend(["e1",board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in white:
            valid_moves_for_ki.extend(["g1",board[dikey+1][yatay+1]])
    
    if piece=="ki" and dict_all["ki"]=="e2":
        if board[dikey+1][yatay] not in white:
            valid_moves_for_ki.extend(["e1",board[dikey+1][yatay]])
        if board[dikey-1][yatay] not in white:
            valid_moves_for_ki.extend(["e3",board[dikey-1][yatay]])
        if board[dikey][yatay-1] not in white:
            valid_moves_for_ki.extend(["d2",board[dikey][yatay-1]])
        if board[dikey][yatay+1] not in white:
            valid_moves_for_ki.extend(["f2",board[dikey][yatay+1]])
        if board[dikey-1][yatay-1] not in white:
            valid_moves_for_ki.extend(["d3",board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in white:
            valid_moves_for_ki.extend(["f3",board[dikey-1][yatay+1]])
        if board[dikey+1][yatay-1] not in white:
            valid_moves_for_ki.extend(["d1",board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in white:
            valid_moves_for_ki.extend(["f1",board[dikey+1][yatay+1]])
    
    if piece=="KI" and dict_all["KI"]=="e8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_KI.extend(["e7",board[dikey+1][yatay]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_KI.extend(["d8",board[dikey][yatay-1]])
        if board[dikey][yatay+1] not in black:
            valid_moves_for_KI.extend(["f8",board[dikey][yatay+1]])
        if board[dikey+1][yatay-1] not in black:
            valid_moves_for_KI.extend(["d7",board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in black:
            valid_moves_for_KI.extend(["f7",board[dikey+1][yatay+1]])
        
    if piece=="KI" and dict_all["KI"]=="d8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_KI.extend(["d7",board[dikey+1][yatay]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_KI.extend(["c8",board[dikey][yatay-1]])
        if board[dikey][yatay+1] not in black:
            valid_moves_for_KI.extend(["e8",board[dikey][yatay+1]])
        if board[dikey+1][yatay-1] not in black:
            valid_moves_for_KI.extend(["c7",board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in black:
            valid_moves_for_KI.extend(["e7",board[dikey+1][yatay+1]])
    
    if piece=="KI" and dict_all["KI"]=="f8":
        if board[dikey+1][yatay] not in black:
            valid_moves_for_KI.extend(["f7",board[dikey+1][yatay]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_KI.extend(["e8",board[dikey][yatay-1]])
        if board[dikey][yatay+1] not in black:
            valid_moves_for_KI.extend(["g8",board[dikey][yatay+1]])
        if board[dikey+1][yatay-1] not in black:
            valid_moves_for_KI.extend(["e7",board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in black:
            valid_moves_for_KI.extend(["g7",board[dikey+1][yatay+1]])
    
    if piece=="KI" and dict_all["KI"]=="d7":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_KI.extend(["d8",board[dikey-1][yatay]])
        if board[dikey+1][yatay] not in black:
            valid_moves_for_KI.extend(["d6",board[dikey+1][yatay]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_KI.extend(["c7",board[dikey][yatay-1]])
        if board[dikey][yatay+1] not in black:
            valid_moves_for_KI.extend(["e7",board[dikey][yatay+1]])
        if board[dikey+1][yatay-1] not in black:
            valid_moves_for_KI.extend(["c6",board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in black:
            valid_moves_for_KI.extend(["e6",board[dikey+1][yatay+1]])
        if board[dikey-1][yatay-1] not in black:
            valid_moves_for_KI.extend(["c8",board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in black:
            valid_moves_for_KI.extend(["e8",board[dikey-1][yatay+1]])
    
    if piece=="KI" and dict_all["KI"]=="f7":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_KI.extend(["f8",board[dikey-1][yatay]])
        if board[dikey+1][yatay] not in black:
            valid_moves_for_KI.extend(["f6",board[dikey+1][yatay]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_KI.extend(["e7",board[dikey][yatay-1]])
        if board[dikey][yatay+1] not in black:
            valid_moves_for_KI.extend(["g7",board[dikey][yatay+1]])
        if board[dikey+1][yatay-1] not in black:
            valid_moves_for_KI.extend(["e6",board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in black:
            valid_moves_for_KI.extend(["g6",board[dikey+1][yatay+1]])
        if board[dikey-1][yatay-1] not in black:
            valid_moves_for_KI.extend(["e8",board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in black:
            valid_moves_for_KI.extend(["g8",board[dikey-1][yatay+1]])
    
    if piece=="KI" and dict_all["KI"]=="e7":
        if board[dikey-1][yatay] not in white:
            valid_moves_for_KI.extend(["e8",board[dikey-1][yatay]])
        if board[dikey+1][yatay] not in black:
            valid_moves_for_KI.extend(["e6",board[dikey+1][yatay]])
        if board[dikey][yatay-1] not in black:
            valid_moves_for_KI.extend(["d7",board[dikey][yatay-1]])
        if board[dikey][yatay+1] not in black:
            valid_moves_for_KI.extend(["f7",board[dikey][yatay+1]])
        if board[dikey+1][yatay-1] not in black:
            valid_moves_for_KI.extend(["d6",board[dikey+1][yatay-1]])
        if board[dikey+1][yatay+1] not in black:
            valid_moves_for_KI.extend(["f6",board[dikey+1][yatay+1]])
        if board[dikey-1][yatay-1] not in black:
            valid_moves_for_KI.extend(["d8",board[dikey-1][yatay-1]])
        if board[dikey-1][yatay+1] not in black:
            valid_moves_for_KI.extend(["f8",board[dikey-1][yatay+1]])
ate=[]  
eat=[]
for i in commands:
    if i[0]=="move":
        for j in dict_all:
            if dict_all[j]==i[2]:
                if i[1] in white and j in black:
                    ate.append(j)
                    eat.append(i[1])
                    eat.append(i[2])
                if i[1] in black and j in white:
                    ate.append(j)
                    eat.append(i[1])
                    eat.append(i[2])
        if "ki" in ate:
            ate.remove("ki")
        if "KI" in ate:
            ate.remove("KI")
        print("> move",i[1]+" "+i[2])
        if i[2]==dict_all["ki"] or i[2]==dict_all["KI"]:
            print("FAILED")
            continue
        if i[1] in wp :
            finder(i[1])
            if valid_moves_for_wp[i[1]]==i[2] and board[dikey-1][yatay] not in white:
                print("OK")
                k = dikey
                if board[dikey-1][yatay] in black:
                    dct = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey-1][yatay]]
                    dict_all["S"+str(k)]=dct  
                    del dict_all[board[dikey-1][yatay]]
                    board[dikey][yatay]="S"+str(k)
                    board[dikey-1][yatay]=i[1]
                    valid_moves_for_wp[i[1]]=showmoves[showmoves.index(i[2])+1] 
                    
                else:
                    dct = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey-1][yatay]]
                    dict_all[board[dikey-1][yatay]]=dct
                    board[dikey][yatay]=board[dikey-1][yatay]
                    board[dikey-1][yatay]=i[1]
                    valid_moves_for_wp[i[1]]=showmoves[showmoves.index(i[2])+1]
            else: 
                print("FAILED")
            
        if i[1] in bp:
            finder(i[1])
            is_valid(i[1])
            if valid_moves_for_bp[i[1]]==i[2] and board[dikey+1][yatay] not in black:
                print("OK")
                k = dikey
                if board[dikey+1][yatay] in white:
                    dct1 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey+1][yatay]]
                    dict_all["L"+str(k)]=dct1  
                    del dict_all[board[dikey+1][yatay]]
                    board[dikey][yatay]="L"+str(k)
                    board[dikey+1][yatay]=i[1]
                    valid_moves_for_bp[i[1]]=showmoves[showmoves.index(i[2])-1]
                else:
                    dct1 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey+1][yatay]]
                    dict_all[board[dikey+1][yatay]]=dct1
                    board[dikey][yatay]=board[dikey+1][yatay]
                    board[dikey+1][yatay]=i[1]
                    valid_moves_for_bp[i[1]]=showmoves[showmoves.index(i[2])-1]
                   
            else: 
                print("FAILED")
           
        #================================================
        if i[1]=="b1":
            finder(i[1])
            is_valid(i[1])
            q,r=dikey,yatay
            if i[2] in valid_moves_for_b1 :
                    print("OK")
                    a = valid_moves_for_b1.index(i[2])
                    finder(valid_moves_for_b1[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="b1"  
            else:
                print("FAILED")
            valid_moves_for_b1=[]
            
            
        if i[1]=="b2":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_b2 :
                    print("OK")
                    a = valid_moves_for_b2.index(i[2])
                    finder(valid_moves_for_b2[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="b2"      
            else:
                print("FAILED")
            valid_moves_for_b2=[]
            
        
        if i[1]=="B1":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_B1 :
                    print("OK")
                    a = valid_moves_for_B1.index(i[2])
                    finder(valid_moves_for_B1[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="B1"      
            else:
                print("FAILED")
            valid_moves_for_B1=[]
            
        
        if i[1]=="B2":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_B2 :
                    print("OK")
                    a = valid_moves_for_B2.index(i[2])
                    finder(valid_moves_for_B2[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="B2"      
            else:
                print("FAILED")
            valid_moves_for_B2=[]
            
        
        if i[1]=="n1":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_n1  :
                    print("OK")
                    a = valid_moves_for_n1.index(i[2])
                    finder(valid_moves_for_n1[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="n1"      
            else:
                print("FAILED")
            valid_moves_for_n1=[]
            
        
        if i[1]=="n2":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_n2 :
                    print("OK")
                    a = valid_moves_for_n2.index(i[2])
                    finder(valid_moves_for_n2[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="n2"      
            else:
                print("FAILED")
            valid_moves_for_n2=[]
            
        
        if i[1]=="N1":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_N1 :
                    print("OK")
                    a = valid_moves_for_N1.index(i[2])
                    finder(valid_moves_for_N1[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="N1"      
            else:
                print("FAILED")
            valid_moves_for_N1=[]
            
        
        if i[1]=="N2":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_N2 :
                    print("OK")
                    a = valid_moves_for_N2.index(i[2])
                    finder(valid_moves_for_N2[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="N2"      
            else:
                print("FAILED")
            valid_moves_for_N2=[]
            
        
        
        if i[1]=="r1":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_r1 :
                    print("OK")
                    a = valid_moves_for_r1.index(i[2])
                    finder(valid_moves_for_r1[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="r1"      
            else:
                print("FAILED")
            valid_moves_for_r1=[]
            
        
        if i[1]=="r2":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_r2 :
                    print("OK")
                    a = valid_moves_for_r2.index(i[2])
                    finder(valid_moves_for_r2[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="r2"      
            else:
                print("FAILED")
            valid_moves_for_r2=[]
            
        
        if i[1]=="R1":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_R1 :
                    print("OK")
                    a = valid_moves_for_R1.index(i[2])
                    finder(valid_moves_for_R1[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="R1"      
            else:
                print("FAILED")
            valid_moves_for_R1=[]
            
        
        if i[1]=="R2":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_R2 :
                    print("OK")
                    a = valid_moves_for_R2.index(i[2])
                    finder(valid_moves_for_R2[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="R2"      
            else:
                print("FAILED")
            valid_moves_for_R2=[]
        
        if i[1]=="qu":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_qu :
                    print("OK")
                    a = valid_moves_for_qu.index(i[2])
                    finder(valid_moves_for_qu[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="qu"      
            else:
                print("FAILED")
            valid_moves_for_qu=[]
        
        if i[1]=="QU":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_QU :
                    print("OK")
                    a = valid_moves_for_QU.index(i[2])
                    finder(valid_moves_for_QU[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="QU"      
            else:
                print("FAILED")
            valid_moves_for_QU=[]
        
        if i[1]=="ki":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_ki :
                    print("OK")
                    a = valid_moves_for_ki.index(i[2])
                    finder(valid_moves_for_ki[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="ki"      
            else:
                print("FAILED")
            valid_moves_for_ki=[]
        
        if i[1]=="KI":
            finder(i[1])
            is_valid(i[1]) 
            q,r=dikey,yatay
            if i[2] in valid_moves_for_KI :
                    print("OK")
                    a = valid_moves_for_KI.index(i[2])
                    finder(valid_moves_for_KI[a+1])
                    dct3 = dict_all[i[1]]
                    dict_all[i[1]]=dict_all[board[dikey][yatay]]
                    dict_all[board[dikey][yatay]]=dct3
                    board[q][r]=board[dikey][yatay]
                    board[dikey][yatay]="KI"      
            else:
                print("FAILED")
            valid_moves_for_KI=[]
            
          
    if i[0]=="showmoves":
        finder(i[1])
        print("> showmoves "+i[1])
        if i[1] in wp :
            if i[1] in wp and board[dikey-1][yatay] not in white:
                print(valid_moves_for_wp[i[1]])
                valid_moves_for_wp= copy3
            else: 
                print("FAILED")
        if i[1] in bp:
            if i[1] in bp and board[dikey+1][yatay] not in black:
               print(valid_moves_for_bp[i[1]])  
               valid_moves_for_bp=copy4
            else:
                print("FAILED")
              
        #
        if i[1]=="b1":
            is_valid(i[1])
            if len(valid_moves_for_b1)>0:
                valid_moves_for_b1.sort()
                for i in valid_moves_for_b1:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_b1=[]
            else:
                print("FAILED")
        
        if i[1]=="b2":
            is_valid(i[1])
            if len(valid_moves_for_b2)>0:
                valid_moves_for_b2.sort()
                for i in valid_moves_for_b2:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_b2=[]
            else:
                print("FAILED")
        if i[1]=="B1":
            is_valid(i[1])
            if len(valid_moves_for_B1)>0:
                valid_moves_for_B1.sort()
                for i in valid_moves_for_B1:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_B1=[]
            else:
                print("FAILED")
        if i[1]=="B2":
            is_valid(i[1])
            if len(valid_moves_for_B2)>0:
                valid_moves_for_B2.sort()
                for i in valid_moves_for_B2:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_B2=[]
            else:
                print("FAILED")
        if i[1]=="n1":
            is_valid(i[1])
            if len(valid_moves_for_n1)>0:
                valid_moves_for_n1.sort()
                for i in valid_moves_for_n1:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_n1=[]
            else:
                print("FAILED")
        if i[1]=="n2":
            is_valid(i[1])
            if len(valid_moves_for_n2)>0:
                valid_moves_for_n2.sort()
                for i in valid_moves_for_n2:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_n2=[]
            else:
                print("FAILED")
        if i[1]=="N1":
            is_valid(i[1])
            if len(valid_moves_for_N1)>0:
                valid_moves_for_N1.sort()
                for i in valid_moves_for_N1:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_N1=[]
            else:
                print("FAILED")
        if i[1]=="N2":
            is_valid(i[1])
            if len(valid_moves_for_N2)>0:
                valid_moves_for_N2.sort()
                for i in valid_moves_for_N2:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_N2=[]
            else:
                print("FAILED")
        
        if i[1]=="r1":
            is_valid(i[1])
            if len(valid_moves_for_r1)>0:
                valid_moves_for_r1.sort()
                for i in valid_moves_for_r1:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_r1=[]
            else:
                print("FAILED")
        
        if i[1]=="r2":
            is_valid(i[1])
            if len(valid_moves_for_r2)>0:
                valid_moves_for_r2.sort()
                for i in valid_moves_for_r2:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_r2=[]
            else:
                print("FAILED")
        
        if i[1]=="R1":
            is_valid(i[1])
            if len(valid_moves_for_R1)>0:
                valid_moves_for_R1.sort()
                for i in valid_moves_for_R1:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_R1=[]
            else:
                print("FAILED")
        
        if i[1]=="R2":
            is_valid(i[1])
            if len(valid_moves_for_R2)>0:
                valid_moves_for_R2.sort()
                for i in valid_moves_for_R2:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_R2=[]
            else:
                print("FAILED")
        
        if i[1]=="qu":
            is_valid(i[1])
            if len(valid_moves_for_qu)>0:
                valid_moves_for_qu.sort()
                for i in valid_moves_for_qu:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_qu=[]
            else:
                print("FAILED")
        
        if i[1]=="QU":
            is_valid(i[1])
            if len(valid_moves_for_QU)>0:
                valid_moves_for_QU.sort()
                for i in valid_moves_for_QU:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_QU=[]
            else:
                print("FAILED")
        
        if i[1]=="ki":
            is_valid(i[1])
            if len(valid_moves_for_ki)>0:
                valid_moves_for_ki.sort()
                for i in valid_moves_for_ki:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_ki=[]
            else:
                print("FAILED")
        
        if i[1]=="KI":
            is_valid(i[1])
            if len(valid_moves_for_KI)>0:
                valid_moves_for_KI.sort()
                for i in valid_moves_for_KI:
                    if i in lst:
                        if i=="b1x":
                            print("b1",end=" ")
                        elif i=="b2x":
                            print("b2",end=" ")
                        else: print(i,end=" ")
                print()
                valid_moves_for_QU=[]
            else:
                print("FAILED")

    if i[0]=="print":
        print("> print")
        print("-----------------------")
        copy = [row[:] for row in board]
        for j in copy:
            for k in j:
                if k[0]=="X" or k[0]=="S" or  k[0]=="L" or  k[0]=="M" or k in ate:
                    a = j.index(k)
                    j[a]="  "  
            print(" ".join(j)) 
        print("-----------------------")    

    if i[0]=="initialize" :
        print("> initialize")
        ate = []
        valid_moves_for_wp={"p1":"a3","p2":"b3","p3":"c3","p4":"d3",
                    "p5":"e3","p6":"f3","p7":"g3","p8":"h3"}
        valid_moves_for_bp={"P1":"a6","P2":"b6","P3":"c6","P4":"d6",
                    "P5":"e6","P6":"f6","P7":"g6","P8":"h6"}
        valid_moves_for_b1=[]
        valid_moves_for_b2=[]
        valid_moves_for_B1=[]
        valid_moves_for_B2=[]
        valid_moves_for_n1=[]
        valid_moves_for_n2=[]
        valid_moves_for_N1=[]
        valid_moves_for_N2=[]
        valid_moves_for_r1=[]
        valid_moves_for_r2=[]
        valid_moves_for_R1=[]
        valid_moves_for_R2=[]
        valid_moves_for_qu=[]
        valid_moves_for_QU=[]
        valid_moves_for_ki=[]
        valid_moves_for_KI=[]
        dict_all={"r1":"a1","n1":"b1x","b1":"c1","qu":"d1","ki":"e1","b2":"f1","n2":"g1","r2":"h1",
          "p1":"a2","p2":"b2x","p3":"c2","p4":"d2","p5":"e2","p6":"f2","p7":"g2","p8":"h2",
          "XP":"a3","XR":"b3","XS":"c3","XT":"d3","XU":"e3","XV":"f3","XY":"g3","XZ":"h3",
          "XH":"a4","XI":"b4","XJ":"c4","XK":"d4","XL":"e4","XM":"f4","XN":"g4","XO":"h4",
          "X9":"a5","XA":"b5","XB":"c5","XC":"d5","XD":"e5","XE":"f5","XF":"g5","XG":"h5",
          "X1":"a6","X2":"b6","X3":"c6","X4":"d6","X5":"e6","X6":"f6","X7":"g6","X8":"h6",
          "P1":"a7","P2":"b7","P3":"c7","P4":"d7","P5":"e7","P6":"f7","P7":"g7","P8":"h7",
          "R1":"a8","N1":"b8","B1":"c8","QU":"d8","KI":"e8","B2":"f8","N2":"g8","R2":"h8"}
        print("-----------------------")
        board = [row[:] for row in copy2]
        for j in copy2:
            for k in j:
                if k[0]=="X":
                    a = j.index(k)
                    j[a]="  "  
            print(" ".join(j))
        print("-----------------------")

    if i[0]=="exit":
        print("> exit")
        sys.exit()
        
