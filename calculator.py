
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication, QTextEdit)
from PyQt5.QtCore import QThread, pyqtSignal, QMutex


class Thread(QThread):

    finished_signal = pyqtSignal(str)  # 括号里填写信号传递的参数
    lst = []

    def __init__(self):
        super(Thread, self).__init__()
        self.mutex = QMutex()

    def run(self):
        self.mutex.lock()
        self.k = ""
        for i in self.lst:
            self.k += str(i)
        self.result = str(eval(self.k))
        self.mutex.unlock()
        self.finished_signal.emit(self.result)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        # self.initUI()
        grid = QGridLayout()
        self.setLayout(grid)
        self.thread = Thread()

        self.names = ['AC', 'Bcksapce', '%', 'Close',
                      '7', '8', '9', '/',
                      '4', '5', '6', '*',
                      '1', '2', '3', '-',
                      '0', '.', '=', '+']
        self.button_mult = QPushButton(self.names[11])
        grid.addWidget(self.button_mult, 20, 30, 10, 10)
        self.button_mult.clicked.connect(self.multiplication)
        self.button_subt = QPushButton(self.names[15])
        grid.addWidget(self.button_subt, 30, 30, 10, 10)
        self.button_subt.clicked.connect(self.subtraction)
        self.button_add = QPushButton(self.names[19])
        grid.addWidget(self.button_add, 40, 30, 10, 10)
        self.button_add.clicked.connect(self.addition)
        self.button_dividi = QPushButton(self.names[7])
        grid.addWidget(self.button_dividi, 10, 30, 10, 10)
        self.button_dividi.clicked.connect(self.divide)
        self.button_equal = QPushButton(self.names[18])
        grid.addWidget(self.button_equal, 40, 20, 10, 10)
        self.button_equal.clicked.connect(self.equal)
        self.buttonAC = QPushButton(self.names[0])
        grid.addWidget(self.buttonAC, 0, 0, 10, 10)
        self.buttonAC.clicked.connect(self.clear)
        self.button_Bcksapce = QPushButton(self.names[1])
        grid.addWidget(self.button_Bcksapce, 0, 10, 10, 10)
        self.button_Bcksapce.clicked.connect(self.Bcksapce)
        self.button_percent = QPushButton(self.names[2])
        grid.addWidget(self.button_percent, 0, 20, 10, 10)
        self.button_percent.clicked.connect(self.percent)
        self.button_close = QPushButton(self.names[3])
        grid.addWidget(self.button_close, 0, 30, 10, 10)
        self.button_close.clicked.connect(self.close)
        self.button_dot = QPushButton(self.names[17])
        grid.addWidget(self.button_dot, 40, 10, 10, 10)
        self.button_dot.clicked.connect(self.dot)
        self.button7 = QPushButton(self.names[4])
        grid.addWidget(self.button7, 10, 0, 10, 10)
        self.button7.clicked.connect(self.buttonClicked_num)
        self.button8 = QPushButton(self.names[5])
        grid.addWidget(self.button8, 10, 10, 10, 10)
        self.button8.clicked.connect(self.buttonClicked_num)
        self.button9 = QPushButton(self.names[6])
        grid.addWidget(self.button9, 10, 20, 10, 10)
        self.button9.clicked.connect(self.buttonClicked_num)
        self.button4 = QPushButton(self.names[8])
        grid.addWidget(self.button4, 20, 0, 10, 10)
        self.button4.clicked.connect(self.buttonClicked_num)
        self.button5 = QPushButton(self.names[9])
        grid.addWidget(self.button5, 20, 10, 10, 10)
        self.button5.clicked.connect(self.buttonClicked_num)
        self.button6 = QPushButton(self.names[10])
        grid.addWidget(self.button6, 20, 20, 10, 10)
        self.button6.clicked.connect(self.buttonClicked_num)
        self.button1 = QPushButton(self.names[12])
        grid.addWidget(self.button1, 30, 0, 10, 10)
        self.button1.clicked.connect(self.buttonClicked_num)
        self.button2 = QPushButton(self.names[13])
        grid.addWidget(self.button2, 30, 10, 10, 10)
        self.button2.clicked.connect(self.buttonClicked_num)
        self.button3 = QPushButton(self.names[14])
        grid.addWidget(self.button3, 30, 20, 10, 10)
        self.button3.clicked.connect(self.buttonClicked_num)
        self.button0 = QPushButton(self.names[16])
        grid.addWidget(self.button0, 40, 0, 10, 10)
        self.button0.clicked.connect(self.buttonClicked_num)
        self.txt1 = QTextEdit(self)
        grid.addWidget(self.txt1, 50, 0, 10, 40)
        self.setGeometry(30, 30, 200, 400)
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

    def buttonClicked_num(self):
        # 获取发送信号的按钮
        sender = self.sender()
        # 在状态栏显示按钮的文本信息
        self.txt1.append(sender.text())
        shu = int(sender.text())
        self.thread.lst.append(shu)

    def clear(self):
        self.txt1.clear()

    def addition(self):
        sender = self.sender()
        self.txt1.append(sender.text())
        jia = str(sender.text())
        self.thread.lst.append(jia)

    def equal(self):
        self.thread.finished_signal.connect(self.result1)
        self.thread.start()

    def result1(self):
        self.txt1.setText(self.thread.result)

    def subtraction(self):
        sender = self.sender()
        self.txt1.append(sender.text())
        jian = str(sender.text())
        self.thread.lst.append(jian)

    def multiplication(self):
        sender = self.sender()
        self.txt1.append(sender.text())
        cheng = str(sender.text())
        self.thread.lst.append(cheng)

    def divide(self):
        sender = self.sender()
        self.txt1.append(sender.text())
        chu = str(sender.text())
        self.thread.lst.append(chu)

    def percent(self):
        sender = self.sender()
        self.txt1.append(sender.text())
        bai_fen = str(sender.text())
        self.thread.lst.append(bai_fen)

    def dot(self):
        sender = self.sender()
        self.txt1.append(sender.text())
        dian = str(sender.text())
        self.thread.lst.append(dian)

    def close(self):
        QApplication.quit()

    def Bcksapce(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
