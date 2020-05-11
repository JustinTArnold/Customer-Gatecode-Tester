# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newgh.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess
import time
import os, os.path
import clipboard


class Ui_GateHelper(object):
    def setupUi(self, GateHelper):
        GateHelper.setObjectName("GateHelper")
        GateHelper.setEnabled(True)
        GateHelper.resize(221, 275)
        GateHelper.setStyleSheet("background-color: rgb(0, 85, 255);")
        GateHelper.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(GateHelper)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(85, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(30, 70, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(85, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 120, 161, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 170, 161, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 220, 161, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        GateHelper.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GateHelper)
        self.statusbar.setObjectName("statusbar")
        GateHelper.setStatusBar(self.statusbar)

        self.retranslateUi(GateHelper)
        self.pushButton.clicked.connect(lambda: Ui_GateHelper.test_gate_code(self))
        self.pushButton_2.clicked.connect(lambda: Ui_GateHelper.gate_poll(self))
        self.pushButton_3.clicked.connect(lambda: Ui_GateHelper.clear(self))

    def retranslateUi(self, GateHelper):
        _translate = QtCore.QCoreApplication.translate
        GateHelper.setWindowTitle(_translate("GateHelper", "GateHelper"))
        self.plainTextEdit.setPlaceholderText(_translate("GateHelper", "Property Number"))
        self.plainTextEdit_2.setPlaceholderText(_translate("GateHelper", "Gate Code"))
        self.pushButton.setText(_translate("GateHelper", "Test GC"))
        self.pushButton_2.setText(_translate("GateHelper", "GatePoll"))
        self.pushButton_3.setText(_translate("GateHelper", "Reset"))

    def test_gate_code(self):
        prop_num = self.plainTextEdit.text()
        gate_code = self.plainTextEdit_2.text()
        result = ""
        if self.plainTextEdit.text() in ipdict3:
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subprocess.call(['runvbs.bat', (ipdict3.get(prop_num)), gate_code], startupinfo=si)
            with open('tellog.txt', 'r') as telnet_result:
                telnet_result = telnet_result.readlines()
                for line in telnet_result:
                    result = str(line)
                    result = result.split()
            self.plainTextEdit_2.setText(result[len(result)-1])
            self.plainTextEdit.setText('')
            clipboard.copy("GC tested and working")
        else:
            self.plainTextEdit.setText("Invalid")
            self.plainTextEdit_2.setText("")

    
    def gate_poll(self):
        if self.plainTextEdit.text() in ipdict1:
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subp = subprocess.Popen(['psexgpnew1.bat', (ipdict1.get(self.plainTextEdit.text()))], startupinfo=si)
            while subp.poll() == None:
                time.sleep(.1)
            self.plainTextEdit.setText("Gate Poll Started!")

        elif self.plainTextEdit.text() in ipdict2:
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subp = subprocess.Popen(['psexgpnew2.bat', (ipdict2.get(self.plainTextEdit.text()))], startupinfo=si)
            while subp.poll() == None:
                time.sleep(.1)
            self.plainTextEdit.setText("Gate Poll Started!")
            
        else:
            self.plainTextEdit.setText("Invalid")
            self.plainTextEdit_2.setText("")
    
    def clear(self):
        self.plainTextEdit.setText("")
        self.plainTextEdit_2.setText("")

ipdict1 = {
    
    "001": "1133",
    "002": "1062",
    "003": "1130",
    "004": "1132",
    "006": "1102",
    "007": "1069",
    "008": "1073",
    "009": "1109",
    "010": "1068",
    "011": "1061",
    "012": "1120",
    "013": "1138",
    "015": "1104",
    "016": "1140",
    "017": "1141",
    "018": "1121",
    "020": "1123",
    "022": "1124",
    "023": "1057",
    "026": "1063",
    "027": "1142",
    "028": "1127",
    "029": "1128",
    "030": "1129",
    "031": "1112",
    "032": "1070",
    "033": "1150",
    "034": "1151",
    "035": "1075",
    "036": "1064",
    "038": "1085",
    "039": "1086",
    "040": "1087",
    "044": "1071",
    "045": "1072",
    "046": "1065",
    "047": "1055",
    "059": "1110",
    "060": "1101",
    "061": "1143",
    "062": "1103",
    "070": "1166",
    "071": "1106",
    "171": "1047",
    "172": "1046",
    "173": "1044",
    "174": "1048",
    "175": "1049",
    "178": "1043"

}

ipdict2 = {
    
    "203": "1053",
    "204": "1054",
    "301": "1032",
    "302": "1033",
    "303": "1026",
    "304": "1029",
    "305": "1031",
    "307": "1159",
    "308": "1034",
    "309": "1028",
    "310": "1035",
    "311": "1025",
    "312": "1036",
    "313": "1037",
    "314": "1157",
    "315": "1162",
    "316": "1163",
    "317": "1164",
    "352": "1021",
    "354": "1023",
    "355": "1022",
    "403": "1137",
    "428": "1088",
    "429": "1089",
    "432": "1107",
    "433": "1108",
    "434": "1111",
    "435": "1067",
    "436": "1116",
    "437": "1117",
    "438": "1118",
    "439": "1119",
    "440": "1152",
    "443": "1081",
    "444": "1082",
    "445": "1083",
    "450": "1153",
    "451": "1144",
    "452": "1145",
    "453": "1146",
    "454": "1147",
    "455": "1148",
    "456": "1161",
    "501": "1092",
    "502": "1093",
    "503": "1094",
    "504": "1095",
    "505": "1096",
    "506": "1097",
    "507": "1098"

}

ipdict3 = {
    "001": "10.100.1.103",
    "002": "10.100.2.103",
    "003": "10.100.3.103",
    "004": "10.100.4.103",
    "006": "10.100.6.103",
    "007": "10.100.7.103",
    "008": "10.100.8.103",
    "009": "10.100.9.103",
    "010": "10.100.10.103",
    "011": "10.100.11.103",
    "012": "10.100.12.103",
    "013": "10.100.13.103",
    "015": "10.100.15.103",
    "016": "10.100.16.103",
    "017": "10.100.17.103",
    "018": "10.100.18.103",
    "020": "10.100.20.103",
    "022": "10.100.22.103",
    "023": "10.100.23.103",
    "024": "10.100.24.103",
    "026": "10.100.26.103",
    "027": "10.100.27.103",
    "028": "10.100.28.103",
    "029": "10.100.29.103",
    "030": "10.100.30.103",
    "031": "10.100.31.103",
    "032": "10.100.32.103",
    "033": "10.100.33.103",
    "034": "10.100.34.103",
    "035": "10.100.35.103",
    "036": "10.100.36.103",
    "038": "10.100.38.103",
    "039": "10.100.39.103",
    "040": "10.100.40.103",
    "044": "10.100.44.103",
    "045": "10.100.45.103",
    "046": "10.100.46.103",
    "047": "10.100.47.103",
    "059": "10.100.59.103",
    "060": "10.100.60.103",
    "061": "10.100.61.103",
    "062": "10.100.62.103",
    "070": "10.100.70.103",
    "071": "10.100.71.103",
    "171": "10.101.71.103",
    "172": "10.101.72.103",
    "173": "10.101.73.103",
    "174": "10.101.74.103",
    "175": "10.101.75.103",
    "177": "10.101.77.103",
    "178": "10.101.78.103",
    "203": "10.102.3.103",
    "204": "10.102.4.103",
    "301": "10.103.1.103",
    "302": "10.103.2.103",
    "303": "10.103.3.103",
    "304": "10.103.4.103",
    "305": "10.103.5.103",
    "307": "10.103.7.103",
    "308": "10.103.8.103",
    "309": "10.103.9.103",
    "310": "10.103.10.103",
    "311": "10.103.11.103",
    "312": "10.103.12.103",
    "313": "10.103.13.103",
    "314": "10.103.14.103",
    "315": "10.103.15.199",
    "316": "10.103.16.103",
    "317": "10.103.17.103",
    "352": "10.103.52.103",
    "354": "10.103.54.103",
    "355": "10.103.55.103",
    "403": "10.104.3.103",
    "425": "10.104.25.103",
    "428": "10.104.28.103",
    "429": "10.104.29.103",
    "432": "10.104.32.103",
    "433": "10.104.33.103",
    "434": "10.104.34.103",
    "435": "10.104.35.103",
    "436": "10.104.36.103",
    "437": "10.104.37.103",
    "438": "10.104.38.103",
    "439": "10.104.39.103",
    "440": "10.104.40.103",
    "443": "10.104.43.103",
    "444": "10.104.44.103",
    "445": "10.104.45.103",
    "450": "10.104.50.103",
    "451": "10.104.51.103",
    "452": "10.104.52.103",
    "453": "10.104.53.103",
    "454": "10.104.54.103",
    "455": "10.104.55.103",
    "456": "10.104.56.103",
    "501": "10.105.1.103",
    "502": "10.105.2.103",
    "503": "10.105.3.103",
    "504": "10.105.4.103",
    "505": "10.105.5.103",
    "506": "10.105.6.103",
    "507": "10.105.7.103"
}
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_GateHelper()
    ui.setupUi(MainWindow)
    MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    MainWindow.show()
    sys.exit(app.exec_())
