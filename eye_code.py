import tkinter as tk
import random
from gc9a01_simulator import SimulatedGC9A01
from gc9a01_constants import *

def draw_eye_refined(sim, blink_progress, gaze_x, gaze_y):
    sim.fillScreen(GC9A01A_BLACK)

    cx, cy = 120, 120

    # 1. Sclera (White part)
    sim.fillCircle(cx, cy, 60, GC9A01A_WHITE)

    # 2. Iris (Blue part) - shifted by gaze
    sim.fillCircle(cx + gaze_x, cy + gaze_y, 25, GC9A01A_BLUE)

    # 3. Pupil (Black part) - shifted by gaze
    sim.fillCircle(cx + gaze_x, cy + gaze_y, 12, GC9A01A_BLACK)

    # 4. Blinking effect: cover the eye with black rectangles from top and bottom
    cover = 60 * blink_progress

    # Top eyelid
    sim.fillRect(0, 0, 240, cy - 60 + cover, GC9A01A_BLACK)
    # Bottom eyelid
    sim.fillRect(0, cy + 60 - cover, 240, 240, GC9A01A_BLACK)

class EyeAnimation:
    def __init__(self, sim):
        self.sim = sim
        self.progress = 0.0
        self.state = "OPEN"  # "OPEN", "CLOSING", "CLOSED", "OPENING"
        self.wait_timer = 0

        # Gaze properties
        self.gaze_x = 0
        self.gaze_y = 0
        self.target_gaze_x = 0
        self.target_gaze_y = 0
        self.gaze_shift_timer = 0

    def update_gaze(self):
        # Smoothly interpolate towards target gaze
        self.gaze_x += (self.target_gaze_x - self.gaze_x) * 0.1
        self.gaze_y += (self.target_gaze_y - self.gaze_y) * 0.1

        # Periodically change target gaze
        self.gaze_shift_timer -= 1
        if self.gaze_shift_timer <= 0:
            # Target a random position within a reasonable range (e.g., +/- 20 pixels)
            self.target_gaze_x = random.randint(-20, 20)
            self.target_gaze_y = random.randint(-15, 15)
            self.gaze_shift_timer = random.randint(30, 100)

    def update(self):
        # Update gaze movement
        self.update_gaze()

        # Update blink state machine
        if self.state == "OPEN":
            if self.wait_timer <= 0:
                self.state = "CLOSING"
            else:
                self.wait_timer -= 1

        elif self.state == "CLOSING":
            self.progress += 0.15
            if self.progress >= 1.0:
                self.progress = 1.0
                self.state = "CLOSED"
                self.wait_timer = 5

        elif self.state == "CLOSED":
            if self.wait_timer <= 0:
                self.state = "OPENING"
            else:
                self.wait_timer -= 1

        elif self.state == "OPENING":
            self.progress -= 0.15
            if self.progress <= 0.0:
                self.progress = 0.0
                self.state = "OPEN"
                self.wait_timer = random.randint(40, 120) # random time between blinks

        draw_eye_refined(self.sim, self.progress, self.gaze_x, self.gaze_y)
        self.sim.update_display()

def main():
    root = tk.Tk()
    root.title("Eye Animation Simulator")

    sim = SimulatedGC9A01()
    sim.renderToTk(root)

    eye = EyeAnimation(sim)

    def animate():
        eye.update()
        root.after(40, animate)

    animate()
    root.mainloop()

if __name__ == "__main__":
    main()
