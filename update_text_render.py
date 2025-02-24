import bpy
import sys
import os

# Get the command-line arguments after '--'
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # Get all arguments after '--'

new_text = argv[0] if argv else "Default Text"

# Define paths dynamically inside the container
BASE_DIR = "/app"
BLEND_FILE_PATH = os.path.join(BASE_DIR, "blenkins.blend")  # Blender file
OUTPUT_DIR = os.path.join(BASE_DIR, "output")  # Output directory

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load the existing .blend file
bpy.ops.wm.open_mainfile(filepath=BLEND_FILE_PATH)

# Find the text object named 'Text'
text_obj = bpy.data.objects.get("Text")

if text_obj and text_obj.type == 'FONT':
    text_obj.data.body = new_text  # Update text
    print(f"Updated text to: {new_text}")

# Set up rendering settings
output_file = os.path.join(OUTPUT_DIR, f"{new_text}.mp4")
bpy.context.scene.render.filepath = output_file

# Configure render format
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.audio_codec = 'AAC'
bpy.context.scene.render.ffmpeg.audio_bitrate = 192
bpy.context.scene.render.ffmpeg.audio_channels = 'STEREO'

# Render the animation
print("Rendering started...")
bpy.ops.render.render(animation=True)
print(f"Rendering complete. Video saved to: {output_file}")
