import numpy as np
import cv2

WIDTH = 600
HEIGHT = 400
PATCH_SIZE = 5

# 이미지 불러오기
img = cv2.imread('sample.JPG', 1)
img = cv2.resize(img, dsize=(WIDTH, HEIGHT))

# 이미지 클릭 시 해당 픽셀(0, 0)으로 하는 패치를 확대출력하는 콜백
def magnify(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        result = np.zeros(shape=(PATCH_SIZE, PATCH_SIZE, 3), dtype=np.uint8)
        for r in range(PATCH_SIZE):
            for c in range(PATCH_SIZE):
                if y+r >= HEIGHT or x+c >= WIDTH:
                    result[r][c][0] = 0
                    result[r][c][1] = 0
                    result[r][c][2] = 0
                else:
                    result[r][c][0] = img[y + r][x + c][0]
                    result[r][c][1] = img[y + r][x + c][1]
                    result[r][c][2] = img[y + r][x + c][2]
        result = cv2.resize(result, dsize=(200, 200), interpolation=cv2.INTER_NEAREST_EXACT)
        cv2.imshow('hey', result)
        cv2.waitKey()


# 콜백함수 등록
cv2.namedWindow("viewer")
cv2.setMouseCallback("viewer", magnify)

# 렌더링
while cv2.waitKey(1) != ord('q'):
    view = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            view[y][x] = img[y][x]
    cv2.imshow("viewer", view)
