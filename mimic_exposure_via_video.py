import cv2
import numpy as np
from PIL import Image

def average_video_frames(input_video_path, output_image_path):
    # Open the video file
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Error: Unable to open the video file.")
        return

    # Initialize variables to store the total pixel values and frame count
    total_pixels = None
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Break the loop when we've processed all frames

        if total_pixels is None:
            total_pixels = np.array(frame, dtype=np.float32)
        else:
            total_pixels += frame.astype(np.float32)

        frame_count += 1

    # Calculate the average frame
    average_frame = (total_pixels / frame_count).astype(np.uint8)

    # Convert the average frame to a PIL image
    average_image = Image.fromarray(cv2.cvtColor(average_frame, cv2.COLOR_BGR2RGB))

    # Save the resulting image
    average_image.save(output_image_path)

    # Release the video capture object
    cap.release()

if __name__ == "__main__":
    input_video_path = input("Video path: ")  # Replace with the path to your input video
    output_image_path = "output_image.png"  # Replace with the desired output image path

    average_video_frames(input_video_path, output_image_path)
    print(f"Average image saved to {output_image_path}")
