#Imports Python’s system module Used here to: Access command-line arguments
import sys

# Imports QApplication, which is:
# The core object required for any PyQt GUI
# Manages the event loop, widgets, and user interaction
from PyQt6.QtWidgets import QApplication

#Imports AutomaticSensors from models file
from models import AutomaticSensors

#import logic layer : Implements railway interlocking rules Controls how tracks, routes, and signals interact safely
from logics import InterlockingLogic

#Imports the graphical user interface
from Gui import InterlockingGUI

# from plc_sensors import PLCReader
# from PyQt6.QtCore import QTimer

def main():
    #Creates the Qt application object sys.argv allows Qt to read command-line options
    app = QApplication(sys.argv)

    # Start in automatic mode
    sensors = AutomaticSensors(mode="automatic")

    #pass sensor objects to the logics like kind of input, output
    logic = InterlockingLogic(sensors.track, sensors.route, sensors.signal)
    
    #create main GUI window
    window = InterlockingGUI(sensors, logic)
    window.show()


    # # PLC reader (polls PLC periodically)
    # plc_reader = PLCReader(tracks, routes, plc_ip="192.168.0.10")

    # plc_timer = QTimer()
    # plc_timer.timeout.connect(plc_reader.update_sensors)
    # plc_timer.start(500)  # poll PLC every 0.5s

    #Starts Qt’s event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


















#     # main.py
# import sys
# from PyQt6.QtWidgets import QApplication
# from PyQt6.QtCore import QTimer
# from models import Track, Route, Signal, AutomaticSensors
# from models.plc_sensors import PLCReader
# from logics import InterlockingLogic
# from Gui import InterlockingGUI

# USE_PLC = False  # Change to True if you want real PLC connection

# def main():
#     app = QApplication(sys.argv)

#     n = 3  # number of tracks/signals/routes

#     # Create models
#     tracks = [Track(name=f"Track {i+1}") for i in range(n)]
#     routes = [Route(name=f"Route {i+1}") for i in range(n)]
#     signals = [Signal(name=f"Signal {i+1}") for i in range(n)]

#     # Logic
#     logic = InterlockingLogic(tracks, routes, signals)

#     # GUI
#     window = InterlockingGUI(tracks, routes, signals, logic)
#     window.show()

#     # Sensors: PLC or simulation
#     if USE_PLC:
#         plc_reader = PLCReader(tracks, routes, plc_ip="192.168.0.10")
#         timer = QTimer()
#         timer.timeout.connect(plc_reader.update_sensors)
#         timer.start(500)
#     else:
#         sim = AutomaticSensors(tracks, routes)  # automatic simulation

#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()

