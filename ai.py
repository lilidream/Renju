import random
def value(data,x,y,color):
    length = len(data)
    x = x+4
    y = y+4

    #扩大棋盘
    newdata = []
    for i in range(length+10):
        d = []
        for j in range(length+10):
            d.append(0)
        newdata.append(d)
    for i in range(length):
        for j in range(length):
            newdata[i+5][j+5] = data[i][j]
    data = newdata
    c= color
    if c == 1:
        d = 2
    else:
        d = 1
    state = [
        [d,d,d,d,0],[d,d,d,d,c],[d,d,d,0,0],[d,d,d,c,0],[d,d,d,c,c],[d,d,0,0,0],[d,d,0,0,c],[d,d,0,c,c],[d,0,d,0,c],[d,0,d,0,0],[d,0,0,d,0],[d,0,0,d,c],
        [c,c,c,c,0],[c,c,c,c,d],[c,c,c,d,d],[c,c,c,0,d],[c,0,c,c,0],[c,0,c,c,d],[c,c,0,c,0],[c,c,0,c,d],[c,c,0,0,d],[c,c,0,d,d]
    ]
    val = [100,100,100,90,90,70,70,50,50,30,30,30,100,100,90,90,80,80,60,60,30,30]
    dire = [
        [data[x-1][y],data[x-2][y],data[x-3][y],data[x-4][y],data[x-5][y]],#left
        [data[x-1][y-1],data[x-2][y-2],data[x-3][y-3],data[x-4][y-4],data[x-4][y-4]],#left_up
        [data[x][y-1],data[x][y-2],data[x][y-3],data[x][y-4],data[x][y-4]],#up
        [data[x+1][y-1],data[x+2][y-2],data[x+3][y-3],data[x+4][y-4],data[x+4][y-4]],#right_up
        [data[x+1][y],data[x+2][y],data[x+3][y],data[x+4][y],data[x+5][y]],#right
        [data[x+1][y+1],data[x+2][y+2],data[x+3][y+3],data[x+4][y+4],data[x+5][y+5]],#right_down
        [data[x][y+1],data[x][y+2],data[x][y+3],data[x][y+4],data[x][y+5]],#down
        [data[x-1][y+1],data[x-2][y+2],data[x-3][y+3],data[x-4][y+4],data[x-5][y+5]],#left_down
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
    v_loca = [-1,-1]
    if s > 2:
        for i in range(len(void)):
            for j in range(len(void)):
                if void[i][j]:
                    k = value(data,j+1,i+1,color)
                    if k>val:
                        val = k
                        v_loca = [j+1,i+1]
        if v_loca == [-1,-1]:
            while True:
                v_loca = [int(random.random()*len(data)),int(random.random()*len(data))]
                if void[v_loca[0]][v_loca[1]]:
                    break

    else:
        v_loca = [int(random.random()*len(data)),int(random.random()*len(data))]
    return v_loca

if __name__ == "__main__":
    data = [
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,2,2,2,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
    ]
    print(loca(data,1))