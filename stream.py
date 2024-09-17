import cv2

# GStreamer pipeline with libcamera for Raspberry Pi camera (adjust width, height, and framerate as needed)
gst_pipeline = (
    "libcamerasrc ! video/x-raw,width=640,height=480,framerate=30/1 ! "
    "videoconvert ! appsink"
)

cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Error: Couldn't open the GStreamer pipeline.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
