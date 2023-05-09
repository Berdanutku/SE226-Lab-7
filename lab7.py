import cv2
img=cv2.imread(r"C:\Users\berda\PycharmProjects\pythonProject\pa.jpg",cv2.IMREAD_COLOR)
cv2.imshow("The Original",img)
cv2.waitKey(0)

blue,green,red=cv2.split(img)

img1=cv2.merge((blue,green,red))
img2=cv2.merge((blue,red,green))
img3=cv2.merge((red,green,blue))

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

redLower=(0,50,50)
redUpper=(10,255,255)
blueLower=(110,50,50)
blueUpper=(130,255,255)

redMod=cv2.inRange(hsv,redLower,redUpper)
blueMod=cv2.inRange(hsv,blueLower,blueUpper)
mask=cv2.bitwise_or(redMod,blueMod)

imgMod=cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("Red",img1)
cv2.imshow("Green",img2)
cv2.imshow("Blue",img3)

cv2.waitKey(0)

cv2.imshow("The Modified",imgMod)
cv2.imshow("The Original",img)

cv2.waitKey(0)
