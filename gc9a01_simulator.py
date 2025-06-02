import math
from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
from tkinter import Canvas


class SimulatedGC9A01:
    def __init__(self, width=240, height=240):
        self.tk_root = None
        self.canvas = None
        self.tk_img = None
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (width, height), "black")
        self.draw = ImageDraw.Draw(self.image)
        self.cursor_x = 0
        self.cursor_y = 0
        self.text_color = (255, 255, 255)
        self.text_size = 1
        self.font = self.load_font()

    def load_font(self):
        try:
            return ImageFont.truetype("DejaVuSansMono.ttf", 8)
        except:
            return ImageFont.load_default()

    # Convertit couleur 16 bits 5-6-5 en tuple RGB 8 bits
    def color565_to_rgb(self, color565):
        r = (color565 >> 11) & 0x1F
        g = (color565 >> 5) & 0x3F
        b = color565 & 0x1F
        r8 = int((r * 255) / 31)
        g8 = int((g * 255) / 63)
        b8 = int((b * 255) / 31)
        return (r8, g8, b8)



    def setCursor(self, x, y):
        r = self.width // 2
        cx, cy = r, r  # centre du cercle

        # Calculer la distance du point au centre
        dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
        if dist > r:
            # Si hors du cercle, repositionner sur le bord du cercle
            angle = math.atan2(y - cy, x - cx)
            self.cursor_x = int(cx + r * math.cos(angle))
            self.cursor_y = int(cy + r * math.sin(angle))
        else:
            self.cursor_x = x
            self.cursor_y = y

    def setTextColor(self, color):
        if isinstance(color, int):
            color = self.color565_to_rgb(color)
        self.text_color = color

    def setTextSize(self, size):
        self.text_size = max(1, size)

    def printText(self, text):
        text = str(text)  # Convertir le texte en une chaîne de caractères

        if self.text_size == 1:
            font = self.font
        else:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 8 * self.text_size)

        for c in text:
            self.draw.text((self.cursor_x, self.cursor_y), c, font=font, fill=self.text_color)
            self.cursor_x += self.text_size * 6  # Ajuster selon la largeur du caractère

    def println(self, text=""):
        self.printText(text)
        line_height = 8 * self.text_size
        self.setCursor(0, self.cursor_y + line_height)

    def fillScreen(self, color):
        if isinstance(color, int):
            color = self.color565_to_rgb(color)
        self.draw.rectangle([0, 0, self.width, self.height], fill=color)

    def drawPixel(self, x, y, color):
        if isinstance(color, int):
            color = self.color565_to_rgb(color)
        self.draw.point((x, y), fill=color)

    def drawLine(self, x0, y0, x1, y1, color):
        if isinstance(color, int):
            color = self.color565_to_rgb(color)
        self.draw.line([x0, y0, x1, y1], fill=color)

    def drawRect(self, x, y, w, h, color):
        if isinstance(color, int):
            color = self.color565_to_rgb(color)
        self.draw.rectangle([x, y, x + w, y + h], outline=color)

    def fillRect(self, x, y, w, h, color):
        if isinstance(color, int):
            color = self.color565_to_rgb(color)
        self.draw.rectangle([x, y, x + w, y + h], fill=color)

    def drawCircle(self, x, y, r, color):
        if isinstance(color, int):
            color = self.color565_to_rgb(color)
        self.draw.ellipse([x - r, y - r, x + r, y + r], outline=color)

    def fillCircle(self, x, y, r, color):
        if isinstance(color, int):
            color = self.color565_to_rgb(color)
        self.draw.ellipse([x - r, y - r, x + r, y + r], fill=color)

    def drawRoundRect(self, x, y, w, h, r, color):
        if isinstance(color, int):
            color = self.color565_to_rgb(color)
        self.draw.rectangle([x + r, y, x + w - r, y + h], outline=color)
        self.draw.rectangle([x, y + r, x + w, y + h - r], outline=color)
        self.draw.arc([x, y, x + 2 * r, y + 2 * r], 180, 270, fill=color)
        self.draw.arc([x + w - 2 * r, y, x + w, y + 2 * r], 270, 360, fill=color)
        self.draw.arc([x, y + h - 2 * r, x + 2 * r, y + h], 90, 180, fill=color)
        self.draw.arc([x + w - 2 * r, y + h - 2 * r, x + w, y + h], 0, 90, fill=color)

    def fillRoundRect(self, x, y, w, h, r, color):
        if isinstance(color, int):
            color = self.color565_to_rgb(color)
        self.draw.rectangle([x + r, y, x + w - r, y + h], fill=color)
        self.draw.rectangle([x, y + r, x + w, y + h - r], fill=color)
        self.draw.pieslice([x, y, x + 2 * r, y + 2 * r], 180, 270, fill=color)
        self.draw.pieslice([x + w - 2 * r, y, x + w, y + 2 * r], 270, 360, fill=color)
        self.draw.pieslice([x, y + h - 2 * r, x + 2 * r, y + h], 90, 180, fill=color)
        self.draw.pieslice([x + w - 2 * r, y + h - 2 * r, x + w, y + h], 0, 90, fill=color)

    def drawChar(self, x, y, c, color=None):
        if color is None:
            color = self.text_color
        self.draw.text((x, y), c, fill=color, font=self.font)

    def create_circular_mask(self, size):
        mask = Image.new('L', (size, size), 0)  # mode L = niveaux de gris (noir=0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)  # cercle blanc (zone visible)
        return mask

    def setRotation(self, rotation):
        self.rotation = rotation % 4  # rotation doit être entre 0 et 3

    def _apply_rotation(self, x, y):
        if self.rotation == 0:
            return x, y
        elif self.rotation == 1:
            return self.height - y - 1, x
        elif self.rotation == 2:
            return self.width - x - 1, self.height - y - 1
        elif self.rotation == 3:
            return y, self.width - x - 1

    def update_display(self):
        if self.canvas is None:
            raise RuntimeError("Canvas not initialized. Call renderToTk(tk_root) first.")

        # Appliquer le masque circulaire à nouveau
        mask = self.create_circular_mask(self.width)
        circ_image = Image.new("RGBA", (self.width, self.height))
        circ_image.paste(self.image, (0, 0), mask=mask)

        self.tk_img = ImageTk.PhotoImage(circ_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)
        self.canvas.image = self.tk_img  # Conserver la référence

    def renderToTk(self, tk_root):
        # Appliquer masque circulaire
        mask = self.create_circular_mask(self.width)
        circ_image = Image.new("RGBA", (self.width, self.height))
        circ_image.paste(self.image, (0, 0), mask=mask)

        self.canvas = tk.Canvas(tk_root, width=self.width, height=self.height)
        self.canvas.pack()

        self.tk_img = ImageTk.PhotoImage(circ_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)

        # Conserver la référence pour éviter le garbage collection
        self.canvas.image = self.tk_img


# Exemple d'utilisation dans une fenêtre Tkinter
if __name__ == "__main__":
    from gc9a01_constants import *

    root = tk.Tk()
    sim = SimulatedGC9A01()

    sim.fillScreen(GC9A01A_BLUE)
    sim.drawCircle(120, 120, 100, GC9A01A_YELLOW)
    sim.fillCircle(120, 120, 90, GC9A01A_RED)
    sim.setTextColor(GC9A01A_WHITE)
    sim.setCursor(50, 110)
    sim.printText("Hello GC9A01!")

    photo = sim.renderToTk(root)

    canvas = Canvas(root, width=sim.width, height=sim.height)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=photo)

    canvas.image = photo  # <-- ✅ Ajoute cette ligne pour garder une référence à l'image

    root.mainloop()
