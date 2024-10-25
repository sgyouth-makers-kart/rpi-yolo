from cv2 import VideoCapture
from ultralytics import YOLO


if __name__ == "__main__":
	cap = VideoCapture(0)
	model = YOLO("yolo11n.pt")

	while True:
		ret, frame = cap.read()
		
		if not ret:
			print("VideoCapture failed")
	
		results = model(frame)
		breakpoint()
		for result in results:
			if len(result.boxes.cls) > 0:
				print(f"{result.names[result.boxes.cls[0].item()]} detected")
			else:
				print("Nothing detected")
