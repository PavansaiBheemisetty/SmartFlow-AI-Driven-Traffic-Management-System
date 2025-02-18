
# **Smart Flow AI-driven Traffic Management System**

**Project Overview:**
Smart Flow is an AI-driven traffic management system that uses deep learning techniques to monitor real-time traffic, detect vehicles, and optimize traffic signals. This project leverages YOLOv3-tiny for vehicle detection, tracking, and counting. It aims to provide efficient traffic management at intersections by adjusting traffic signals based on real-time vehicle data.

<img src ='https://images.squarespace-cdn.com/content/v1/53f78d0be4b06aa2bfc2d8da/1450204066544-CURD8Q4Y9J5FNGHCMCBP/ke17ZwdGBToddI8pDm48kD8CuAIZkq9N8hb0i_3XLvYUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYxCRW4BPu10St3TBAUQYVKc89AJUwEjX8DQLiIhOsVfkPWEpIqnx-skx3ZV02U_kD7o301BB-hY3eq-4LA4hOjV/TV_Web_2015_Home_placeholder4a.png?format=1500w'>

---

## **Features:**

- **Real-Time Vehicle Detection:** Detects cars, trucks, buses, and motorcycles using the YOLOv3-tiny model.
- **Vehicle Counting:** Counts the number of vehicles detected in each lane.
- **Dynamic Traffic Signal Management:** Assigns green signals to lanes with the highest vehicle count, ensuring optimal traffic flow.
- **Deadlock Prevention:** Implements a mechanism to avoid deadlock situations by considering lanes that have waited for long periods.
- **Prediction-Based Signal Assignment:** Predicts and assigns green signals based on real-time vehicle counts.
- **Vehicle Tracking:** Continuously tracks vehicles with a bounding box, displaying their probability of being a vehicle.
  <img src ='https://trafficinfratech.com/wp-content/uploads/2022/08/New-Project-2022-08-01T122206.059.jpg'>

---

## **Technologies Used:**

- **Deep Learning:** YOLOv3-tiny for vehicle detection.
- **OpenCV:** For video processing and displaying real-time results.
- **MoviePy:** For video frame extraction and parallel processing.
- **Python:** Programming language used for implementation.

---

## **Installation Instructions:**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Smart-Flow-Traffic-Management.git
   cd Smart-Flow-Traffic-Management
   ```

2. **Install Dependencies:**
   - Install required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLOv8 Model Weights:**
   - Download the YOLOv8 model weights and place them in the project folder.
   ```bash
   wget https://path-to-yolov8-model/yolov8n.pt
   ```

4. **Prepare Input Video:**
   - Place your video file (e.g., `rush.mp4`) in the `videos/` directory.

5. **Run the System:**
   - Run the Python script to start processing the video:
   ```bash
   python traffic_management.py
   ```

---

## **How It Works:**

1. **Video Input:** The system takes a video input of the traffic scene with multiple lanes.
2. **Frame Extraction:** The video is processed frame-by-frame to detect vehicles.
3. **Vehicle Detection:** YOLOv3-tiny is used to detect vehicles (cars, buses, trucks, and motorcycles).
4. **Vehicle Tracking and Counting:** Each detected vehicle is tracked and counted for each lane.
5. **Traffic Signal Management:** The lane with the highest vehicle count is assigned a green signal. The system dynamically updates signals based on vehicle counts.
6. **Deadlock Prevention:** If a lane has not received a green signal for a while, it is given priority to avoid deadlock.

---

## **Future Scope:**

- **Criminal Tracking:** Detect traffic rule violations and alert the nearest police station.
- **Collision Detection:** Predict and prevent potential traffic collisions.
- **Number Plate Recognition:** Integrate number plate recognition for vehicle identification.
- **Emergency Vehicle Detection:** Detect and prioritize emergency vehicles like ambulances and police cars.
