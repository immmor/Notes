import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton

class DemoWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.init_ui()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('PyQt6 Demo')
        button = QPushButton('显示消息框', self)
        button.setGeometry(100, 80, 100, 30)
        button.clicked.connect(self.show_message_box)

    # def init_ui(self):
    #     self.setGeometry(100, 100, 300, 200)
    #     self.setWindowTitle('PyQt6 Demo')
    #     button = QPushButton('显示消息框', self)
    #     button.setGeometry(100, 80, 100, 30)
    #     button.clicked.connect(self.show_message_box)

    def show_message_box(self):
        QMessageBox.information(self, '消息', "Hello, How's life there!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoWindow()
    window.show()
    sys.exit(app.exec())
