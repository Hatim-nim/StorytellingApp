from PIL import Image
import cv2
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip
import tkinter as tk
from tkinter.filedialog import askopenfilename

def select_file(title="Select file", filetypes=(("all files","*.*"),)):
    # Create a root window but hide it from the user
    root = tk.Tk()
    root.withdraw()
    # Open the file dialog
    file_path = askopenfilename(title=title, filetypes=filetypes)
    return file_path

def create_frames(character_path, background_path, num_frames=30, repeats=3):
    # Load images
    character = Image.open(character_path)
    background = Image.open(background_path)

    # Resize character to 25% of its original size
    character_resized = character.resize((character.width // 4, character.height // 4), Image.Resampling.LANCZOS)

    frames = []
    background_width, background_height = background.size
    character_width, character_height = character_resized.size

    # Define the height range for jumping
    jump_heights = np.linspace(0, -50, num_frames//2).tolist() + np.linspace(-50, 0, num_frames//2).tolist()

    # Repeat each jump height multiple times
    extended_jump_heights = []
    for height in jump_heights:
        extended_jump_heights.extend([height] * repeats)

    # Create jumping frames using the extended list
    for height in extended_jump_heights:
        temp_background = background.copy()
        character_x = (background_width - character_width) // 2
        character_y = (background_height - character_height) // 2 + int(height)
        temp_background.paste(character_resized, (character_x, character_y), character_resized)
        frames.append(np.array(temp_background.convert('RGB')))

    return frames

def add_movement_and_pause(frames, character_path, background_path, move_start, move_frames=15):
    character = Image.open(character_path)
    character_resized = character.resize((character.width // 4, character.height // 4), Image.Resampling.LANCZOS)
    background = Image.open(background_path)

    background_width, background_height = background.size
    character_width, character_height = character_resized.size

    # Process movement frames and hold the final position
    for i in range(move_start, move_start + move_frames):
        temp_background = background.copy()
        shift_x = 10 * (i - move_start)
        shift_y = 8 * (i - move_start)
        character_x = (background_width - character_width) // 2 - shift_x
        character_y = (background_height - character_height) // 2 + shift_y
        temp_background.paste(character_resized, (character_x, character_y), character_resized)
        frames[i] = np.array(temp_background.convert('RGB'))

    # Extend the last moved position for the remainder of the video
    final_position_frame = frames[move_start + move_frames - 1]
    for j in range(move_start + move_frames, len(frames)):
        frames[j] = final_position_frame

def save_video(frames, output_path, fps=10):
    height, width, layers = frames[0].shape
    size = (width, height)
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc('m','p','4','v'), fps, size)
    for frame in frames:
        out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    out.release()

def add_audio_to_video(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_path, codec='libx264')

# Use dialogs to get file paths
character_path = select_file("Select the character image", (("Image files", "*.png;*.jpg;*.jpeg"),))
background_path = select_file("Select the background image", (("Image files", "*.png;*.jpg;*.jpeg"),))
audio_path = select_file("Select the audio file", (("Audio files", "*.mp3;*.wav"),))

# Create frames with increased jump frequency
initial_frames = create_frames(character_path, background_path, num_frames=30, repeats=3)
move_start = int(len(initial_frames) * 0.4)  # Calculate when the movement starts as 40% of the total frames

# Add movement and ensure the character stays in the final position
add_movement_and_pause(initial_frames, character_path, background_path, move_start)

# Save the video to a temporary path
temp_video_path = r'M:\Kau\Year 3\Summer Term\380\Project\MyVideo\temp_monkey_jumping.mp4'
save_video(initial_frames, temp_video_path)

# Add audio to the video and save it to the final path
final_video_path = r'M:\Kau\Year 3\Summer Term\380\Project\MyVideo\monkey_jumping_with_audio.mp4'
add_audio_to_video(temp_video_path, audio_path, final_video_path)