import cv2
import stack
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    


path = "./images/shapes.png"
img = cv2.imread(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, ksize=(7, 7), sigmaX=1)
imgCanny = cv2.Canny(img, 50, 50)
imgBlank = np.zeros_like(img)

# cv2.imshow("Original", img)
# cv2.imshow("imgGray", imgGray)
# cv2.imshow("imgBlur", imgBlur)

imgStack = stack.stackImages(0.6, [[img, imgGray, imgBlur], [imgCanny, imgBlank, imgBlank]])
cv2.imshow("imgStack", imgStack)


cv2.waitKey(0)
