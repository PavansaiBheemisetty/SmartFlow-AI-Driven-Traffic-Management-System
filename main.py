import cv2
import time
from lane_management import manage_traffic  # Your traffic logic
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

# Path to input video
video_path = "videos/rush.mp4"

# Open video file
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

# Frame rate control (adjust as needed)
frame_delay = int(1000 / cap.get(cv2.CAP_PROP_FPS))  # Milliseconds per frame

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        print("End of video stream.")
        break

    # Run YOLOv8 for object detection
    results = model(frame)

    # Extract detected objects
    vehicle_counts = {"car": 0, "bus": 0, "truck": 0, "motorbike": 0}
    
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]

            # Filter for vehicles only
            if label in vehicle_counts:
                vehicle_counts[label] += 1

                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display vehicle count
    count_text = f"Car: {vehicle_counts['car']}, Bus: {vehicle_counts['bus']}, " \
                 f"Truck: {vehicle_counts['truck']}, M-bike: {vehicle_counts['motorbike']}"
    
    cv2.rectangle(frame, (10, 10), (350, 50), (0, 0, 0), -1)  # Background
    cv2.putText(frame, count_text, (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Lane signal info (Example: Assume lane 1 is green)
    green_signal_lane = 1
    signal_text = f"Green Signal: Lane {green_signal_lane}"
    cv2.rectangle(frame, (10, 60), (250, 90), (0, 0, 0), -1)
    cv2.putText(frame, signal_text, (15, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show the frame in an OpenCV window
    cv2.imshow("Traffic Management System", frame)

    # Wait for frame_delay ms, and exit if 'q' is pressed
    if cv2.waitKey(frame_delay) & 0xFF == ord('q'):
        break

# Release video and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
#madda gudu dengeyy ra puka
