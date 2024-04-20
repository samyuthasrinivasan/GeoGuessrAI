import cv2

for i in range(35):
    #read image
    original_image = cv2.imread(f"spain/bollard/BOLLARD#{i+1}.png")
    newImage = cv2.resize(original_image, (100,200))
    cv2.imwrite("BOLLARD#{i+1}.png", newImage)