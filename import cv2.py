

from ultralytics import YOLO

model = YOLO('yolov8n.pt')

def run_inference(cv_img):
    results = modle(cv_img, stream=True)

    for r in results:
        annotated_frame = r.plot()

        cv2.imshow("CARLA YOLO DETECTION", annotated_frame)
        cv2.waitKey(1)


