import time
import threading
from ultralytics import YOLO
import cv2
import numpy as np
from polygon import draw_polygon, draw_dram_polygon, inside_polygon
import chime

# Path to the alarm sound
path_alarm = "alarmm.m4a"

def play_alarm():
    chime.play_wav(path_alarm)

# Loading the model
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("thief_video.mp4")

target_classes = [0,2]       #person, car

pts = draw_dram_polygon("thief_video.mp4")

count = 0
number_of_photos = 3

while True:
    ret, frame = cap.read()

    results = model(frame, conf=0.5)

    for point in pts:
        cv2.circle(frame, point, 5, (0, 0, 255), -1)

    cv2.line(frame, pts[0], pts[1], (0, 255, 0), 2)
    cv2.line(frame, pts[2], pts[0], (0, 255, 0), 2)
    cv2.line(frame, pts[3], pts[2], (0, 255, 0), 2)
    cv2.line(frame, pts[1], pts[3], (0, 255, 0), 2)



    for pred in results[0].boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = pred
        if int(class_id) in target_classes:
            # Visualize the results on the frame
            annotated_frame = results[0].plot()
            frame = cv2.bitwise_and(annotated_frame, frame)
            center_x = (x2 + x1) / 2
            center_y = (y2 + y1) / 2


            pts = np.array(pts)
            if inside_polygon((center_x, center_y), pts) :

                cv2.putText(frame, "Person Detected", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                # Uncomment if you want to save detected photos
                if count < number_of_photos:
                   cv2.imwrite("Detected Photos/detected" + str(count) + ".jpg", frame)
                   count += 1

                # Uncomment if you want to play an alarm sound
                threading.Thread(target=play_alarm).start()
    cv2.imshow("Video", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()