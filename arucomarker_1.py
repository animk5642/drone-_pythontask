import cv2

# Load dictionary and create detector
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
aruco_params = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)

# Open webcam
cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect markers
    corners, ids, rejected =  detector.detectMarkers(frame)

    # If found, draw and print
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)


        # print(corners[0][0])        # Get center of first marker
        c = corners[0][0]
        center_x = int((c[0][0] + c[2][0]) / 2)
        center_y = int((c[0][1] + c[2][1]) / 2)
        
        print(f"ID: {ids[0][0]}, Center: ({center_x}, {center_y})")
        cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

    cv2.imshow("ArUco Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()