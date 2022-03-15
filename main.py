import cv2
import pyttsx3

def talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.setProperty("rate", 200)
    engine.runAndWait()
    engine.say(text)
    engine.runAndWait()
def reco():
    thres = 0.65  # Threshold to detect object

    check = []
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    cap.set(10, 70)
    classNames = []
    classFile = 'coco.names.txt'
    with open(classFile,'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')

        configPath = 'D:\pragatheeshwar\Smart India Hack\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt.txt'
        weightsPath = 'D:\\pragatheeshwar\\Smart India Hack\\frozen_inference_graph.pb'

        net = cv2.dnn_DetectionModel(weightsPath, configPath)
        net.setInputSize(320, 320)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        while True:
            success, img = cap.read()
            classIds, confs, bbox = net.detect(img, confThreshold=thres)
            #print(classIds, bbox)

            if len(classIds) != 0:
                for classId, confidence, box,i in zip(classIds.flatten(), confs.flatten(), bbox,bbox):
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    #cv2.putText(img, str(i), (box[0] + 10, box[1] + 30),
                                #cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    check.append(classIds[0])


                    start_point = (14000,0)
                    end_point = (0,250)
                    color = (0, 255, 0)
                    thickness = 2
                    cv2.line(img,start_point,end_point,color,thickness)
                if check.count(classIds[0]) <= 2:
                    talk(str(classNames[classIds[0] - 1])+" detected in few meters")
            cv2.imshow("Output", img)
            cv2.waitKey(1)

print("listening: ")
for i in range(100000000):
    pass
talk("Opening object detection module")
reco()