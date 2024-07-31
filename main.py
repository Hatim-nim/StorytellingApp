import customtkinter as ctk
import os
from PIL import Image, ImageTk

ctk.set_appearance_mode("light")  # "dark" is also available
ctk.set_default_color_theme("blue")  # You can change the theme color

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Storytelling App")
        self.geometry("800x600")

        # Layout configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Icons for the buttons
        icons = [
    "assets/images/text.jpg",
    "assets/images/picture_gallery.jpg",
    "assets/images/sound.png",
    "assets/images/movie.jpg"
        ]   
        for icon in icons:
            if not os.path.exists(icon):
                print(f"File not found: {icon}")
            else:
                print(f"File exists: {icon}")        
        button_texts = ["Text", "Image", "Sound", "Video"]
        actions = [self.on_text, self.on_image, self.on_sound, self.on_video]

        # Create buttons with icons
        for i in range(4):
            frame = ctk.CTkFrame(self, corner_radius=10)
            frame.grid(row=i//2, column=i%2, padx=20, pady=20, sticky="nsew")
            
            # Load icon
            img = Image.open(icons[i])
            img = img.resize((50, 50), Image.ANTIALIAS)  # Resize the image
            photo = ImageTk.PhotoImage(img)

            icon_label = ctk.CTkLabel(frame, image=photo)
            icon_label.image = photo  # keep a reference!
            icon_label.pack(pady=(20, 5))

            button = ctk.CTkButton(frame, text=button_texts[i], command=actions[i])
            button.pack(pady=(5, 20))

    def on_text(self):
        print("Text multimedia selected")

    def on_image(self):
        print("Image multimedia selected")

    def on_sound(self):
        print("Sound multimedia selected")

    def on_video(self):
        print("Video multimedia selected")

if __name__ == "__main__":
    app = App()
    app.mainloop()
