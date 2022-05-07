import cv2 as cv


def compare(original, crop):
    difference = cv.subtract(original, crop)
    b, g, r = cv.split(difference)
    return (cv.countNonZero(r)+cv.countNonZero(b)+cv.countNonZero(g))/3


# main
original = cv.imread("original.jpg")
crop_image = cv.imread("crop.jpg")
originalHeight, originalWidth, originalZ = original.shape
cropHeight, cropWidth, cropZ = crop_image.shape
minI, minJ = 0, 0
imageMin = 1100
flag = False
for i in range(originalHeight-cropHeight):
    for j in range(originalWidth-cropWidth):
        newCrop = original[i:i+cropHeight, j:j+cropWidth]
        #print(compare(crop_image, newCrop))
        check = compare(crop_image, newCrop)
        if check < imageMin:
            imageMin = compare(crop_image, newCrop)
            minI = i
            minJ = j
            flag = True
        if flag:
            break
    if flag:
        break

print(imageMin)
cv.rectangle(original, (minJ + cropWidth, minI + cropHeight),
             (minJ, minI), (255, 0, 0), 5)
cv.imshow("result", original)


cv.waitKey(0)
