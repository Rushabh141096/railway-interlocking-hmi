
#choice is a function from Python’s random module.
from random import choice

#QTimer is a class from the PyQt6 library. It is a timer that can call a function repeatedly at a set interval.
from PyQt6.QtCore import QTimer

class Signal:
    RED = 0
    GREEN = 1
    def __init__(self):
        self.aspect = Signal.RED

class Track:
    def __init__(self):
        self.occupied = False

class Route:
    def __init__(self):
        self.locked = False

class AutomaticSensors:
    def __init__(self, mode="automatic"):
        self.mode = mode
        self.track = Track()
        self.route = Route()
        self.signal = Signal()

        self.sensor_timer = QTimer()
        self.sensor_timer.timeout.connect(self.update_sensors)
        self.sensor_timer.start(1000) #Starts the timer, firing every 1000 milliseconds (1 second).

    def update_sensors(self):
        if self.mode == "automatic":
            self.track.occupied = choice([True, False])
            self.route.locked = choice([True, False])

    def toggle_track(self):
        if self.mode == "manual":
            self.track.occupied = not self.track.occupied

    def toggle_route(self):
        if self.mode == "manual":
            self.route.locked = not self.route.locked

    def switch_mode(self, mode=None):
        """Switch mode safely"""
        if mode:
            self.mode = mode
        else:
            self.mode = "manual" if self.mode == "automatic" else "automatic"

























# # models/plc_sensors.py
# from pyModbusTCP.client import ModbusClient

# class PLCReader:
#     def __init__(self, tracks, routes, plc_ip="192.168.0.10"):
#         self.tracks = tracks
#         self.routes = routes
#         self.plc = ModbusClient(host=plc_ip, port=502, auto_open=True)

#     def update_sensors(self):
#         """Poll the PLC and update track/route objects"""
#         # Tracks occupancy from PLC coils
#         for i, track in enumerate(self.tracks):
#             coil = self.plc.read_coils(i, 1)
#             if coil:
#                 track.occupied = coil[0]

#         # Routes lock status from PLC coils
#         for i, route in enumerate(self.routes):
#             coil = self.plc.read_coils(100 + i, 1)
#             if coil:
#                 route.locked = coil[0]
