import cv2
import numpy as np
points = []

def draw_polygon(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        points.append([x, y])

def draw_dram_polygon(video_path):
    global points
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Video file not found or unable to open.")
        return

    cv2.namedWindow('Draw Polygon')
    cv2.setMouseCallback('Draw Polygon', draw_polygon)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        for point in points:
            cv2.circle(frame, point, 5, (0, 0, 255), -1)


        if len(points) == 4:
            cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
            cv2.line(frame, points[2], points[0], (0, 255, 0), 2)
            cv2.line(frame, points[3], points[2], (0, 255, 0), 2)
            cv2.line(frame, points[1], points[3], (0, 255, 0), 2)
        cv2.imshow('Draw Polygon', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return points

# Function to check if a point is inside a polygon
def inside_polygon(point,polygon):
    result = cv2.pointPolygonTest(polygon, (point[0], point[1]), False)
    if result == 1:
        return True
    else:
        return False




