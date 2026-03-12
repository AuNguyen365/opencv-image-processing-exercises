import cv2
import numpy as np

gray = cv2.imread("photo.jpg", cv2.IMREAD_GRAYSCALE)

if gray is None:
    print("Không đọc được ảnh!")
    exit()

def clip_uint8(arr):
    return np.clip(arr, 0, 255).astype(np.uint8)

# ảnh tối
gray_dark = clip_uint8(gray.astype(np.int32) - 50)

# ảnh sáng
gray_bright = clip_uint8(gray.astype(np.int32) + 50)

# tăng tương phản
gray_contrast = clip_uint8(gray.astype(np.int32) * 1.5)

# threshold
T = 128
binary = np.where(gray >= T, 255, 0).astype(np.uint8)

# lưu ảnh
cv2.imwrite("dark.jpg", gray_dark)
cv2.imwrite("bright.jpg", gray_bright)
cv2.imwrite("contrast.jpg", gray_contrast)
cv2.imwrite("binary.jpg", binary)

# in pixel
print("Pixel trước:", gray[100,100])
print("Pixel sau:", gray_dark[100,100])
print("test git")