# Delivery Drone Simulation in webots

Deakin SIT217 Final Project

## Project Proposal

A drone, given a zone, can (1) move to a zone, avoiding obstacles, (2) locate a marked safe landing spot, (3) land safely, (4) take off again, and (5) return home, avoiding obstacles.  
Additional goals: (1) Once it has taken off, the drone will take a picture to prove delivery. (2) The drone can locate a safe landing spot without zone marking. (3) The drone will carry and unload a payload using a gripper tool.

## Project Deliverables

- A drone, which has...
  - A way of moving around the environment
  - A way of detecting safe landing zones at a property
  - A way of detecting obstacles
  - A way of representing load
  - A way of detecting how far it is from the ground
- A controller, which can...
  - A way of moving the drone around the environment
  - A way of safely taking off and landing the drone
  - A way of using the drone's sensors to detect safe landing zones
  - A way of detecting obstacles and controlling the drone around them
- An environment, which models...
  - Properties to deliver to
  - Safe zones on properties
  - Obstacles the drone must avoid
