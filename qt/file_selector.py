import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel


class FileSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题和布局
        self.setWindowTitle('文件加密解密器')
        layout = QVBoxLayout()

        # 创建按钮和标签
        self.button = QPushButton('选择文件', self)
        self.button.clicked.connect(self.select_file)
        layout.addWidget(self.button)

        self.label = QLabel('未选择文件', self)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def select_file(self):
        # 打开文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(self, '选择文件', '', '所有文件 (*)')
        if file_path:
            self.label.setText(f'文件路径: {file_path}')
        else:
            self.label.setText('未选择文件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileSelector()
    window.resize(600, 500)
    window.show()
    sys.exit(app.exec())
