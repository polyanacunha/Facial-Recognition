# import subprocess
# from flask import Flask, render_template, jsonify, request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/smile-detection', methods=['POST'])
# def smile_detection():
#     try:
#         return subprocess.Popen(['python', 'smile_detection.py'])
                  
#     except Exception as e:
#         return jsonify(status="error", message=str(e))
    
# @app.route('/histogram', methods=['POST'])
# def create_histogram():
#     try:
#         return subprocess.Popen(['python', 'histogram_from_camera_video.py'])
                  
#     except Exception as e:
#         return jsonify(status="error", message=str(e))
    
# @app.route('/face-recognition', methods=['POST'])
# def face_recognition():
#     try:
#         return subprocess.Popen(['python', 'facerec_from_video_file.py'])
                  
#     except Exception as e:
#         return jsonify(status="error", message=str(e))
    
# @app.route('/blur-faces', methods=['POST'])
# def blur_on_faces():
#     try:
#         return subprocess.Popen(['python', 'blur_faces_on_webcam.py'])
                  
#     except Exception as e:
#         return jsonify(status="error", message=str(e))
    
# @app.route('/enhance-sharpness', methods=['POST'])
# def enhance_sharpness():
#     try:
#         # Extract parameters from the request, assuming JSON input
#         data = request.get_json()
#         image_path = data['./image_with_blur.jpg']
#         output_path = data['output.jpg']
#         sharpness_factor = data['sharpness_factor']

#         # Build the command to run the Python script
#         command = ['python', 'increase_sharpness.py', image_path, output_path, str(sharpness_factor)]
#         print(command)
#         # Start the subprocess
#         subprocess.Popen(command)
        
#         # Return a successful JSON response
#         return jsonify({"status": "success", "message": "Enhancement process started"}), 200
#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500
    
# @app.route('/displacement', methods=['POST'])
# def displacement():
#     try:
#         return subprocess.Popen(['python', 'displacement.py'])
                  
#     except Exception as e:
#         return jsonify(status="error", message=str(e))
    
# @app.route('/periodic-signal', methods=['POST'])
# def periodic_signal():
#     try:
#         return subprocess.Popen(['python', 'periodic_signal.py'])
                  
#     except Exception as e:
#         return jsonify(status="error", message=str(e))

# if __name__ == "__main__":
#     app.run(debug=True)


import subprocess
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

processes = {}

@app.route('/start-process/<process_name>', methods=['POST'])
def start_process(process_name):
    try:
        if process_name in processes:
            processes[process_name].terminate()  # Terminate if already running
        # Example of adding specific scripts to a dictionary for better management
        script_path = {
            'smile-detection': 'smile_detection.py',
            'histogram': 'histogram_from_camera_video.py',
            'face-recognition': 'facerec_from_video_file.py',
            'blur-faces': 'blur_faces_on_webcam.py',
            'enhance-sharpness': 'increase_sharpness.py',  # Example for enhance sharpness
            'displacement': 'displacement.py',
            'periodic-signal': 'periodic_signal.py'
        }.get(process_name)

        if not script_path:
            return jsonify(status="error", message="Invalid process name"), 400

        # Running the subprocess
        proc = subprocess.Popen(['python', script_path])
        processes[process_name] = proc
        return jsonify(status="success", message=f"{process_name} started"), 200
    except Exception as e:
        return jsonify(status="error", message=str(e)), 500

@app.route('/stop-process', methods=['POST'])
def stop_process():
    try:
        data = request.get_json()
        process_name = data.get('process_name')
        if process_name in processes:
            processes[process_name].terminate()
            return jsonify(status="success", message=f"{process_name} stopped"), 200
        return jsonify(status="error", message="Process not found"), 404
    except Exception as e:
        return jsonify(status="error", message=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True)
