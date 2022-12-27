import cv2
from pathlib import Path
webcam = cv2.VideoCapture(0)
title = 'mouse event'
x, y = 100, 100


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('fail')

while True:

    key = cv2.waitKey(60)
    if key == 27:
        break
    
cv2.namedWindow('CAM_Window')

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()
    str = '''Image captured! if you want to exit, please press 'q' on keyboard'''
    if status:
        cv2.imshow("test", frame)
    if cv2.waitKey(1) & 0xFF == ord('o'):
        cv2.putText(frame, str, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 100))
        png_list = list(Path('/Users/hyerin_m/Desktop/vscode/').rglob('*.png'))
        c = 0
        for i in png_list:
            num_stem = i.stem.split('_')[-1]
            c+=1
            if c ==1:
                cv2.imwrite(f'file_name_{int(num_stem)+1}.png',frame, params=[cv2.IMWRITE_PNG_COMPRESSION,0])
                img = cv2.imread(f'file_name_{int(num_stem)+1}.png')
                cv2.imshow(f'file_name_{int(num_stem)+1}.png', img)
                c=0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()