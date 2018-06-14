from pyfirmate import Arduino,util  #首先需要安装pyfirmate 
import time

class CameraControl():
	def __init__(self, keep_time, wait_time):
	self.c1 = 10                    
    self.c2 = 11
    self.c3 = 12
	self.keep_time = keep_time
    self.wait_time = wait_time
	board = Arduino('COM6')   #Arduino 所在串口
	
	def shoot(self) :
        board.digital[self.c3].write(0)
        time.sleep(self.keep_time)

        board.digital[self.c3].write(1)
        time.sleep(self.wait_time)

    def connect(self) :
        board.digital[self.c2].write(0)
        time.sleep(3)
        board.digital[self.c2].write(1)

    def power_on(self) :
        board.digital[self.c1].write(1)
        board.digital[self.c2].write(1)
        board.digital[self.c3].write(1)


    def power_off(self):
        board.digital[self.c1].write(0)
        time.sleep(0.01)
        board.digital[self.c1].write(1)