import random
def value(data,x,y,color):
    length = len(data)
    x = x+3
    y = y+3

    #扩大棋盘
    newdata = []
    for i in range(length+8):
        d = []
        for j in range(length+8):
            d.append(0)
        newdata.append(d)
    for i in range(length):
        for j in range(length):
            newdata[i+4][j+4] = data[i][j]
    data = newdata
    c= color
    if c == 1:
        d = 2
    else:
        d = 1
    state = [[c,c,c,c],[c,c,c,0],[0,c,c,c],[c,c,c,d],[c,c,0,0],[0,c,c,0],[0,0,c,c],[c,c,0,d],[c,c,d,d],[0,c,c,d],[c,0,0,0]]
    val = [100,90,90,80,60,60,60,50,30,30,10]
    dire = [
        [data[x-1][y],data[x-2][y],data[x-3][y],data[x-4][y]],#left
        [data[x-1][y-1],data[x-2][y-2],data[x-3][y-3],data[x-4][y-5]],#left_up
        [data[x][y-1],data[x][y-2],data[x][y-3],data[x][y-4]],#up
        [data[x+1][y-1],data[x+2][y-2],data[x+3][y-3],data[x+4][y-4]],#right_up
        [data[x+1][y],data[x+2][y],data[x+3][y],data[x+4][y]],#right
        [data[x+1][y+1],data[x+2][y+2],data[x+3][y+3],data[x+4][y+4]],#right_down
        [data[x][y+1],data[x][y+2],data[x][y+3],data[x][y+4]],#down
        [data[x-1][y+1],data[x-2][y+2],data[x-3][y+3],data[x-4][y+4]],#left_down
    ]
    value = 0
    for i in range(8):
        if dire[i] in state:
            value += val[state.index(dire[i])]
        else:
            value += 0
    return value

def loca(data,color):
    void =[]
    s = 0
    for i in range(len(data)):
        v = []
        for j in range(len(data)):
            if data[i][j] == 0:
                v.append(1)
            else:
                v.append(0)
            s += data[i][j]
        void.append(v)
    val = 0
    v_loca = [0,0]
    if s > 2:
        for i in range(len(void)):
            for j in range(len(void)):
                if void[i][j]:
                    k = value(data,j+1,i+1,color)
                    if k>val:
                        val = k
                        v_loca = [j+1,i+1]
    else:
        v_loca = [int(random.random()*len(data)),int(random.random()*len(data))]
    return v_loca

if __name__ == "__main__":
    data = [
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
    ]
    print(loca(data,1))