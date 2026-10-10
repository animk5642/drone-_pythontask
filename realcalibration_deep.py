import cv2
import numpy as np
import glob
import os

# Chessboard settings
CHESSBOARD = (9, 6)
SQUARE_SIZE = 27  # Size of each square in mm (adjust to your printed chessboard)

# Prepare object points (0,0,0), (1,0,0), (2,0,0) ...
objp = np.zeros((CHESSBOARD[0] * CHESSBOARD[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHESSBOARD[0], 0:CHESSBOARD[1]].T.reshape(-1, 2)
objp = objp * SQUARE_SIZE  # Convert to mm

# Arrays to store object points and image points
objpoints = []  # 3D points in real world
imgpoints = []  # 2D points in image plane

img = cv2.imread("calibration_images1/img_0.jpg")
cv2.imshow("check", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load all calibration images
images = glob.glob("calibration_images1/*.jpg")

if len(images) < 10:
    print("Need at least 10 images. Capture more.")
    exit()

print(f"Found {len(images)} images")

found = 0
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, CHESSBOARD, None)
    print(f"{fname}: {'FOUND' if ret else 'not found'}")
    if ret:
        found += 1
print(f"\n{found} / {len(images)} images had the pattern detected")

for fname in images:
    # img = cv2.imread(fname)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    ret, corners = cv2.findChessboardCorners(gray, CHESSBOARD, None)

    if ret:
        objpoints.append(objp)

        # Refine corners
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1),
                                     (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
        imgpoints.append(corners2)

# Calibrate camera
ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
    objpoints, imgpoints, gray.shape[::-1], None, None
)

# Print results
print("\n--- Calibration Results ---")
print(f"Reprojection Error: {ret:.4f}")
print(f"\nCamera Matrix:\n{camera_matrix}")
print(f"\nDistortion Coefficients:\n{dist_coeffs}")

# Save to file
np.savez("camera_calibration.npz",
         camera_matrix=camera_matrix,
         dist_coeffs=dist_coeffs)

print("\nSaved to camera_calibration.npz")

# Test undistortion on one image
img = cv2.imread(images[0])
h, w = img.shape[:2]
new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(
    camera_matrix, dist_coeffs, (w, h), 1, (w, h)
)
undistorted = cv2.undistort(img, camera_matrix, dist_coeffs, None, new_camera_matrix)

cv2.imshow("Original", img)
cv2.imshow("Undistorted", undistorted)
cv2.waitKey(0)
cv2.destroyAllWindows()