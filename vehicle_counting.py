from frame_extraction import extract_frames
from object_detection import detect_vehicles

def count_vehicles(video_path):
    """
    Counts vehicles in a given video.
    :param video_path: Path to the video file
    :return: Total vehicle count
    """
    frames = extract_frames(video_path)
    total_count = sum(detect_vehicles(frame) for frame in frames)
    return total_count
