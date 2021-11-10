# OP360
True 360 degree vision for openpilot 
Openpilot 360 is comprised of 3 models (for now) 
The first model determines when to stop, go, and slow down at intersections. 
The second and third models determine when it is safe to perform a lane change through two side mounted usb cameras. 
Each of these models have been trained on 1,200 image individually and have an accuracy rate of over 90%. 
The models are labeled 1, 2, and 3. 

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



