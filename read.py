import cv2 as cv

##read img
img = cv.imread('Pics\wallpaperflare.com_wallpaper (1).jpg')
cv.imshow('Cat', img)
cv.waitKey(0)

#read vid
capture = cv.VideoCapture('Vids\model_build_from_scratch.mp4')

# while True:
#     isTrue, frame =  capture.read()
#     cv.imshow('Vid', frame)

#     if cv.waitKey(5) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
