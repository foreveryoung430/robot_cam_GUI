import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer,QThread

# import Opencv module
import cv2


from CameraGUI import *

class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        self.ui.OpenCamBT.clicked.connect(self.controlTimer)
        self.ui.ForwardBT.clicked.connect(self.move_forward)
        self.ui.BackwardBT.clicked.connect(self.move_backward)
        self.ui.GetherBT.clicked.connect(self.swim_gether)
        self.ui.CrossBT.clicked.connect(self.swim_cross)
        self.ui.LeftBT.clicked.connect(self.swim_left)
        self.ui.RightBT.clicked.connect(self.swim_right)
        self.ui.ResetBT.clicked.connect(self.reset)

        # start/stop timer
    def controlTimer(self):
            # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)                # start timer
            self.timer.start(20)
                # update OpenCamBT text
            self.ui.OpenCamBT.setText("关闭摄像头")
            # if timer is started
        else:
                # stop timer
            self.timer.stop()
                # release video capture
            self.cap.release()
                # update OpenCamBT text

            self.ui.OpenCamBT.setText("打开摄像头")

                # view camera
    def viewCam(self):
                    # read image in BGR format
        ret, image = self.cap.read()
                    # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    # get image infos
        height, width, channel = image.shape
        step = channel * width
                    # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
                    # show image in img_label
        self.ui.CamLB.setPixmap(QPixmap.fromImage(qImg))

            ##1同步2交错3左4右
    def move_forward(self):
        print("move_forward")
    def move_backward(self):
        print("move_backward")

    def swim_gether(self):
        print("swim_gether")
        ##两个if
        #第一个IF判断是否第一个
        #第二个IF判断上一个是什么

        #TongBu_swim(key_List)
        #key_List = [1, 0, 0, 0]
    def swim_cross(self):
        print("swim_cross")
        key_List = [0,1,0,0]

    def swim_left(self):
        print("swim_left")
    def swim_right(self):
        print("swim_right")
    def reset(self):
        print("reset")







if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())