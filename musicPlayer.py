import sys
from PyQt4 import QtGui
from pygame import mixer

X = 20
Y = 10
BUTTON_WIDTH = 80
mixer.init()
pausedMusic = True

def play():
    mixer.music.load('test.mp3')
    mixer.music.play()


def stop():
    mixer.music.stop()


def pause():
    global pausedMusic
    if pausedMusic:
        mixer.music.pause()
    else:
        mixer.music.unpause()
    pausedMusic = not pausedMusic


def backward():
    mixer.music.stop()


def create_button(button_name, widget, button_count, functionality, line=0):
    button = QtGui.QPushButton(widget)
    button.setText(button_name)
    button.move(X + BUTTON_WIDTH * (button_count - 1), Y + (line*30))
    button.clicked.connect(functionality)


def window():
    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()
    create_button("Play", widget, 1, play)
    create_button("Pause", widget, 2, pause)
    create_button("Stop", widget, 3, stop)
    create_button("Back", widget, 1, stop, line=1)
    create_button("Next", widget, 2, stop, line=1)
    widget.setGeometry(100, 100, 290, 300)
    widget.setWindowTitle("MusicPlayer")
    playlist = QtGui.QListWidget(widget)
    playlist.addItem('test')
    playlist.move(X, Y + BUTTON_WIDTH)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
