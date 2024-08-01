import customtkinter as ctk
from PIL import Image, ImageTk

from Picture import Picture

ctk.set_appearance_mode("dark")  # Set the UI mode
ctk.set_default_color_theme("blue")  # Set the color theme

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Storytelling App")
        self.geometry("800x600")

        # Configure the grid to distribute space equally
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Main frame setup
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, sticky="nsew", columnspan=2, rowspan=2)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Initialize buttons
        self.create_button("assetes/images/text.png", "Text", self.on_text, 0, 0)
        self.create_button("assetes/images/pic.png", "Image", self.on_image, 0, 1)
        self.create_button("assetes/images/sound.png", "Sound", self.on_sound, 1, 0)
        self.create_button("assetes/images/movie.png", "Video", self.on_video, 1, 1)

    def create_button(self, icon_path, text, action, row, col):
        frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        frame.grid(row=row, column=col, padx=20, pady=20, sticky="nsew")

        img = Image.open(icon_path).resize((200, 180), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        icon_label = ctk.CTkLabel(frame, image=photo, text="")
        icon_label.image = photo
        icon_label.pack(pady=(20, 5))

        button = ctk.CTkButton(frame, text=text, command=lambda: self.change_content(action))
        button.pack(pady=(5, 20))

    def change_content(self, action):
    # Clear all widgets from the main_frame using destroy to remove all geometry management
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # Execute the action to update the content
        action()

    def create_initial_buttons(self):
    # Clear existing content properly before creating new buttons
        for widget in self.main_frame.winfo_children():
            widget.destroy()  # Ensuring all widgets are removed

    # Recreate the initial buttons
        self.create_button("assetes/images/text.png", "Text", self.on_text, 0, 0)
        self.create_button("assetes/images/pic.png", "Image", self.on_image, 0, 1)
        self.create_button("assetes/images/sound.png", "Sound", self.on_sound, 1, 0)
        self.create_button("assetes/images/movie.png", "Video", self.on_video, 1, 1)

    def add_back_button(self):
    # Position the back button at the bottom or another specific place
        back_button = ctk.CTkButton(self.main_frame, text="Back", command=self.create_initial_buttons)
        back_button.pack(pady=1, padx=5)  # Using pack here as well to place the button below the label


    def on_text(self):
    # Clear all widgets from the main_frame using destroy to remove all geometry management
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        

        self.add_back_button()


    def on_image(self):
    # Clear all widgets from the main_frame using destroy to remove all geometry management
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # Create an instance of the Picture class, handling image operations
        self.picture_handler = Picture(self.main_frame)
    
    # Add a button to load and display the image
        load_button = ctk.CTkButton(self.main_frame, text="Load Image", command=self.picture_handler.load_image)
        load_button.pack(pady=10)

    # Add a button to lighten the image
        lighten_button = ctk.CTkButton(self.main_frame, text="Lighten", command=self.picture_handler.lighten_image)
        lighten_button.pack(pady=10, padx=10)
    
    # Add back button at the bottom
        self.add_back_button()

    def on_sound(self):
    # Clear all widgets from the main_frame using destroy to remove all geometry management
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # New Content from here on 
        label = ctk.CTkLabel(self.main_frame, text="Sound multimedia content here")
        label.pack(pady=20, padx=20)  # Using pack for simplicity in single widget scenarios

        self.add_back_button()

    def on_video(self):
    # Clear all widgets from the main_frame using destroy to remove all geometry management
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # New Content from here on 
        label = ctk.CTkLabel(self.main_frame, text="Movie multimedia content here")
        label.pack(pady=20, padx=20)  # Using pack for simplicity in single widget scenarios
        #create_movie(self.main_frame)
        self.add_back_button()

if __name__ == "__main__":
    app = App()
    app.mainloop()
