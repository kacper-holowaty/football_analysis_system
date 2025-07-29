# Football Analysis System

## 1. Training the model
For training the model, I used the dataset available here: https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1. It contains various scenes from football matches, enabling the detection of players, referees, goalkeepers and the ball.

The instructions and code used for training are saved in the file `training/football_training_yolo_v5.ipynb`. You can train the model yourself or download it from here: [best.pt](https://drive.google.com/file/d/1YNJ21Vrr-wlLxmvKEbmQ5ONT2FHhWK3A/view?usp=drive_link). The trained model should be placed in the `models` directory.

## 2. Exploring how YOLO works with object detection based on video
Before we begin, we still need an input file - a video based on which we will perform object detection.
An example input video file is available here: [Example Input Video](https://drive.google.com/file/d/1jW4OuN-KLoiaPrYchXYdIi3IxgrKJCEk/view?usp=drive_link).  It should be downloaded and placed in the `input_videos` directory.
We execute the code available in the file `yolo_inference.py`. The result of executing this code is available here: [output_video_v1.avi](https://drive.google.com/file/d/1y_WDv9ub4y9-CTPnE8ZuIwL0xWbV2Xxp/view?usp=drive_link)

## 3. Adding tracking to players, referees and the ball (initial phase)
The preliminary result of this action is available here: [output_video_v2.avi](https://drive.google.com/file/d/1zKfecuWywcJYb9hn1lJwdw-rDs9A-Jq3/view?usp=drive_link)

## 4. Assigning colors to players
The result of this action is available here: [output_video_v3.avi](https://drive.google.com/file/d/1e9_UryUNL4LYPsiGIamHn6dakf295jST/view?usp=drive_link)
