# Railway Interlocking HMI (Python)

## Overview
A Python-based railway interlocking HMI simulating PLC-controlled tracks, routes, and signals.
Supports automated testing and PLC integration via Modbus.

## Architecture
- Models: Track, Route, Signal
- Logic: Interlocking safety rules
- GUI: PyQt6 HMI
- PLC: Modbus TCP / Simulation
- Tests: pytest-based safety tests

## Run
```bash
pip install -r requirements.txt
python main.py
