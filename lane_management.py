import cv2
import threading
from vehicle_counting import count_vehicles
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

def draw_overlay(frame, lane, vehicle_counts, green_signal_lane):
    """
    Draw bounding boxes, vehicle counts, and lane signal information on the frame.
    """
    # Detect objects
    results = model(frame)
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            conf = float(box.conf[0])  # Confidence score
            cls = int(box.cls[0])  # Class ID
            label = model.names[cls]  # Object label

            # Filter only vehicle classes
            if label in ["car", "truck", "bus", "motorbike"]:
                color = (0, 255, 0) if lane == green_signal_lane else (0, 0, 255)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Get vehicle counts with default values (0 if key not found)
    count_text = f"Car: {vehicle_counts.get('car', 0)}, Bus: {vehicle_counts.get('bus', 0)}, " \
                 f"Truck: {vehicle_counts.get('truck', 0)}, M-bike: {vehicle_counts.get('motorbike', 0)}"

    cv2.rectangle(frame, (10, 10), (300, 50), (0, 0, 0), -1)
    cv2.putText(frame, count_text, (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Display lane signal
    signal_text = f"Green Signal: Lane {green_signal_lane}"
    cv2.rectangle(frame, (10, 60), (250, 90), (0, 0, 0), -1)
    cv2.putText(frame, signal_text, (15, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    return frame


def manage_traffic(video_paths):
    """
    Displays real-time video with detected vehicles and dynamic lane signaling.
    """
    lane_counts = {lane: 0 for lane in video_paths}  # Store vehicle counts for each lane
    lane_occurrences = {lane: 0 for lane in video_paths}  # Track how many times a lane has received green

    # Open video streams
    caps = {lane: cv2.VideoCapture(path) for lane, path in video_paths.items()}

    while True:
        lane_dict = {}

        # Run vehicle detection for each lane in parallel
        threads = []
        for lane, path in video_paths.items():
            t = threading.Thread(target=lambda: lane_dict.update({lane: count_vehicles(path)}))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        # Determine which lane gets green signal
        green_signal_lane = max(lane_dict, key=lane_dict.get)
        lane_counts[green_signal_lane] = 0  # Reset count after green signal
        lane_occurrences[green_signal_lane] += 1

        # Read and process frames for display
        for lane, cap in caps.items():
            ret, frame = cap.read()
            if not ret:
                continue

            # Process frame with overlay
            frame = draw_overlay(frame, lane, lane_dict, green_signal_lane)

            # Display the processed video
            cv2.imshow(f"Lane {lane}", frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    for cap in caps.values():
        cap.release()
    cv2.destroyAllWindows()
