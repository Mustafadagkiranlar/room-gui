import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow

from room_v1alfa import Ui_mainWindow

class MainWindow:
    def __init__(self):
        self.main_win=QMainWindow()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.odalarPage)#set page 1

        self.ui.odalarButton.clicked.connect(self.showodalar)
        self.ui.girisButton.clicked.connect(self.showgiris)
        self.ui.infoButton.clicked.connect(self.showinfo)

    def show(self):
        self.main_win.show()

    def showgiris(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.girisPage)
    
    def showodalar(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.odalarPage)
    
    def showinfo(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.infoPage)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())