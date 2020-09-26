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

## Product Backlog(for Sprint 2: 9/25-9/28)

*1. Drone*
  1. Use what was learned from DJI Mavic 2 Pro controller to decide on sensors - Ben
  2. Build prototype drone
  
*2. Environment*
  1. Add safe delivery zone (as flat area of different colour) - Paul
  2. Add supervisor which can send drone location to drone (See week 4 tasks) - Mayank
  3. Modify supervisor to send safe landing zone information

*3. Controller*
  1. Create controller which can recognise components of prototype drone
  2. Modify controller to use propellers to lift
  3. Modify controller to receive information from supervisor
  4. Modify controller to act on information from supervisor
      * ...by raising to target altitude
      * ...by moving to safe delivery zone
      * ... by lowering to the ground

*4. Github*
  1. Add Product Backlog to README.md (See markdown guidelines: <https://guides.github.com/features/mastering-markdown/>) - Mengyao
  2. Add screenshot of environment to README.md - Paul

## Product Backlog(for Sprint 1: 9/21-9/24)

*1. Drone*
  1. Decide on style of drone(eg. quadrocopter) - Everyone
      * Research necessary components based on requirments
  2. Decide on representation of packages - Mayank 
      * Research effect of weight on flight
      * Consider how to measure weight
      * Add weight to drone design 
  3. Decide on sensors - Ben
  4. Build drone

*2. Environment*
  1. Decide on representation of properties
  2. Decide on representation of safe delivery zones - Ben
      * Research detection methods 
  3. Build environment in Webots - Paul
  
*3. Controller*
  1. Gather examples of Webots controllers for quadcopters
  2. Create DJI Mavic 2 Pro controller in Python - Ben

*4. Git repository*
  1. Create Git repository on GitHub - Paul
  2. Ensure all members can access and modify repository - Everyone

*5. Webots project*
  1. Create Webots project - Ben
      * Upload to GitHub (depends: 4.1)

  
  
  
