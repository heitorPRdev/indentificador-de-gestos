import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

while True:
    check,img = webcam.read()
    if check:
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        resultado = Hand.process(imgRGB)
        handsPoints = resultado.multi_hand_landmarks
        h,w,p = img.shape
        pontos = []
        if handsPoints:
            for points in handsPoints:
                mpDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS)
                for id,cord in enumerate(points.landmark):
                    cx,cy = int(cord.x*w),int(cord.y*h)
                    cv2.putText(img,str(id), (cx,cy+10), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0), 2)
                    pontos.append((cx,cy))
        dedos = [8,12,16,20]
        
        if pontos:
            for x in dedos:
                if pontos[4][0] < pontos[2][0] and pontos[x][1] > pontos[x-2][1]:
                   print('Gesto:joinha\nSignificado:ok\n')
                elif pontos[4][0] > pontos[2][0] and pontos[8][1] < pontos[5][1] and pontos[12][1] < pontos[9][1] and  pontos[16][1] > pontos[13][1] and  pontos[20][1] > pontos[17][1]:
                    print('Gesto:vezinho\nSignificado:paz\n')
                elif pontos[4][0] < pontos[2][0] and pontos[8][1] > pontos[5][1] and pontos[12][1] > pontos[9][1] and  pontos[16][1] > pontos[13][1] and  pontos[20][1] < pontos[17][1]:
                    print('Gesto:Hang loose\nSignificado:tudo tranquilo\n')
                
                else:
                    print('nem um gesto indentificado')
      
        cv2.imshow('imagem', img)
        if cv2.waitKey(1) == ord('f'):
            break
webcam.release