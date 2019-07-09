import random
import re
import ai

#输入棋盘二维数组信息：0无棋，1黑棋，2白棋
def draw(data):
    if len(data) == 0 or len(data)!=len(data[0]):
        print("[Error]Length of data error!")
    else:
        print("    1 2 3 4 5 6 7 8 9 A B C D E F")
        print("   "+"-"*(len(data)*2+1))
        for i in range(len(data)):
            if i+1<10:
                c = "0"+str(i+1)
            else:
                c = str(i+1)
            text = c+"|"
            for j in range(len(data)):
                if data[i][j] == 0:
                    text += " ·"
                elif data[i][j] == 1:
                    text += " ○"
                else:
                    text += " ●"
            text += " |" 
            print(text)
        print("   "+"-"*(len(data)*2+1))

def point(data,x,y,type):
    data[y-1][x-1]=type
    return data

def void_2dArray(length):
    data = []
    for i in range(length):
        d = []
        for j in range(length):
            d.append(0)
        data.append(d)
    return data

def verify(data,type):
    length = len(data)-3
    state = 0
    for i in range(2,length):
        for j in range(2,length):
            if data[i][j]==type:
                if data[i][j-2] == type and data[i][j-1] == type and data[i][j+1] == type and data[i][j+2] == type: 
                    state = 1
                elif data[i-2][j] == type and data[i-1][j] == type and data[i+1][j] == type and data[i+2][j] == type: 
                    state = 1
                elif data[i-2][j-2] == type and data[i-1][j-1] == type and data[i+1][j+1] == type and data[i+2][j+2] == type: 
                    state = 1
                elif data[i+2][j-2] == type and data[i+1][j-1] == type and data[i-1][j+1] == type and data[i-2][j+2] == type: 
                    state = 1
                else:
                    state = 0
            if state:
                return 1
    return 0

def overturn(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == 1:
                data[i][j] = 2
            elif data[i][j] == 2:
                data[i][j] = 1
            else:
                None
    return data

if __name__ == "__main__":
    frist = input("Who frist(Black)?[1.You 2.Computer]")
    if frist == "1":
        mode = "hm"
        type = {"hm":1,"ai":2}
    else:
        mode = "ai"
        type = {"hm":2,"ai":1}
    
    step = 0
    data = void_2dArray(15)
    while step<=15*15:
        draw(data)
        if mode == "hm":
            input1 = input("Input your flag location(x,y):")
            r = re.compile(r"(\d+),(\d+)")
            x = int(r.findall(input1)[0][0])
            y = int(r.findall(input1)[0][1])
            data = point(data,x,y,type["hm"])
            if verify(data,type["hm"]):
                draw(data)
                print("Human Win!")
                break
            else:
                mode = "ai"
        if mode == "ai":
            loca = ai.loca(data,type["ai"])
            data = point(data,loca[0],loca[1],type["ai"])
            if verify(data,type["ai"]):
                draw(data)
                print("AI Win")
                break
            else:
                mode = "hm"