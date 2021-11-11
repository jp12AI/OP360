# OP360
True 360 degree vision for openpilot

Openpilot 360 is comprised of 3 models (for now)

The first model determines when to stop, go, and slow down at intersections.

The second and third models determine when it is safe to perform a lane change through two side mounted usb cameras. 

Each of these models have been trained on 1,200 image individually and have an accuracy rate of over 90%. 

The models are labeled Left, Right, and Intersection.

# Model Outputs 
Left and Right model outputs: Safe or Unsafe 

Intersection model outputs: Stop, Slow, Go, and Not applicable (for when there is no light or predictions needed)

# Live Model Testing Made Easy (with webcam as tensorflow.js model)
1) Follow the setup instructions here to setup: https://github.com/lobe/web-bootstrap 

2) Clone this repository

3) Copy the contents of one of the desired Tensorflow JS models (as labeled), clear/delete the contents of the public/model folder in the websocket folder, and then paste the contents of the model into the folder. 

4) yarn start and then select the desired camera. 

5) The models were trained to work with cameras mounted on the side front of a vehicle and a camera facing outside the windshield. There's no use in testing the models without the cameras in these orientations/enviroment. I routed the webcam wire through my car window but be creative. Collect data if you can and then send them in the discord server. 

NOTE: ONNX models won't work with this testing solution. These are for integration into openpilot. The models were adapted to tensorflow for live testing purposes. Also, the interface on localhost takes about 30 seconds to load so be patient. 

![Screenshot from 2021-11-11 10-47-14](https://user-images.githubusercontent.com/58639429/141352433-0363d82b-812f-42b9-b45a-c957ed6fdbcf.png)


# The goal can be broken up into 4 stages: 
Stage 1: Train and release models (opensource)

Stage 2: Integrate the models into openpilot to use there outputs as indicators in the UI 

Stage 3: Increase the model accuracy and training data

Stage 4: have openpilot make decisions based on the model outputs and work on guidance by navigation (plannerad modification)

Having openpilot guided by naivgation through modifying plannerad is a long term goal. 

This openpilot setup is intended to be run on a mini pc based on this concept: 

https://github.com/commaai/openpilot/tree/master/tools/webcam 

# Important 
None of the models are currently integrated into openpilot. I'm working to enlist developers to help with this proccess in our discord server. 

# Useful Links: 
https://github.com/commaai/openpilot

https://comma-ai.medium.com/self-driving-car-for-free-82e871fe0587

# OP360 discord server: 
https://discord.gg/mb3FkgnqEc 



