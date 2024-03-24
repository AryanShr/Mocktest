import tkinter as tk
from tkinter import filedialog
import fitz
from PIL import Image, ImageTk

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    if file_path:
        doc = fitz.open(file_path)
        for i in range(len(doc)):
            for img in doc.get_page_images(i):
                xref = img[0]
                base = doc.extract_image(xref)
                img = Image.open(io.BytesIO(base["image"]))
                photo = ImageTk.PhotoImage(img)
                label = tk.Label(image=photo)
                label.image = photo
                label.pack()

root = tk.Tk()
open_button = tk.Button(root, text='Open PDF', command=open_file)
open_button.pack()
root.mainloop()
