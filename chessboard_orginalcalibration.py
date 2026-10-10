# import cv2
# import os

# # Create folder to save images
# if not os.path.exists("calibration_images1"):
#     os.makedirs("calibration_images1")

# # Chessboard settings (9x6 = 9 columns, 6 rows)
# CHESSBOARD = (9, 6)

# # Open webcam
# cap = cv2.VideoCapture(2)
# count = 0

# print("Press SPACE to save an image. Press Q to quit.")
# print("Move the chessboard to different angles and distances.")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Try to find chessboard corners
#     found, corners = cv2.findChessboardCorners(gray, CHESSBOARD, None)

#     if found:
#         cv2.drawChessboardCorners(frame, CHESSBOARD, corners, found)
#         cv2.putText(frame, "FOUND - Press SPACE to save", (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#     else:
#         cv2.putText(frame, "Searching...", (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

#     cv2.imshow("Calibration Capture", frame)

#     key = cv2.waitKey(1) & 0xFF

#     if key == ord(' '):
#         if found:
#             filename = f"calibration_images1/img_{count}.jpg"
#             cv2.imwrite(filename, frame)
#             count += 1
#             print(f"Saved: {filename}")

#     if key == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# print(f"\nTotal images saved: {count}")
# print("Now run calibrate_camera.py")


import cv2

CHESSBOARD = (9, 6)
cap = cv2.VideoCapture(2)
count = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    found, corners = cv2.findChessboardCorners(gray, CHESSBOARD, None)

    display = frame.copy()
    if found:
        cv2.drawChessboardCorners(display, CHESSBOARD, corners, found)
        cv2.putText(display, "FOUND - press SPACE to save", (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("capture", display)
    key = cv2.waitKey(1) & 0xFF

    if key == ord(' ') and found:   # only saves when a pattern is actually confirmed
        cv2.imwrite(f"calibration_images1/img_{count}.jpg", frame)
        print(f"Saved img_{count}.jpg")
        count += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()