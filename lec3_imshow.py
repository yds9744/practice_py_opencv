import cv2

image = cv2.imread("images/lunar.jpg", cv2.IMREAD_ANYCOLOR)
cv2.imshow("Moon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
