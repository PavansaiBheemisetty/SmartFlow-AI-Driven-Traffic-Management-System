import cv2

def extract_frames(video_path, frame_rate=25):
    """
    Extracts frames from a video at a specified frame rate.
    :param video_path: Path to the video file
    :param frame_rate: Extract one frame every 'frame_rate' frames
    :return: List of extracted frames
    """
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_rate == 0:
            frames.append(frame)
        frame_count += 1
    
    cap.release()
    return frames
