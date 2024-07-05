import cv2
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
loc= r"C:\Users\jai\Desktop\text_reg\2.png"
# Read the image
image = cv2.imread(loc)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection using Canny edge detector
edges = cv2.Canny(gray, 50, 150)

# Perform dilation to enhance the edges
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilated_edges = cv2.dilate(edges, kernel, iterations=1)

# Find contours in the edge-detected image
contours, _ = cv2.findContours(dilated_edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over contours and extract text regions
ntxt= []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    roi = image[y:y+h, x:x+w]
    
    # Perform text recognition using Tesseract on the extracted region
    text = pytesseract.image_to_string(roi)
    
    # Print the recognized text
    print("Recognized Text in Region:")
    print(text)
    ntxt.append(text)
    while "" in ntxt:
        ntxt.remove("")

# Show the edge-detected image
cv2.imshow('Edge-detected Image', edges)
print(ntxt)
cv2.waitKey(0)
cv2.destroyAllWindows()
