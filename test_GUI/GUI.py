import tkinter as tk
from tkinter import font
from PIL import Image
import numpy as np
import sys
import os
import time
import qrcode
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
import gspread
import datetime
import cv2
import numpy as np
import json
import datetime
from datetime import datetime
#import picamera
#import picamera.array
#from   picamera . array   import   PiRGBArray 
#from   picamera  import   PiCamera 

scopes = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
json_file = r'C:\Users\HN4-00012\Documents\Bridge\face-id-022a16cbf2d0.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scopes=scopes)
http_auth = credentials.authorize(Http())

doc_id = '1f0wXrRdXSR2TJ_RoFZ3sv66UnZNBRJb0UlaBjHDFMrw'
SPREADSHEET_KEY = '1f0wXrRdXSR2TJ_RoFZ3sv66UnZNBRJb0UlaBjHDFMrw'
client = gspread.authorize(credentials)
gfile = client.open_by_key(doc_id)
gc = gspread.authorize(credentials)
worksheet = gfile.sheet1

worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

dt_now = datetime.today()
print(dt_now)


headers = ['name', 'birth', 'sex']

def decode():
    def edit_contrast(image, gamma):
        """コントラクト調整"""
        look_up_table = [np.uint8(255.0 / (1 + np.exp(-gamma * (i - 128.) / 255.)))
            for i in range(256)]

        result_image = np.array([look_up_table[value]
                                 for value in image.flat], dtype=np.uint8)
        result_image = result_image.reshape(image.shape)
        return result_image


    if __name__ == "__main__":
        capture = cv2.VideoCapture(0)
        #capture = picamera.PiCamera(0)
        #if capture.isOpened() is False:
            #raise("IO Error")

        while True:
            ret, frame = capture.read()
            qr = cv2.QRCodeDetector()
            if ret == False:
                continue
        
        # グレースケール化してコントラクトを調整する
            gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            image = edit_contrast(gray_scale, 5)

        # 加工した画像からフレームQRコードを取得してデコードする
        #codes = decode(image)
            data, points, straight_qrcode = qr.detectAndDecode(image)


            if len(data) > 0:
            
                print(data)
                
               # data2 = json.loads(data)
                worksheet.append_row([str(data)])
                worksheet.append_row([data])

                #column = []
                #for header in headers:
                 #   column.append(data2[header])

                #Swks.append_row(column)
                print('読み取りが完了しました。')
                label2.config(text="読み取りが完了しました、ご来店ありがとうございます")
                break
        
            else :
                print('読み取れません。もう一度かざしてください。')
                label2.config(text="読み取りができませんでした。もう一度お願いします。")
            



        capture.release() 
        cv2.destroyAllWindows() 


root = tk.Tk()
root.title("スタンプ")
root.geometry("500x500")





button3 = tk.Button(root,text="【スタンプする】",height=5,command=decode)
button3.pack()


font1 = font.Font(family='Helvetica', size=6, weight='bold')
label2 = tk.Label(root,fg="white", bg="black", font=font1)
label2.pack(side="top")



root.mainloop()


  

   


