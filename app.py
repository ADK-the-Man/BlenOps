from flask import Flask, render_template, request, jsonify, send_from_directory
import subprocess
import os
import time

app = Flask(__name__)

# Define directories
BASE_DIR = "/app"
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
BLENDER_SCRIPT_PATH = os.path.join(BASE_DIR, "update_text_render.py")

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    new_text = request.form['new_text']
    
    # Run Blender in background to render the video
    blender_command = f'blender --background --python {BLENDER_SCRIPT_PATH} -- "{new_text}"'
    subprocess.Popen(blender_command, shell=True)
    
    return render_template('progress.html', filename=f"{new_text}.mp4")

@app.route('/progress/<filename>')
def progress(filename):
    file_path = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(file_path):
        return jsonify({'status': 'done', 'download_url': f'/download/{filename}'})
    else:
        return jsonify({'status': 'rendering'})

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
