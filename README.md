# Contour Detection
This code is used for contour detection of certain contour/shape in image. The code will detect the shape/contour that has 5 side 

## Detailed

### Image Processing
Image processing is very important and determining the success of contour detection. Image processing consists of :
- Converting from colored image to grayscale image (`cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`)
- Edge detection using Canny (`cv2.Canny(gray,50,150)`)

### Finding Contour
Finding all contours in image can be done using `cv2.findContours(imgcnt,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)`. The method will return all the contours in list form.

### Looping
Looping is used to detect each of the contours. Each of the contours is then checked if it has 5 side contours using `cv2.approxPolyDP(c,0.01*peri,True)`
