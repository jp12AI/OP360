# OP360
True 360 degree vision for openpilot

Openpilot 360 is comprised of two Tensorflow Lite models (for now).

The goal of these models is to determine when it is safe to perform a lane change through two side mounted usb cameras. 

Each of these models have been trained on 1,200 images individually and have an accuracy rate of over 90%. 

The models are labeled saved_model_left and saved_model_right.

The concept.py script is what I intened to use as a baseline for integrating the output of the models into the mentioned UI below. 

# Model Outputs 
Left and Right model outputs: Safe or Unsafe 

# Model Testing and use
There are three python scripts in this repository. Detect_left.py & Detect_right.py are for model testing. Be sure to have the required python libraries installed. 
To perform testing: Download/clone this repositroy, update the path to the models and label files on your device, make sure you have a camera plugged in, and then run the script with python. 

# The goal can be broken up into 4 stages: 
Stage 1: Train and release models (opensource)

Stage 2: Integrate the models into this UI: https://github.com/299299/tesla_hmi 

Stage 3: Integrate the tesla_hmi UI as the UI for openpilot itself (not running beside).

Stage 4: Create a practical and easy to integrate product to collect data and use collected data to further train better and more sophisiticated models. 

Stage 5: have openpilot make decisions based on the model outputs and work on guidance by navigation (plannerad modification)

Having openpilot guided by naivgation through modifying plannerad is a long term goal. 

This openpilot setup is intended to be run on a mini pc based on this concept: 

https://github.com/commaai/openpilot/tree/master/tools/webcam 

# Update 11/28/21: 
None of the models are currently integrated into openpilot. Working on the UI aspect currently. 

# Useful Links: 
https://github.com/commaai/openpilot

https://comma-ai.medium.com/self-driving-car-for-free-82e871fe0587

# Want to contribute? Join our OP360 discord server: 
https://discord.gg/mb3FkgnqEc 



