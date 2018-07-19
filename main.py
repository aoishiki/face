import cv2

color_red = (0, 0, 225)	#枠の色

if __name__ == '__main__':
	# window
	cv2.namedWindow("face test")
	# webcamera
	cap = cv2.VideoCapture(0)
	# 分類器の指定
	cascadeFile = "data\haarcascade_frontalface_default.xml"
	cascade = cv2.CascadeClassifier(cascadeFile)

	while (True):
		# frameに映像,retに取得できたかどうか
		ret,frame = cap.read()
		# frameの大きさを取得
		height, width, channels = frame.shape
        # 画像の取得と顔の検出
		face_list = cascade.detectMultiScale(frame, minSize=(100, 100))

        # 検出した顔に印を付ける
		for (x, y, w, h) in face_list:
			pen_w = 3
			cv2.rectangle(frame, (x, y), (x+w, y+h), color_red, thickness = pen_w)

        # フレーム表示
		if ret :
			cv2.imshow("ORIGINAL", frame)
		if cv2.waitKey(33) == 27:
			break
		
	cap.release()
	cv2.destroyAllWindows()