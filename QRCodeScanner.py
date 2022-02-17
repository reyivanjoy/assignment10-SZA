import cv2
import numpy as np 
from datetime import datetime
from pyzbar.pyzbar import decode

capture = cv2.VideoCapture(0)
capture.set(3,700)
capture.set(4,700)

while True:
    success, frame = capture.read()
    for barcode in decode(frame):
        dataInformation = barcode.data.decode("utf-8")
        
        timeAndDate = datetime.now()
        timeAndDateF = timeAndDate.strftime("Date: %B-%d-%Y\nTime: %H:%M:%S")
        
        txtFile = open("DataInformation.text", "w")
        txtFile.write(f"{dataInformation}\n{timeAndDateF}")
        
        print(f"{dataInformation}\n{timeAndDateF}")
        
    cv2.imshow("Results", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
            cv2.destroyAllWindows()
            break
