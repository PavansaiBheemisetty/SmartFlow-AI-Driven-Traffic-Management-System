from ultralytics import YOLO

# Load YOLOv8n model
model = YOLO("yolov8n.pt") 

def detect_vehicles(frame):
    """
    Detects vehicles using YOLOv8n.
    :param frame: Input frame for detection
    :return: List of detected objects (bounding boxes, labels, confidence)
    """
    results = model(frame)
    detections = results[0].boxes.data.cpu().numpy()  

    vehicle_count = 0
    for box in detections:
        x1, y1, x2, y2, conf, class_id = box
        if int(class_id) in [2, 3, 5, 7]:  # Car, Motorcycle, Bus, Truck
            vehicle_count += 1

    return vehicle_count
