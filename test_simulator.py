import tkinter as tk
from gc9a01_simulator import SimulatedGC9A01
from gc9a01_constants import *

root = tk.Tk()  # Crée la fenêtre principale

tft = SimulatedGC9A01()
tft.renderToTk(root)  # Initialise le canvas et l'affichage

def step_text():


    tft.fillScreen(GC9A01A_BLACK)
    tft.setCursor(50, 20)
    tft.setTextColor((255, 255, 255))
    tft.setTextSize(1)
    tft.println("Hello World!")
    tft.println("Texte")
    tft.setTextColor(GC9A01A_YELLOW)
    tft.setTextSize(2)
    tft.println(1234.56)
    tft.setTextColor(GC9A01A_RED)
    tft.update_display()

    tft.println()
    tft.setTextColor(GC9A01A_GREEN)
    tft.setTextSize(5)
    tft.println("Groop")
    tft.setTextSize(2)
    tft.println("I implore thee,")
    tft.setTextSize(1)
    tft.println("my foonting turlingdromes.")
    tft.println("And hooptiously drangle me")
    tft.println("with crinkly bindlewurdles,")
    tft.println("Or I will rend thee")
    tft.println("in the gobberwarts")
    tft.println("with my blurglecruncheon,")
    tft.println("see if I don't!")
    tft.update_display()
    root.after(6000, step_anim)





def step_anim():
    tft.fillScreen(GC9A01A_BLACK)

    tft.setTextColor((255, 255, 255))
    tft.setTextSize(1)
    tft.setCursor(5, 5)
    tft.printText("Text size 1")

    tft.setTextSize(2)
    tft.setCursor(10, 30)
    tft.printText("Size 2")

    tft.drawRoundRect(10, 60, 100, 40, 10, (0, 255, 0))
    tft.fillRoundRect(120, 60, 100, 40, 10, (0, 0, 255))

    tft.drawCircle(60, 140, 20, (255, 0, 0))
    tft.fillCircle(180, 140, 20, (255, 255, 0))
    tft.drawLine(10, 200, 230, 200, (255, 255, 255))
    tft.update_display()
    root.after(2000, step_black)

def step_black():
    tft.fillScreen(GC9A01A_BLACK)
    tft.update_display()
    root.after(1000, step_red)  # appelera la suite après 1 seconde

def step_red():
    tft.fillScreen(GC9A01A_RED)
    tft.update_display()
    root.after(1000, step_green)

def step_green():
    tft.fillScreen(GC9A01A_GREEN)
    tft.update_display()
    root.after(1000, step_blue)

def step_blue():
    tft.fillScreen(GC9A01A_BLUE)
    tft.update_display()
    root.after(1000, step_final_black)

def step_final_black():
    tft.fillScreen(GC9A01A_BLACK)
    tft.update_display()
    root.after(1000, rotation)

def rotation():
    tft.fillScreen(GC9A01A_RED)
    tft.setRotation(1)
    tft.setCursor(10, 10)
    tft.println("Rotated!")
    tft.update_display()


# Démarre l'enchaînement
step_text()

# Lancer la boucle Tkinter
root.mainloop()
