import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer,QThread,pyqtSignal,pyqtSlot

# import Opencv module
import cv2
import time
a = 0
K =0
temp_cam = 0
from CameraGUI import *
class ControlThread(QThread):
    #步态控制子线程
    signal = pyqtSignal(str)
    global a
    K = a
    print(K)
    def run(self):
        # if signal == 1:
        global K
        global a
        K = a
        #全局变量传递控制值
        #K  ——1：同步 2：交错 3：左转 4：右转 5：步行前进
        # for i in range (1,10):
        #     print("first mode:")
        #     print("hello ")
        #     time.sleep(0.1)
        if K == 2:
            for i in range (1,50):
                print("Second mode:")
                print("hello ")
                time.sleep(0.1)
        if K == 1:
            for i in range (1,50):
                print("Third mode:")
                print("hello ")
                time.sleep(0.1)
        if K == 3:
            for i in range (1,50):
                print("Third mode:")
                print("hello ")
                time.sleep(0.1)
        if K == 4:
            for i in range (1,50):
                print("Third mode:")
                print("hello ")
                time.sleep(0.1)
        K =0

    def stop(self):
        # 关闭摄像头
        self.terminate()
        self.quit()
        self.exit()
        self.stopped = True
        self.terminated = True

class Thread(QThread):
    # a signal called "changePixmap" that take an argument QImage
    # QImage is an image representation that allows direct access to pixel data
    changePixmap = pyqtSignal(QImage)

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                #ret, image = cap.read()
                # convert image to RGB format
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # get image infos
                height, width, channel = image.shape
                step = channel * width
                # create QImage from image
                qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
                # show image in img_label
                #self.ui.CamLB.setPixmap(QPixmap.fromImage(qImg))
                self.changePixmap.emit(qImg)

    def stop(self):
        # 关闭摄像头
        self.terminate()
        self.quit()
        self.exit()
        self.stopped = True
        self.terminated = True
#class
class MainWindow(QWidget):

    @pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        self.ui.CamLB.setPixmap(QtGui.QPixmap.fromImage(image))


    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # create a timer
        #self.timer = QTimer()
        # set timer timeout callback function
        #self.timer.timeout.connect(self.viewCam)
        self.ui.OpenCamBT.clicked.connect(self.controlTimer)
        self.ui.ForwardBT.clicked.connect(self.move_forward)
        self.ui.BackwardBT.clicked.connect(self.move_backward)
        self.ui.GetherBT.clicked.connect(self.swim_gether)
        self.ui.CrossBT.clicked.connect(self.swim_cross)
        self.ui.LeftBT.clicked.connect(self.swim_left)
        self.ui.RightBT.clicked.connect(self.swim_right)
        self.ui.ResetBT.clicked.connect(self.reset)
        # th = Thread(self)
        # # signal is connected to a slot using .connect()
        # th.changePixmap.connect(self.setImage)
        self.th =Thread()
        self.th.changePixmap.connect(self.setImage)
        # th.start()
        #默认开启摄像头
        self.Ctrlthread = ControlThread()

#摄像头开关函数
    def controlTimer(self):
        global temp_cam

        print(temp_cam)
        #global th
        if temp_cam == 1:
            self.ui.OpenCamBT.setText("关闭摄像头")

            self.th.start()
            temp_cam = 0
        elif temp_cam == 0 :
            self.ui.OpenCamBT.setText("打开摄像头")
            try:
                self.th.stop()
                #self.ui.CamLB.setPixmap(0)
            except:
                pass
            temp_cam = 1

#按钮响应函数，点击后开启子线程进入步态PWM赋值
    # 全局变量传递控制值
    # K  ——1：同步 2：交错 3：左转 4：右转 5：步行前进
            ##1同步2交错3左4右
    def move_forward(self):
        print("move_forward")
        global a
        a = 5
        self.Ctrlthread.start()
    def move_backward(self):
        print("move_backward")



    def swim_gether(self):
        print("swim_gether")

        global a
        a = 1
        self.Ctrlthread.start()
        #TongBu_swim(key_List)
        #key_List = [1, 0, 0, 0]
    def swim_cross(self):
        print("swim_cross")
        global a
        a  = 2
        #key_List = [0,1,0,0]
        self.Ctrlthread.start()
    def swim_left(self):
        print("swim_left")
        global a
        a  = 3
        self.Ctrlthread.start()
    def swim_right(self):
        print("swim_right")
        global a
        a  = 4#右转
        self.Ctrlthread.start()
    def reset(self):
        print("reset")
        self.Ctrlthread.stop()
        print("all stop")
        print("return Zero")









if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())