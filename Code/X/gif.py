import cv2
import numpy as np


class gifmodel:

    def playgif(self,frame):
        #Se reemplaza el valor de X obtenido en main
        file="./Gifs/video-"+frame+".gif"
        frameTime=100
        while True:

            isclosed=0
            cap = cv2.VideoCapture(file)
            #cap=cv2.resize(cap, (400, 400)) 
            while (True):

                ret, frame = cap.read()

                if ret == True:

                    cv2.imshow('Asistente',frame)
                    if cv2.waitKey(frameTime) & 0xFF == ord('q'):
                        break
                    if cv2.waitKey(1) == 27:

                        isclosed=1
                        break
                else:
                    break

            if isclosed:
                break

        cap.release()
        cv2.destroyAllWindows()

    def __init__(self, info):
        self.playgif(info)


#g=gifmodel('1-2')