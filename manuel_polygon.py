#kordinatları bulmak için manuel deneme
import numpy as np
import cv2

video = cv2.VideoCapture("thief_video.mp4")

ret, frame = video.read()

if ret:
 # Manuel olarak poligon koordinatlarını belirleme
 pts = np.array([[260, 250], [460, 200], [540, 2500], [240, 1000]], np.int32)
 pts = pts.reshape((-1, 1, 2))

 cv2.fillPoly(frame, [pts], (0, 255, 0))

 # Görüntüyü gösterme
 cv2.imshow("First Frame with Polygon", frame)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
else:
    print("Video dosyasından kare alınamadı!")