from Magic8Ball_OBJ import magic8Ball
from time import sleep

if __name__ == "__main__":
    myBall = magic8Ball()
    myBall.resetBall()
    sleep(2)
    myBall.generateResponse()
    print('\n\n')