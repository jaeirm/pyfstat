from PIL import Image
import pytesseract as pyt
import cv2
pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
loc= r"C:\Users\jai\Desktop\text_reg\3.png"
img = cv2.imread(loc)
img = cv2.resize(img,(1200,1200))
retval, threshold = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)   
# cv2.imshow("Original Image", img) 
txt = pyt.image_to_string(threshold)
print(txt)
cv2.imshow("Threshold", threshold)  
cv2.waitKey(0) 
f=open("text3.txt","w")
f.write(txt)
f.close()