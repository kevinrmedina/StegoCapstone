import sys
from PyQt4 import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.show()

    def init_ui(self):
        main_menu = self.menuBar()
        dashboard = main_menu.addMenu('Dashboard')
        dashboard.addAction(QAction('Detail Raport', self))
        dashboard.addAction(QAction('All companies', self))
        dashboard.triggered.connect(self.change_view)

        self.dashboardView = Dashboard()
        self.detailView = Raport()

        self.stacked = QStackedWidget()
        self.setCentralWidget(self.stacked)
        self.stacked.addWidget(self.detailView)
        self.stacked.addWidget(self.dashboardView)

    def change_view(self, q):
        if q.text() == 'Detail Raport':
            self.stacked.setCurrentWidget(self.detailView)
        elif q.text() == 'All companies':
            self.stacked.setCurrentWidget(self.dashboardView)

class RaportWindow(object):
    def detailRaport(self, MainWindow):
        console.log("Hello")

class DashboardWindow(object):
    def setupUIdashboard(self, MainWindow):
        console.log("Hello")

class Dashboard(QMainWindow, DashboardWindow):
    def __init__(self, parent=None):
        super(Dashboard, self).__init__(parent)
        self.setupUIdashboard(self)

class Raport(QMainWindow, RaportWindow):
    def __init__(self, parent=None):
        super(Raport, self).__init__(parent)
        self.detailRaport(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())