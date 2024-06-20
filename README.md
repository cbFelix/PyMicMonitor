# PyMicMonitor

PyMicMonitor is a simple application that monitors microphone input and displays real-time amplitude data using PyQtGraph and PySide6.

## Terms of Use

This software is provided "as is", without warranty of any kind. You may use and modify this software for personal and educational purposes under the terms of GNU General Public License version 3. See LICENSE.md for more details.

## Installation

To run PyMicMonitor, ensure you have Python 3.8 or higher installed, along with the following dependencies:

- numpy
- PySide6
- sounddevice
- pyqtgraph

You can install these dependencies using pip:

```bash
pip install numpy PySide6 sounddevice pyqtgraph
```

## Usage

Run the application using Python:

```bash
python mic_monitor.py
```

Once launched, the application will display a real-time plot of microphone input amplitude. The plot updates every 20 milliseconds. You can adjust the sampling rate and number of channels in the code (`MicrophoneMonitor` class initialization).

## License

PyMicMonitor is licensed under the GNU General Public License version 3. See LICENSE.md for the full license text.

## Contact

For questions or suggestions regarding PyMicMonitor, please contact [onerun325@gmail.com].