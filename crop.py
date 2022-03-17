import cv2 as cv


def compare(original, crop):
    difference = cv.subtract(original, crop)
    b, g, r = cv.split(difference)
    print("bgr diffrence:"+str((cv.countNonZero(b)+cv.countNonZero(g)+cv.countNonZero(r))/3))
    print("==============================")
    if (cv.countNonZero(b)+cv.countNonZero(g)+cv.countNonZero(r))/3<30000:
        return True
    else:
        return False


original = cv.imread("original.jpg")
crop_image = cv.imread("crop.jpg")
originalHeight, originalWidth, originalZ = original.shape
cropHeight, cropWidth, cropZ = crop_image.shape
print("height: "+ str(cropHeight)+"\nwidth: "+str(cropWidth))
flag = True
for i in range(originalHeight-cropHeight):
    for j in range(originalWidth-cropWidth):
        newCrop = original[i:i+cropHeight, j:j+cropWidth]
        if compare(crop_image, newCrop):
            cv.rectangle(original, (j + cropWidth, i + cropHeight),(j, i), (255, 0, 0), 5)
            cv.imshow("result", original)
            flag = False
        if not flag:
            break
    if not flag:
        break

cv.waitKey(0)
