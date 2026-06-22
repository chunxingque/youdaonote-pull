Introduction

In some applications it is often necessary to perform long-running tasks, such as computations or network operations, that cannot be broken up into smaller pieces and processed alongside normal application events. In such cases, we would like to be able to perform these tasks in a way that does not interfere with the normal running of the application, and ensure that the user interface continues to be updated. One way of achieving this is to perform these tasks in a separate thread to the main user interface thread, and only interact with it when we have results we need to display.

This example shows how to create a separate thread to perform a task - in this case, drawing stars for a picture - while continuing to run the main user interface thread. The worker thread draws each star onto its own individual image, and it passes each image back to the example's window which resides in the main application thread.

The User Interface

We begin by importing the modules we require. We need the math and random modules to help us draw stars.

import math, random, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Window(QWidget):

    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        
        self.thread = Worker()

The main window in this example is just a QWidget. We create a single Worker instance that we can reuse as required.

The user interface consists of a label, spin box and a push button that the user interacts with to configure the number of stars that the thread wil draw. The output from the thread is presented in a QLabel instance, viewer.

        label = QLabel(self.tr("Number of stars:"))
        self.spinBox = QSpinBox()
        self.spinBox.setMaximum(10000)
        self.spinBox.setValue(100)
        self.startButton = QPushButton(self.tr("&Start"))
        self.viewer = QLabel()
        self.viewer.setFixedSize(300, 300)

We connect the standard finished() and terminated() signals from the thread to the same slot in the widget. This will reset the user interface when the thread stops running. The custom output(QRect, QImage) signal is connected to the addImage() slot so that we can update the viewer label every time a new star is drawn.

        self.connect(self.thread, SIGNAL("finished()"), self.updateUi)
        self.connect(self.thread, SIGNAL("terminated()"), self.updateUi)
        self.connect(self.thread, SIGNAL("output(QRect, QImage)"), self.addImage)
        self.connect(self.startButton, SIGNAL("clicked()"), self.makePicture)

The start button's clicked() signal is connected to the makePicture() slot, which is responsible for starting the worker thread.

We place each of the widgets into a grid layout and set the window's title:

        layout = QGridLayout()
        layout.addWidget(label, 0, 0)
        layout.addWidget(self.spinBox, 0, 1)
        layout.addWidget(self.startButton, 0, 2)
        layout.addWidget(self.viewer, 1, 0, 1, 3)
        self.setLayout(layout)
        
        self.setWindowTitle(self.tr("Simple Threading Example"))

The makePicture() slot needs to do three things: disable the user interface widgets that are used to start a thread, clear the viewer label with a new pixmap, and start the thread with the appropriate parameters.

Since the start button is the only widget that can cause this slot to be invoked, we simply disable it before starting the thread, avoiding problems with re-entrancy.

    def makePicture(self):
    
        self.spinBox.setReadOnly(True)
        self.startButton.setEnabled(False)
        pixmap = QPixmap(self.viewer.size())
        pixmap.fill(Qt.black)
        self.viewer.setPixmap(pixmap)
        self.thread.render(self.viewer.size(), self.spinBox.value())

We call a custom method in the Worker thread instance with the size of the viewer label and the number of stars, obtained from the spin box.

Whenever is star is drawn by the worker thread, it will emit a signal that is connected to the addImage() slot. This slot is called with a QRect value, indicating where the star should be placed in the pixmap held by the viewer label, and an image of the star itself:

    def addImage(self, rect, image):
    
        pixmap = self.viewer.pixmap()
        painter = QPainter()
        painter.begin(pixmap)
        painter.drawImage(rect, image)
        painter.end()
        self.viewer.update(rect)

We use a QPainter to draw the image at the appropriate place on the label's pixmap.

The updateUi() slot is called when a thread stops running. Since we usually want to let the user run the thread again, we reset the user interface to enable the start button to be pressed:

    def updateUi(self):
    
        self.spinBox.setReadOnly(False)
        self.startButton.setEnabled(True)

Now that we have seen how an instance of the Window class uses the worker thread, let us take a look at the thread's implementation.

The Worker Thread

The worker thread is implemented as a PyQt thread rather than a Python thread since we want to take advantage of the signals and slots mechanism to communicate with the main application.

class Worker(QThread):

    def __init__(self, parent = None):
    
        QThread.__init__(self, parent)
        self.exiting = False
        self.size = QSize(0, 0)
        self.stars = 0

We define size and stars attributes that store information about the work the thread is required to do, and we assign default values to them. The exiting attribute is used to tell the thread to stop processing.

Each star is drawn using a QPainterPath that we define in advance:

        self.path = QPainterPath()
        angle = 2*math.pi/5
        self.outerRadius = 20
        self.innerRadius = 8
        self.path.moveTo(self.outerRadius, 0)
        for step in range(1, 6):
            self.path.lineTo(
                self.innerRadius * math.cos((step - 0.5) * angle),
                self.innerRadius * math.sin((step - 0.5) * angle)
                )
            self.path.lineTo(
                self.outerRadius * math.cos(step * angle),
                self.outerRadius * math.sin(step * angle)
                )
        self.path.closeSubpath()

Before a Worker object is destroyed, we need to ensure that it stops processing. For this reason, we implement the following method in a way that indicates to the part of the object that performs the processing that it must stop, and waits until it does so.

    def __del__(self):
    
        self.exiting = True
        self.wait()

For convenience, we define a method to set up the attributes required by the thread before starting it.

    def render(self, size, stars):
    
        self.size = size
        self.stars = stars
        self.start()

The start() method is a special method that sets up the thread and calls our implementation of the run() method. We provide the render() method instead of letting our own run() method take extra arguments because the run() method is called by PyQt itself with no arguments.

The run() method is where we perform the processing that occurs in the thread provided by the Worker instance:

    def run(self):
        
        # Note: This is never called directly. It is called by Qt once the
        # thread environment has been set up.
        
        random.seed()
        n = self.stars
        width = self.size.width()
        height = self.size.height()

Information stored as attributes in the instance determines the number of stars to be drawn and the area over which they will be distributed.

We draw the number of stars requested as long as the exiting attribute remains False. This additional check allows us to terminate the thread on demand by setting the exiting attribute to True at any time.

        while not self.exiting and n > 0:
        
            image = QImage(self.outerRadius * 2, self.outerRadius * 2,
                           QImage.Format_ARGB32)
            image.fill(qRgba(0, 0, 0, 0))
            
            x = random.randrange(0, width)
            y = random.randrange(0, height)
            angle = random.randrange(0, 360)
            red = random.randrange(0, 256)
            green = random.randrange(0, 256)
            blue = random.randrange(0, 256)
            alpha = random.randrange(0, 256)
            
            painter = QPainter()
            painter.begin(image)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(red, green, blue, alpha))
            painter.translate(self.outerRadius, self.outerRadius)
            painter.rotate(angle)
            painter.drawPath(self.path)
            painter.end()

The drawing code is not particularly relevant to this example. We simply draw on an appropriately-sized transparent image.

For each star drawn, we send the main thread information about where it should be placed along with the star's image by emitting our custom output() signal:

            self.emit(SIGNAL("output(QRect, QImage)"),
                      QRect(x - self.outerRadius, y - self.outerRadius,
                            self.outerRadius * 2, self.outerRadius * 2), image)
            n -= 1

Since QRect and QImage objects can be serialized for transmission via the signals and slots mechanism, they can be sent between threads in this way, making it convenient to use threads in a wide range of situations where built-in types are used.

Running the Example

We only need one more piece of code to complete the example:

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())