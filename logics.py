from models import Signal

class InterlockingLogic:
    def __init__(self, track, route, signal):
        self.track = track
        self.route = route
        self.signal = signal

    def evaluate(self):
        """Set signal green if track free and route locked, else red"""
        if not self.track.occupied and self.route.locked:
            self.signal.aspect = Signal.GREEN
        else:
            self.signal.aspect = Signal.RED



































#             # logics.py
# from models import Signal

# class InterlockingLogic:
#     def __init__(self, tracks, routes, signals):
#         self.tracks = tracks
#         self.routes = routes
#         self.signals = signals

#     def evaluate(self):
#         """Simple interlocking logic"""
#         for i in range(len(self.signals)):
#             track = self.tracks[i]
#             route = self.routes[i]
#             signal = self.signals[i]

#             if not track.occupied and route.locked:
#                 signal.aspect = Signal.GREEN
#             else:
#                 signal.aspect = Signal.RED

