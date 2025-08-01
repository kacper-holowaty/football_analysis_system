# Football Analysis System

## 1. Training the model
For training the model, I used the dataset available here: https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1. It contains various scenes from football matches, enabling the detection of players, referees, goalkeepers and the ball.

The instructions and code used for training are saved in the file `training/football_training_yolo_v5.ipynb`. You can train the model yourself or download it from here: [best.pt](https://drive.google.com/file/d/1YNJ21Vrr-wlLxmvKEbmQ5ONT2FHhWK3A/view?usp=drive_link). The trained model should be placed in the `models` directory.

## 2. Exploring how YOLO works with object detection based on video
Before we begin, we still need an input file - a video based on which we will perform object detection.
An example input video file is available here: [Example Input Video](https://drive.google.com/file/d/1jW4OuN-KLoiaPrYchXYdIi3IxgrKJCEk/view?usp=drive_link).  It should be downloaded and placed in the `input_videos` directory.
We execute the code available in the file `yolo_inference.py`. The result of executing this code is available here: [output_video_v1.avi](https://drive.google.com/file/d/1y_WDv9ub4y9-CTPnE8ZuIwL0xWbV2Xxp/view?usp=drive_link)

## 3. Adding tracking to players, referees and the ball
In this section, I implement the `Tracker` class, which uses the `YOLO` model to detect objects in a sequence of frames and tracks them between frames using the `ByteTrack` algorithm from the Supervision library.The detected objects (players, referees, and the ball) are assigned unique identifiers and visualized on the video — players are marked with ellipses drawn beneath them, while the ball is indicated with a small triangle.
The preliminary result of this action is available here: [output_video_v2.avi](https://drive.google.com/file/d/1zKfecuWywcJYb9hn1lJwdw-rDs9A-Jq3/view?usp=drive_link)

## 4. Assigning players to teams by jersey colors
In this section, I implement the `TeamAssigner` class, which uses the `K-Means` algorithm to analyze the jersey colors of players and automatically assign them to one of two teams. First, K-Means (with 2 clusters) groups the pixels from the upper part of each player’s silhouette to identify the dominant jersey color. Then, a second K-Means clustering step classifies all players into two teams based on these extracted colors. An example visualization of this process can be found in the file: `team_assigner/jersey_color_clustering_example.py`.
The result of this action is available here: [output_video_v3.avi](https://drive.google.com/file/d/1e9_UryUNL4LYPsiGIamHn6dakf295jST/view?usp=drive_link)

## 5. Ball interpolation and possession assignment
Sometimes the ball is not detected for several consecutive frames, making continuous tracking impossible. To address this issue, interpolation and backfilling based on data from surrounding frames are applied. As a result, even if the model fails to detect the ball in a particular frame, its approximate position is preserved, allowing for smooth tracking of the ball’s trajectory.

In this section, the ball is also assigned to the nearest player by checking which player is closest to the center of the ball, based on the distance from the player’s feet (i.e., the bottom of their bounding box). Helper functions are used to calculate the center of the ball's bounding box and the distance between points. If a player is within a 60-pixel radius of the ball, the ball is assigned to that player. This logic is implemented in the `PlayerBallAssigner` class.

This player-ball assignment turned out to be particularly useful for calculating the ball possession percentage for both teams. The results are visualized on the video using a semi-transparent white rectangle displaying the current possession statistics (up to the current frame) for Team 1 and Team 2. OpenCV is used for drawing and overlaying the text on the video.
The result of this action is available here: [output_video_v4.avi](https://drive.google.com/file/d/1aDkSSTNmP1jDnhRwKn1HoeVyAvoqPJs_/view?usp=drive_link)

## 6. Camera movement estimator
In this section, I implement the `CameraMovementEstimator` class, which estimates the camera movement (displacement along the X and Y axes) by tracking points across consecutive video frames. It also allows correcting the positions of tracked objects relative to this movement and visualizes the detected displacements on the frames. This makes it possible to separate the camera motion from the movement of objects in the scene. The result of this action is available here: [output_video_v5.avi](https://drive.google.com/file/d/1ZFFIAzMfjkU0J_AC6fDxWcW_DldEPzIg/view?usp=drive_link)

## 7. Speed and distance estimator
This section implements the `SpeedAndDistanceEstimator` class, which calculates the speed (in km/h) and distance traveled (in meters) of objects based on their positions across consecutive frames at specified time intervals. It can then draw these values (speed and distance) on the video frames near the feet of the tracked objects, excluding the ball and referees. The result of this action is available here: [output_video_final.avi](https://drive.google.com/file/d/14QUN_diEoftDrPJ2qZ2_sIHjqiWzR3xR/view?usp=drive_link). At this point, this is the final result of the working code.

> **Note:** ⚠️ This project is still a work in progress and has several issues. 
