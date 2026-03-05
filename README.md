# ComVision 01주차 실습
# OpenCV 실습 과제

## 0101. 이미지 불러오기 및 그레이스케일 변환
- **설명**: 이미지를 불러오고 흑백으로 변환 후 나란히 출력
- **요구사항**:
  - cv.imread()              :이미지 로드
  - cv.cvtColor()            :이미지를 그레이스케일로 변환
  - np.hstack()              :원본 이미지와 그레이스케일 이미지를 가로로 연결하여 출력
  - cv.imshow(), cv.waitKey():결과를 화면에표시, 아무 키나 누르면 창이 닫히도록
- **코드**
  ```python
  ```
- **주요코드**
  ```python
  ```
- **결과물**:
<img width="2845" height="1675" alt="image" src="https://github.com/user-attachments/assets/52f65b68-9aee-4d6a-98fc-d148ec49061e" />



## 0102. 페인팅 붓 크기 조절
- **설명**: 마우스 클릭으로 그림을 그리고, `+`, `-` 키로 붓 크기를 1~15까지(초기 5) 조절
- **요구사항**:
  - 좌클릭(B)
  - 우클릭(R)
  - 드래그로 연속 그리기
  - 창 종료(q)
- **코드**
  ```python
  ```
- **주요코드**
  ```python
  ```
- **결과물**: 
<img width="2835" height="1799" alt="image" src="https://github.com/user-attachments/assets/88470528-8b0f-4e0d-b065-94e54aa3b6f1" />
<img width="1015" height="388" alt="image" src="https://github.com/user-attachments/assets/74258ccc-b7f6-4b61-bf13-6fba43118472" />


## 0103. ROI(관심영역) 추출
- **설명**: 마우스 드래그로 영역을 선택하고 영역만 저장 혹은 표시
- **요구사항**:
  - cv.setMouseCallback()을사용하여마우스이벤트를처리
  - 사용자가클릭한시작점에서드래그하여사각형을그리며영역을선택
  - 마우스를놓으면해당영역을잘라내서별도의창에출력
  - r :선택을리셋하고처음부터다시선택
  - s :선택한영역을이미지파일로저장
- **코드**
  ```python
  ```
- **주요코드**
  ```python
  ```
- **결과물**:
<img width="2807" height="1651" alt="image" src="https://github.com/user-attachments/assets/464e49c5-f099-4f86-aa9b-882522d9c916" />
<img width="1805" height="1474" alt="image" src="https://github.com/user-attachments/assets/269e71c5-7c22-4fef-bc4a-26165a52e88b" />



