# gc9a01_simulator
Project Overview
gc9a01_simulator is a Python-based simulator for the GC9A01 circular display. It uses PIL (Pillow) for drawing and tkinter for rendering the simulated display in a window.

Architecture
SimulatedGC9A01 (gc9a01_simulator.py): The core class that mimics a GC9A01 display. It maintains an internal PIL image, provides drawing methods (pixels, lines, circles, text), handles rotation, and applies a circular mask to simulate a round screen.
gc9a01_constants.py: Contains color definitions (e.g., GC9A01A_RED) in 565 format.
font5x7.py: Provides a bitmap font mapping for drawBitmapChar and printText.
Rendering Pipeline:
Drawing operations update a rectangular PIL image.
update_display() or renderToTk() applies a circular mask.
The resulting image is rotated based on the current rotation setting.
The final image is displayed on a tkinter.Canvas.
Common Development Tasks
Running the Simulator
To run the main simulator with a basic example:

python gc9a01_simulator.py
Running Tests/Animations
To run the test suite with various drawing and animation examples:

python test_simulator.py
Key Implementation Details
Color Conversion: The simulator converts 16-bit 565 colors to 8-bit RGB tuples via color565_to_rgb.
Coordinate System: The display is 240x240. The setCursor method handles circular clipping by repositioning points outside the radius back to the circle's edge.
Rotation: Supports four rotation states (0-3), mapping to PIL's ROTATE_90, ROTATE_180, and ROTATE_270.
