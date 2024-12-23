# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\encryption.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(700, 611)
        self.verticalLayoutWidget = QtWidgets.QWidget(widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 701, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.encryption = QtWidgets.QVBoxLayout()
        self.encryption.setObjectName("encryption")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.encryption_input_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.encryption_input_label.setAlignment(QtCore.Qt.AlignCenter)
        self.encryption_input_label.setObjectName("encryption_input_label")
        self.verticalLayout_2.addWidget(self.encryption_input_label)
        self.encryption_input = QtWidgets.QHBoxLayout()
        self.encryption_input.setObjectName("encryption_input")
        self.encryption_input_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.encryption_input_lineEdit.setObjectName("encryption_input_lineEdit")
        self.encryption_input.addWidget(self.encryption_input_lineEdit)
        self.encryption_input_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.encryption_input_button.setObjectName("encryption_input_button")
        self.encryption_input.addWidget(self.encryption_input_button)
        self.encryption_input.setStretch(0, 2)
        self.encryption_input.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.encryption_input)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 4)
        self.encryption.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.encryption.addItem(spacerItem)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.encryption_output_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.encryption_output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.encryption_output_label.setObjectName("encryption_output_label")
        self.verticalLayout_6.addWidget(self.encryption_output_label)
        self.encryption_output = QtWidgets.QHBoxLayout()
        self.encryption_output.setObjectName("encryption_output")
        self.encrytion_output_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.encrytion_output_lineEdit.setObjectName("encrytion_output_lineEdit")
        self.encryption_output.addWidget(self.encrytion_output_lineEdit)
        self.encryption_output_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.encryption_output_button.setObjectName("encryption_output_button")
        self.encryption_output.addWidget(self.encryption_output_button)
        self.encryption_output.setStretch(0, 2)
        self.encryption_output.setStretch(1, 1)
        self.verticalLayout_6.addLayout(self.encryption_output)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 4)
        self.encryption.addLayout(self.verticalLayout_6)
        self.encryption_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.encryption_button.setObjectName("encryption_button")
        self.encryption.addWidget(self.encryption_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.encryption.addItem(spacerItem1)
        self.encryption.setStretch(0, 3)
        self.encryption.setStretch(1, 4)
        self.encryption.setStretch(2, 3)
        self.encryption.setStretch(3, 1)
        self.encryption.setStretch(4, 3)
        self.horizontalLayout.addLayout(self.encryption)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.decryption = QtWidgets.QVBoxLayout()
        self.decryption.setObjectName("decryption")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.decryption_input_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.decryption_input_label.setAlignment(QtCore.Qt.AlignCenter)
        self.decryption_input_label.setObjectName("decryption_input_label")
        self.verticalLayout_8.addWidget(self.decryption_input_label)
        self.decryption_input = QtWidgets.QHBoxLayout()
        self.decryption_input.setObjectName("decryption_input")
        self.decryption_input_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.decryption_input_lineEdit.setObjectName("decryption_input_lineEdit")
        self.decryption_input.addWidget(self.decryption_input_lineEdit)
        self.decryption_input_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.decryption_input_button.setObjectName("decryption_input_button")
        self.decryption_input.addWidget(self.decryption_input_button)
        self.decryption_input.setStretch(0, 2)
        self.decryption_input.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.decryption_input)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 4)
        self.decryption.addLayout(self.verticalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.decryption.addItem(spacerItem3)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.decryption_output_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.decryption_output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.decryption_output_label.setObjectName("decryption_output_label")
        self.verticalLayout_9.addWidget(self.decryption_output_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.decryption_output_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.decryption_output_lineEdit.setObjectName("decryption_output_lineEdit")
        self.horizontalLayout_2.addWidget(self.decryption_output_lineEdit)
        self.decryption_output_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.decryption_output_button.setObjectName("decryption_output_button")
        self.horizontalLayout_2.addWidget(self.decryption_output_button)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.decryption_filename_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.decryption_filename_lineEdit.setObjectName("decryption_filename_lineEdit")
        self.horizontalLayout_3.addWidget(self.decryption_filename_lineEdit)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.decryption_file_selector = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.decryption_file_selector.setObjectName("decryption_file_selector")
        self.decryption_file_selector.addItem("")
        self.decryption_file_selector.addItem("")
        self.decryption_file_selector.addItem("")
        self.decryption_file_selector.addItem("")
        self.decryption_file_selector.addItem("")
        self.decryption_file_selector.addItem("")
        self.decryption_file_selector.addItem("")
        self.horizontalLayout_3.addWidget(self.decryption_file_selector)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 4)
        self.verticalLayout_9.setStretch(2, 1)
        self.decryption.addLayout(self.verticalLayout_9)
        self.decryption_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.decryption_button.setObjectName("decryption_button")
        self.decryption.addWidget(self.decryption_button)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.decryption.addItem(spacerItem4)
        self.decryption.setStretch(0, 3)
        self.decryption.setStretch(1, 4)
        self.decryption.setStretch(2, 3)
        self.decryption.setStretch(3, 1)
        self.decryption.setStretch(4, 3)
        self.horizontalLayout.addLayout(self.decryption)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.log = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy)
        self.log.setMinimumSize(QtCore.QSize(0, 12))
        self.log.setMaximumSize(QtCore.QSize(16777215, 36))
        self.log.setObjectName("log")
        self.verticalLayout.addWidget(self.log)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 1)
        self.encryption_input_button.clicked.connect(self.select_file)
        self.retranslateUi(widget)

        QtCore.QMetaObject.connectSlotsByName(widget)


    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "文件加密解密器"))
        self.label.setText(_translate("widget", "欢迎使用文件加密器"))
        self.encryption_input_label.setText(_translate("widget", "选择加密文件"))
        self.encryption_input_button.setText(_translate("widget", "选择文件"))
        self.encryption_output_label.setText(_translate("widget", "选择输出地址"))
        self.encryption_output_button.setText(_translate("widget", "选择文件"))
        self.encryption_button.setText(_translate("widget", "加密"))
        self.decryption_input_label.setText(_translate("widget", "选择解密文件"))
        self.decryption_input_button.setText(_translate("widget", "选择文件"))
        self.decryption_output_label.setText(_translate("widget", "选择输出路径"))
        self.decryption_output_button.setText(_translate("widget", "输出地址"))
        self.label_3.setText(_translate("widget", "."))
        self.decryption_file_selector.setItemText(0, _translate("widget", "txt"))
        self.decryption_file_selector.setItemText(1, _translate("widget", "docx"))
        self.decryption_file_selector.setItemText(2, _translate("widget", "doc"))
        self.decryption_file_selector.setItemText(3, _translate("widget", "pptx"))
        self.decryption_file_selector.setItemText(4, _translate("widget", "ppt"))
        self.decryption_file_selector.setItemText(5, _translate("widget", "xlsx"))
        self.decryption_file_selector.setItemText(6, _translate("widget", "zip"))
        self.decryption_button.setText(_translate("widget", "解密"))
        self.encryption_input_lineEdit.setText("请选择需要加密的文件...")


    def select_file(self):
        # 打开文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(None, '选择文件', '', '所有文件 (*)')
        if file_path:
            self.encryption_input_lineEdit.setText(f'{file_path}')
        else:
            self.encryption_input_lineEdit.setText('未选择文件')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())