from multiprocessing import Process, Queue
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys

class MainWindow(QMainWindow):

    def __init__(self, log, url, que):
        super(MainWindow,self).__init__()
        
        self.que = que
        self.log = log
        print("In __init__,  log : ", type(log), log)
        print("In __init__,  que : ", type(que), que)        

        self.browser = QWebEngineView()
        self.browser.setGeometry(300, 300, 1200, 800)
        self.browser.setUrl(QUrl(url))

        self.setCentralWidget(self.browser)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(46,33))
        self.addToolBar(navtb)

        back_btn = QAction(QIcon('back.png'), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon('forward.png'), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction(QIcon('refresh.png'), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)

        exit_btn = QAction(QIcon('exit.png'), "Select and exit", self)
        exit_btn.setStatusTip("Select URL and exit to calibre")
        exit_btn.triggered.connect(self.select_and_exit)
        navtb.addAction(exit_btn)

        self.show()

    def navigate_to_url(self): # Does not receive the Url
        q = QUrl( self.urlbar.text() )
        self.browser.setUrl(q)
        print("In navigate_to_url  URL : ", self.urlbar.text())

    def update_urlbar(self, q):
        self.urlbar.setText( q.toString() )
        self.urlbar.setCursorPosition(0)

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle(title)

    def select_and_exit(self):
        self.que.put(self.urlbar.text())
        sys.exit(0)
        #sys.exit("done")
        # need to push the address to calling process using the queue opened
        
def spawned_main(que, url):
    logfile = open("spanlog.txt", "a")
    txt=time.strftime("%D %H:%M:%S", time.localtime())+' logfile is open now'
    logfile.write(txt+"\n")
    logfile.flush()
    print(time.strftime("%D %H:%M:%S", time.localtime()), "In spawned_main(que, url)", type(que), type(url))
    app = QApplication([])
    window = MainWindow(logfile, url, que)
    app.exec_()
    
if __name__ == '__main__':
    url="https://www.noosfere.org/"
    que = Queue()
    prc = Process(target=spawned_main, args=(que, url))
    prc.start()
    print("In main, la dernier url est: ", que.get())
    prc.join()
    
