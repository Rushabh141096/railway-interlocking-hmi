from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer, Qt
from models import Signal

class InterlockingGUI(QWidget):
    def __init__(self, sensors, logic):
        super().__init__()
        self.sensors = sensors
        self.logic = logic

        self.setWindowTitle("Interlocking HMI")
        self.setGeometry(80, 80, 400, 500)

        # Labels
        self.track_label = QLabel()
        self.route_label = QLabel()
        self.signal_label = QLabel()

        # Buttons
        self.track_btn = QPushButton("Toggle Track Occupancy")
        self.route_btn = QPushButton("Toggle Route Lock")
        self.mode_btn = QPushButton("Switch Mode (Current: {})".format(self.sensors.mode.capitalize()))

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.track_label)
        layout.addWidget(self.route_label)
        layout.addWidget(self.signal_label)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.track_btn)
        btn_layout.addWidget(self.route_btn)
        layout.addLayout(btn_layout)
        layout.addWidget(self.mode_btn)

        self.setLayout(layout)

        # Connect buttons
        self.track_btn.clicked.connect(self.sensors.toggle_track)
        self.route_btn.clicked.connect(self.sensors.toggle_route)
        self.mode_btn.clicked.connect(self.switch_mode)

        # Timer to refresh UI every 500ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(500)

        self.update_ui()

    def switch_mode(self):
    # Toggle mode
        self.sensors.switch_mode()
        self.mode_btn.setText(f"Switch Mode (Current: {self.sensors.mode.capitalize()})")

    # Optional: disable toggle buttons in automatic mode
        if self.sensors.mode == "automatic":
            self.track_btn.setDisabled(True)
            self.route_btn.setDisabled(True)
        else:
            self.track_btn.setDisabled(False)
            self.route_btn.setDisabled(False)


    def update_ui(self):
        # Evaluate logic first
        self.logic.evaluate()

        # Track label
        if self.sensors.track.occupied:
            self.track_label.setText("Track: OCCUPIED")
            self.track_label.setStyleSheet("background-color:red; color:white; font-weight:bold; font-size:14px")
        else:
            self.track_label.setText("Track: FREE")
            self.track_label.setStyleSheet("background-color:green; color:white; font-weight:bold; font-size:14px")

        # Route label
        if self.sensors.route.locked:
            self.route_label.setText("Route: LOCKED")
            self.route_label.setStyleSheet("background-color:green; color:white; font-weight:bold; font-size:14px")
        else:
            self.route_label.setText("Route: UNLOCKED")
            self.route_label.setStyleSheet("background-color:gray; color:white; font-weight:bold; font-size:14px")

        # Signal label
        if self.sensors.signal.aspect == Signal.GREEN:
            pixmap = QPixmap("go.jpg")
        else:
            pixmap = QPixmap("stop.jpg")

        pixmap = pixmap.scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.signal_label.setPixmap(pixmap)
        self.signal_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
























# # Gui.py
# from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
# from PyQt6.QtWidgets import QPushButton
# from PyQt6.QtGui import QPixmap
# from PyQt6.QtCore import QTimer, Qt
# from models import Signal

# class InterlockingGUI(QWidget):
#     def __init__(self, tracks, routes, signals, logic):
#         super().__init__()
#         self.tracks = tracks
#         self.routes = routes
#         self.signals = signals
#         self.logic = logic

#         self.setWindowTitle("Interlocking HMI")
#         self.setGeometry(50, 50, 500, 150 + len(tracks)*120)

#         # GUI elements
#         self.track_labels = []
#         self.route_labels = []
#         self.signal_labels = []

#         main_layout = QVBoxLayout()

#         for i in range(len(tracks)):
#             track_label = QLabel()
#             route_label = QLabel()
#             signal_label = QLabel()

#             self.track_labels.append(track_label)
#             self.route_labels.append(route_label)
#             self.signal_labels.append(signal_label)

#             h_layout = QHBoxLayout()
#             v_layout = QVBoxLayout()
#             v_layout.addWidget(track_label)
#             v_layout.addWidget(route_label)
#             v_layout.addWidget(signal_label)
#             h_layout.addLayout(v_layout)

#             main_layout.addLayout(h_layout)

#         self.setLayout(main_layout)

#         # Timer for GUI update
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_ui)
#         self.timer.start(500)
#         self.update_ui()

#     def update_ui(self):
#         self.logic.evaluate()
#         for i in range(len(self.tracks)):
#             track = self.tracks[i]
#             route = self.routes[i]
#             signal = self.signals[i]

#             self.track_labels[i].setText(f"{track.name}: {'OCCUPIED' if track.occupied else 'FREE'}")
#             self.track_labels[i].setStyleSheet(
#                 f"background-color:{'red' if track.occupied else 'green'}; color:white; font-weight:bold; font-size:14px"
#             )

#             self.route_labels[i].setText(f"{route.name}: {'LOCKED' if route.locked else 'UNLOCKED'}")
#             self.route_labels[i].setStyleSheet(
#                 f"background-color:{'green' if route.locked else 'gray'}; color:white; font-weight:bold; font-size:14px"
#             )

#             # Signal graphics
#             pixmap = QPixmap("go.jpg") if signal.aspect == Signal.GREEN else QPixmap("stop.jpg")
#             pixmap = pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
#             self.signal_labels[i].setPixmap(pixmap)
#             self.signal_labels[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
