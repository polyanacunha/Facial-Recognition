import cv2
import numpy as np
import matplotlib.pyplot as plt

# Initialize video capture
video_capture = cv2.VideoCapture(0)  # Replace '0' with video file path if not from camera

# Create a matplotlib figure for plotting histograms
plt.ion()  # Enable interactive mode
fig, ax = plt.subplots()

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate histogram using 256 bins and the full range of pixel values
    hist = cv2.calcHist([gray_frame], [0], None, [256], [0, 256])

    # Clear the current plot
    ax.clear()
    ax.plot(hist)
    ax.set_title('Grayscale Histogram')
    ax.set_xlim([0, 256])

    # Display the frame
    cv2.imshow('Video', frame)

    # Draw the histogram
    plt.draw()
    plt.pause(0.001)  # Pause briefly to allow update

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_capture.release()
cv2.destroyAllWindows()
plt.close()
