# Picture.py
import jes4py as jes
from tkinter import filedialog, Label
from PIL import Image, ImageTk, ImageEnhance

class Picture:
    def __init__(self, master):
        self.master = master
        self.image_label = None
        self.image_path = None
        self.image = None

    def load_image(self):
        self.image_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.image_path:  # Check if a file was selected
            self.display_image()

    def display_image(self):
        if self.image_label:
            self.image_label.destroy()

        self.image = Image.open(self.image_path)
    
    # Get the frame dimensions
        frame_width = self.master.winfo_width()
        frame_height = self.master.winfo_height()

    # Calculate the new size to maintain aspect ratio
        image_ratio = self.image.width / self.image.height
        frame_ratio = frame_width / frame_height

        if image_ratio > frame_ratio:
        # Fit to width
            new_width = frame_width
            new_height = int(frame_width / image_ratio)
        else:
        # Fit to height
            new_height = frame_height
            new_width = int(frame_height * image_ratio)

    # Resize the image
        resized_image = self.image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Update the display
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label = Label(self.master, image=photo)
        self.image_label.image = photo
        self.image_label.pack()


    def lighten_image(self):
        try:
            converter = ImageEnhance.Brightness(self.image)
            # Increase brightness by a factor of 1.5
            self.image = converter.enhance(1.5)
            self.update_image_display()  # Update the image on the UI
        except Exception as e:
            print(f"Error lightening image: {e}")

    def update_image_display(self):
        # Convert the PIL Image to a format that can be displayed in Tkinter
        photo = ImageTk.PhotoImage(self.image)
        # Update the image label with the new image
        self.image_label.config(image=photo)
        self.image_label.image = photo
