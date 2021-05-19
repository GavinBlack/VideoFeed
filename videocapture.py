import cv2
import random
cap = cv2.VideoCapture(1)

pixels = []

def getInputs(pixels):
    xPix = input("Enter the x: ")
    yPix = input("Enter the y: ")
    pixels.append(xPix)
    pixels.append(yPix)
    return pixels

#pixels = getInputs(pixels)
#cap.set(3,int(pixels[0]))
#cap.set(4,int(pixels[1]))
cap.set(3,60)
cap.set(4,60)

def liveVideoFeed():   #WIP
    gray = False
    normal = True
    while True:
        ret, frame = cap.read()
        if normal:
            cv2.imshow('Spy Camera', frame)
        if gray:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Spy Camera', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1) & 0xFF == ord('s'):
            count = random.randint(0, 100000)
            file = 'C:/Users/Black/OneDrive/Desktop/Screenshots/img' + str(count) + '.jpg'
            cv2.imwrite(file, frame)
            print("Took screenshot, labeled: " + "img" + str(count) + ".jpg")
        elif cv2.waitKey(1) & 0xFF == ord('g'):
            if not gray:
                gray = True
                normal = False
            else:
                gray = False
                normal = True


liveVideoFeed()

cap.release()
cv2.destroyAllWindows()