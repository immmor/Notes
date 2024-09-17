import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel, QDesktopWidget
from PyQt5.QtCore import Qt, pyqtSlot, QTranslator, QCoreApplication
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQtNotes'
        self.width = 700
        self.height = 500
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        # 设置窗口无边框
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)


        # 设置窗口图标
        icon_path = os.path.join('..', '..', 'Statics', 'Image', 'notes.png')
        self.setWindowIcon(QIcon(icon_path))

        # 设置样式
        self.setStyleSheet("""
            QWidget {
                border-radius: 100px;
                background-color: lightblue;
            }
            QPushButton {
                padding: 10px;
                background-color: lightgreen;
                border-radius: 10px;
                font-size: 16px;
                max-width: 200px;  /* 设置最大宽度 */
                min-width: 100px;  /* 设置最小宽度 */
                min-height: 40px;  /* 设置最小高度 */
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """)
        
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        
        self.label = QLabel('欢迎使用PyQt5Notes!', self)
        vLayout.addWidget(self.label)
        

        
        button = QPushButton('点击我', self)
        button.clicked.connect(self.on_click)
        hLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # vLayout.addWidget(button)
        hLayout.addWidget(button)
        vLayout.addLayout(hLayout)
        
        self.setLayout(vLayout)
        
        self.center()
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    @pyqtSlot()
    def on_click(self):
        self.label.setText('你好! 你点击了按钮。')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())