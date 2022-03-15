# Succour-to-Divyang
Today, the world has about 295 million visually impaired people (VIP). VIP are naturally dependent on others to complete their tasks, not just at a physical level but at Psychological level.
In this study, we present a novel framework to assist the VIP in object detection and
recognition, so that they can be aware of their surroundings and navigate independently, GPS and fall detection which keeps their relatives updated of their status. With these the VIPs become more productive and independent.
The white cane is the most popular blind navigating device. This was further improved by the addition of ultrasonic and IR sensors to detect obstacles in the vicinity of the VIP and provide feedback in the form of vibration or sound. Though this approach was useful for the mobility of the visually impaired user, it provided little or no information about the surroundings.
For the user to have a better understanding of the surrounding, objection detection and
classification, followed by recognition and audio feedback is crucial.
Neural networks, particularly, convolutional neural networks have shown promising
results especially in object detection, classification, and recognition tasks from images.
MAIN TECHNIQUES TO BE EMPLOYED:
(i) Image classification
(ii) Object detection
(iii) Image segmentation
IMAGE CLASSIFICATION:
SSD(single-shot detector)Mobilenetv3 a deep learning algorithm which is to be used to extract the most salient features from each frame.
SSD Mobilenetv3 has shown promising results compared to other algorithms like
Alexnet 2012, google net, etc in image classification domain.
Imagenet dataset which is a famous dataset containing 1000 classes, is to be used to
train the module.
OBJECT DETECTION:
Object detection is a combination of:
(i) Classification
(ii) Localization
SSD Mobilenetv3 (latest version) and Yolo v1,v2(compatibility) are the algorithms to be
employed for object detection and facial recognition.
The widely used Coco dataset which contains over 80 classes is to be used for training the module. Image Segmentation:
Image Segmentation is based on salient features.
Each pixel is classified so that the image could be separated and recognized accurately from the background.Cityscape dataset is to be employed for this instance.

GPS TRACKING AND FALL DETECTION:
Google maps API would be integrated to our project which would accurately tell the user the direction and the obstacles in his/her way. Accelerometer in the phone is employed to detect the unusual vibrations, when the person falls and intimates the VIP's relative.
SECURITY:
All the dataset and image recognition algorithms happen in the cloud, thereby ensuring the security and reliability of the proposed system.

