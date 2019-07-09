import Renju
import ai

def train():
    data = Renju.void_2dArray(15)
    step = 0
    mode = 1
    while step<=15*15:
        Renju.draw(data)
        if mode == 1:
            loca = ai.loca(data,1)
            data = Renju.point(data,loca[0],loca[1],1)
            #print(loca)
            if Renju.verify(data,1):
                Renju.draw(data)
                print("AI1 Win")
                break
            else:
                mode = 2
                step += 1
        if mode == 2:
            loca = ai.loca(data,2)
            data = Renju.point(data,loca[0],loca[1],2)
            #print(loca)
            if Renju.verify(data,2):
                Renju.draw(data)
                print("AI2 Win")
                break
            else:
                mode = 1
                step += 1

if __name__ == "__main__":
    train()