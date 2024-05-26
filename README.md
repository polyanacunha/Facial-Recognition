# Face Recognition

## Installation

### Requirements

  * Python 3.3+ or Python 2.7
  * macOS or Linux (Windows not officially supported, but might work)


#### Installing on Mac Linux

First, make sure you have dlib already installed with Python bindings:

  * [How to install dlib from source on macOS or Ubuntu](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)
  
Then, make sure you have cmake installed:  
 
```brew install cmake```

Finally, install this module from pypi using `pip3` (or `pip2` for Python 2):

```bash
pip3 install face_recognition
```

## To start to test run these command first:

## Build the main dlib library (optional if you just want to use Python):

cd dlib
mkdir build; cd build; cmake ..; cmake --build .

## activate virtual env python :
python3.11 -m venv .
. ./bin/activate
## Build and install the Python extensions:

cd ..
pip install -r requirements.txt

## how to run the files :
poetry run python facerec_from_video_file.py


##### Speeding up Face Recognition

Face recognition can be done in parallel if you have a computer with
multiple CPU cores. For example, if your system has 4 CPU cores, you can
process about 4 times as many images in the same amount of time by using
all your CPU cores in parallel.

If you are using Python 3.4 or newer, pass in a `--cpus <number_of_cpu_cores_to_use>` parameter:

```bash
$ face_recognition --cpus 4 ./pictures_of_people_i_know/ ./unknown_pictures/
```

You can also pass in `--cpus -1` to use all CPU cores in your system.


## Python Code Examples

All the examples are available [here](https://github.com/ageitgey/face_recognition/tree/master/examples).

#### Facial Features

* [Identify specific facial features in a photograph](https://github.com/ageitgey/face_recognition/blob/master/examples/find_facial_features_in_picture.py)
* [Apply (horribly ugly) digital make-up](https://github.com/ageitgey/face_recognition/blob/master/examples/digital_makeup.py)

#### Functions in Facial Recognition

* [Find and recognize unknown faces in a photograph based on photographs of known people](https://github.com/ageitgey/face_recognition/blob/master/examples/recognize_faces_in_pictures.py)
* [Identify and draw boxes around each person in a photo](https://github.com/ageitgey/face_recognition/blob/master/examples/identify_and_draw_boxes_on_faces.py)
* [Compare faces by numeric face distance instead of only True/False matches](https://github.com/ageitgey/face_recognition/blob/master/examples/face_distance.py)
* [Recognize faces in live video using your webcam - Simple / Slower Version (Requires OpenCV to be installed)](https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam.py)
* [Recognize faces in live video using your webcam - Faster Version (Requires OpenCV to be installed)](https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py)
* [Recognize faces in a video file and write out new video file (Requires OpenCV to be installed)](https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_video_file.py)
* [Recognize faces on a Raspberry Pi w/ camera](https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_on_raspberry_pi.py)
* [Run a web service to recognize faces via HTTP (Requires Flask to be installed)](https://github.com/ageitgey/face_recognition/blob/master/examples/web_service_example.py)
* [Recognize faces with a K-nearest neighbors classifier](https://github.com/ageitgey/face_recognition/blob/master/examples/face_recognition_knn.py)
* [Train multiple images per person then recognize faces using a SVM](https://github.com/ageitgey/face_recognition/blob/master/examples/face_recognition_svm.py)

## Creating a Standalone Executable
If you want to create a standalone executable that can run without the need to install `python` or `face_recognition`, you can use [PyInstaller](https://github.com/pyinstaller/pyinstaller). However, it requires some custom configuration to work with this library. See [this issue](https://github.com/ageitgey/face_recognition/issues/357) for how to do it.

## Articles and Guides that cover `face_recognition`

- Article on how Face Recognition works: [Modern Face Recognition with Deep Learning](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78)
  - Covers the algorithms and how they generally work
- [Face recognition with OpenCV, Python, and deep learning](https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/) by Adrian Rosebrock
  - Covers how to use face recognition in practice
- [Raspberry Pi Face Recognition](https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/) by Adrian Rosebrock
  - Covers how to use this on a Raspberry Pi
- [Face clustering with Python](https://www.pyimagesearch.com/2018/07/09/face-clustering-with-python/) by Adrian Rosebrock
  - Covers how to automatically cluster photos based on who appears in each photo using unsupervised learning

## How Face Recognition Works

If you want to learn how face location and recognition work instead of
depending on a black box library, [read my article](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78).

# To have more information, go to the face_recognition lib repository 

- https://github.com/ageitgey/face_recognition/tree/master
