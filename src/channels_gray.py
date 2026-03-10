import cv2
import numpy as np

img = cv2.imread("photo.jpg")
if img is None:
    print("Error: Cannot read image")
    exit()
print("Color image shape:", img.shape)

B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]

print("Blue channel shape:", B.shape)
print("Green channel shape:", G.shape)
print("Red channel shape:", R.shape)

cv2.imwrite("results/blue.png", B)
cv2.imwrite("results/green.png", G)
cv2.imwrite("results/red.png", R)

# Chuyển sang grayscale (manual)
gray = ((R.astype(float) + G.astype(float) + B.astype(float)) / 3).astype(np.uint8)

print("Gray image shape:", gray.shape)

# Lưu grayscale
cv2.imwrite("results/gray_manual.png", gray)

scale = 0.5 
img_small = cv2.resize(img, None, fx=scale, fy=scale)
B_small = cv2.resize(B, None, fx=scale, fy=scale)
G_small = cv2.resize(G, None, fx=scale, fy=scale)
R_small = cv2.resize(R, None, fx=scale, fy=scale)
gray_small = cv2.resize(gray, None, fx=scale, fy=scale)

cv2.imshow("Small Original Image", img_small)
cv2.imshow("Small Blue Channel", B_small)
cv2.imshow("Small Green Channel", G_small)
cv2.imshow("Small Red Channel", R_small)
cv2.imshow("Small Gray Image (Manual)", gray_small)
# Chờ nhấn phím bất kỳ
cv2.waitKey(0)