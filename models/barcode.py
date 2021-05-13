import cv2
from pyzbar.pyzbar import decode

class Barcode():
    def __init__(self):
        self.cap = cv2.VideoCapture(0) 
        self.camera = True
        self.book_code = ""

    def scan_code(self):
        while self.camera == True:
            success, frame = self.cap.read()

            for code in decode(frame):
                #print(code.type)
                self.book_code = code.data.decode('utf-8')
                #print(book_code)
            cv2.imshow("Testing-code-scan", frame)
            cv2.waitKey(1)
            if self.book_code != "":
                self.camera == False        
                break
        
        return self.book_code

