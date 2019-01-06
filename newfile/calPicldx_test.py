import cv2
import numpy
import random
import math

src = cv2.imread("E:\\code\\py_tools\\test.jpg")
print(src.shape)
h = src.shape[0]
w = src.shape[1]
c = src.shape[2]

row = 3
col = 3

offset_h = h/row
offset_w = w/col

firstClick = False
clickIdx = [0,0]

tileList = []
def calPicIdx(x, y):
    print(str(y)+" "+str(h/col))
    i = y//(offset_h)
    print(str(y%offset_h)+" "+str(offset_w))
    j = math.ceil((x%w)/offset_w)
    idx = i*row+j
    print("i:"+str(i)+" j:"+str(j)+" idx:"+str(idx))
    return int(idx)

def onMouse(event, x, y, flag ,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        print("left button down:"+str(x)+" "+str(y))
        idx = calPicIdx(x, y)
        global firstClick
        firstClick = not firstClick
        print(firstClick)
        if firstClick:
            clickIdx[0] = idx
        else:
            clickIdx[1] = idx
            tileList[clickIdx[0]], tileList[clickIdx[1]] = tileList[clickIdx[1]], tileList[clickIdx[0]]
            for i in range(0, row):
                for j in range (0, col):
                    dst[i*offset_h:(i+1)*offset_h-1, j*offset_w:(j+1)*offset_w-1] = tileList[i*row+j]
            cv2.imshow("dst", dst)

            difference = cv2.subtract(dst, src2)
            result = not numpy.any(difference) #if difference is all zeros it will return False
            print("result:"+str(result))
        print(clickIdx)

# --------------splite image into n*n tile--------------

tile = numpy.zeros((offset_h-1, offset_w-1, c),numpy.uint8)

for i in range(0, row):
    for j in range (0, col):
        tile = src[i*offset_h:(i+1)*offset_h-1, j*offset_w:(j+1)*offset_w-1]
        tileList.append(tile)
        # cv2.imshow("tile", tile)

# --------------ramdom the tiles--------------------
print(len(tileList))
for i in range(len(tileList)-1,0,-1):
    randomIdx = random.randint(0,i-1)
    print("swap:"+str(random.randint(0,i-1))+" "+str(i))
    tileList[i], tileList[randomIdx] = tileList[randomIdx], tileList[i]

# debug show every tile
# for k,tile in enumerate(tileList):
#   cv.imshow("tile"+str(k), tile)

dst = numpy.zeros((h, w, c), numpy.uint8)
for i in range(0, row):
    for j in range (0, col):
        dst[i*offset_h:(i+1)*offset_h-1, j*offset_w:(j+1)*offset_w-1] = tileList[i*row+j]
cv2.namedWindow("dst")
cv2.setMouseCallback("dst", onMouse)
cv2.imshow("dst", dst)

# -------------match the origin image and now--------------
src2 = src.copy()
for i in range(1, row):
    src2[i*offset_h-1:i*offset_h]= numpy.zeros((1,w,3), numpy.uint8)
    for j in range(1, col):
        src2[0:h,j*offset_w-1:j*offset_w]= numpy.zeros((h,1,3), numpy.uint8)
# cv2.imshow("src2", src2)



cv2.waitKey(0)