import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow

from room_v1alfa import Ui_mainWindow #add created python library

class MainWindow:
    def __init__(self):
        self.main_win=QMainWindow()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.odalarPage)#set page 1

        self.ui.odalarButton.clicked.connect(self.showodalar)
        self.ui.girisButton.clicked.connect(self.showgiris)
        self.ui.infoButton.clicked.connect(self.showinfo)

        #adding İtems to The list 
        for i in range(5):
            self.ui.odalarList.insertItem(i,"Oda {}".format(i+1))

        #send Clicked button data
        self.ui.odalarList.itemDoubleClicked.connect(self.showRoomInfo)
        # or single clicked
        #self.ui.odalarList.itemClicked.connect(self.showRoomInfo)

    def show(self):
        self.main_win.show()

    def showgiris(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.girisPage)
    
    def showodalar(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.odalarPage)
    
    def showinfo(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.infoPage)

    #get pushed button data in the function and processes it
    def showRoomInfo(self,sendedItem):
        print(self.ui.odalarList.currentItem().text()) #shows text when clicked
        print(self.ui.odalarList.currentRow()) #show index when clicked
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())