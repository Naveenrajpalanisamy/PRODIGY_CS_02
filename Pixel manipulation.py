import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

def load_image():
    global img, img_array, img_display
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img_display = ImageTk.PhotoImage(img)
    img_array = np.array(img)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_display)

def save_image(img_array):
    result_img = Image.fromarray(img_array)
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    result_img.save(save_path)

def encrypt_image():
    global img_array, img_display
    key = 100  # Simple encryption key
    encrypted_array = (img_array + key) % 256  # Simple encryption by adding the key value
    img_display = ImageTk.PhotoImage(Image.fromarray(encrypted_array))
    canvas.create_image(0, 0, anchor=tk.NW, image=img_display)
    img_array = encrypted_array

def decrypt_image():
    global img_array, img_display
    key = 100  # Same key as used in encryption
    decrypted_array = (img_array - key) % 256  # Simple decryption by subtracting the key value
    img_display = ImageTk.PhotoImage(Image.fromarray(decrypted_array))
    canvas.create_image(0, 0, anchor=tk.NW, image=img_display)
    img_array = decrypted_array

# Setting up the GUI window
root = tk.Tk()
root.title("Image Encryption Tool")

# Canvas to display the image
canvas = tk.Canvas(root, width=900, height=800)
canvas.pack()

# Buttons for operations
load_btn = tk.Button(root, text="Load Image", command=load_image)
load_btn.pack(side=tk.LEFT)

encrypt_btn = tk.Button(root, text="Encrypt Image", command=encrypt_image)
encrypt_btn.pack(side=tk.LEFT)

decrypt_btn = tk.Button(root, text="Decrypt Image", command=decrypt_image)
decrypt_btn.pack(side=tk.LEFT)

save_btn = tk.Button(root, text="Save Image", command=lambda: save_image(img_array))
save_btn.pack(side=tk.LEFT)

# Start the GUI event loop
root.mainloop()
