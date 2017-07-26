import sys
from PyQt4 import QtGui
from pygame import mixer

X = 50
Y = 20
BUTTON_WIDTH = 80
mixer.init()

def play():
    mixer.music.load('test.mp3')
    mixer.music.play()

def stop():
    mixer.music.stop()

def create_button(button_name, widget, button_count, function):
    button = QtGui.QPushButton(widget)
    button.setText(button_name)
    button.move(X + BUTTON_WIDTH * (button_count - 1), Y)
    button.clicked.connect(function)


def window():
   app = QtGui.QApplication(sys.argv)
   widget = QtGui.QWidget()
   create_button("Play", widget, 1, play)
   create_button("Pause", widget, 2, stop)
   create_button("Stop", widget, 3, stop)
   widget.setGeometry(100,100,400,50)
   widget.setWindowTitle("MusicPlayer")
   widget.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()