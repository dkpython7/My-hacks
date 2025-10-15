from ultralytics import YOLO
model = YOLO('yolov8n.pt')
results = model('image.jpg')
results[0].show()
