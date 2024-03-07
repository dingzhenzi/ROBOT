import cv2
img=cv2.imread('D:\image-20221027164357622.png')#‘ ’内改成电脑对应的图片路径
cur_img=img.copy()
cur_img[:,:,2]=0
gray=cv2.cvtColor(cur_img,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 15)
ret,thresh=cv2.threshold(gray,37,255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt=contours[2]
x,y,w,h=cv2.boundingRect(cnt)
print(x,y)
text="%d,%d" % (x, y)
img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.putText(img,text, (171,420 ), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
cv2.imshow("1",img)
cv2.waitKey(0)