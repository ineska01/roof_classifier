from ultralytics import YOLO


model = YOLO("yolov8n.pt")
results = model(0, show=True) 