import sys
import numpy as np
from PySide6.QtCore import QTimer, Slot
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
import sounddevice as sd
import pyqtgraph as pg


class PyMicrophoneMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyMicMonitor')
        self.setGeometry(100, 100, 1000, 600)

        self.plot_data = np.zeros(100)
        self.fs = 48000
        self.channels = 2
        self.setup_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(20)

        self.stream = sd.InputStream(channels=self.channels, samplerate=self.fs, callback=self.audio_callback)
        self.stream.start()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.info_label = QLabel()
        layout.addWidget(self.info_label)

        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)

        self.setLayout(layout)

        self.curve = self.plot_widget.plot(self.plot_data, pen='green', width=0.5)
        self.plot_widget.setYRange(0, 1)
        self.plot_widget.setTitle("Microphone Input")
        self.plot_widget.setLabel('left', 'Amplitude')
        self.plot_widget.setLabel('bottom', 'Samples')

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        amplitude = np.abs(indata).mean()
        self.plot_data[:-1] = self.plot_data[1:]
        self.plot_data[-1] = amplitude

    @Slot()
    def update_plot(self):
        self.curve.setData(self.plot_data)
        self.info_label.setText(f"Sampling Rate: {self.fs} Hz | Channels: {self.channels} | Sample Size: {self.stream.samplesize} | CPU Load: {self.stream.cpu_load*100:.2f}%")

    def closeEvent(self, event):
        self.stream.stop()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    monitor = PyMicrophoneMonitor()
    monitor.show()
    sys.exit(app.exec())
