from PyQt5.QtWidgets import QMessageBox, QPushButton, QLabel, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class MyApp(QtGui.MainWindow):

    def select_file(self):
            fname = QFileDialog.getOpenFileName(None, "Open File", "", "All Files (*);; Python Files (*.py)")
            if fname:
                self.old_file_name_info.setText("Old Filename: " + str(fname))
                #self.original_path_info.setText(_translate("MainWindow", "Original Path:"))

    def rename_new_file_popup(self):  
            rename_msg_box = QtWidgets.QInputDialog(None, 'Rename File', "New Filename:")
            x = rename_msg_box.exec_()


