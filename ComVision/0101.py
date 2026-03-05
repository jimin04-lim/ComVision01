import cv2 as cv
import numpy as np 

img = cv.imread(r"C:\Users\a0105\Documents\ComVision\girl_laughing.jpg")

if img is None:
    print("오류: 이미지를 로드할 수 없습니다. 파일명과 경로를 확인하세요.")
else:
    print("이미지 로드 성공!")
    cv.imshow('Test', img)
    cv.waitKey(0)
    cv.destroyAllWindows()