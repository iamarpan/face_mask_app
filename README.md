# face_mask_app

This app was developed using yolov5 for face mask detection.

Dataset: 
The model was trained on face mask dataset present on kaggle: https://www.kaggle.com/andrewmvd/face-mask-detection

### Model: ###
ultralytics/yolov5 model was used to train on the dataset and runs files were generated for them.

### Data Preparation: ###
The code base contains files to convert xml file to yolov5 format and also to divide the dataset into train and validation set.

### Preprequisite: ###
1) Make sure to install yolov5 in your local system.

### Run the code: ###
To run the inference on videos use the below command
* python yolov5/detect.py --source {file path of video} --weights {runs/train/exp4/weights/best.pt} --conf 0.25
-> pretrained weights are already provided in my code repo.

To run the inference on images use the below command
* python yolov5/detect.py --source {file path of image} --weights {runs/train/exp4/weights/best.pt} --conf 0.25
-> pretrained weights are already provided in my code repo.

To run the inference on live video using webcam
* python yolov5/detect.py --source 0 --weights {runs/train/exp4/weights/best.pt} --conf 0.25
-> pretrained weights are already provided in my code repo.



