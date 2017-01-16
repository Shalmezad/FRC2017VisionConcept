# FRC2017VisionConcept
A demo in python showing how a robot's position relates to the gear sample target

Requires pygame.

## Usage:
`python projectionTest.py`
or
`make`

## Controls:
* Up/W: Forward
* Down/S: Backward
* Left/A: Turn left
* Right/D: Turn right
* Q/E: Strafe

## Screens:
Left side is a top-down view of the robot's camera in relation to the gear peg.

Top-right side shows the vision target from the camera's perspective

Bottom right gives some debugging information related to the robot's coordinates

## Coordinate system
Debugging information is given in inches and degrees.

Position: 

X is relative to the peg. Negative X is left of the peg, positive X is right of the peg. 

Y is relative to the peg base. Positive Y is away from the peg (so the tip of the peg is +10.5).

Z is relative to the floor.

Angle: angle is given such that 0 degrees is from the peg tip facing the peg base. + turns clockwise, - turns counter clockwise.

## Screenshot:
![Screenshot](https://github.com/Shalmezad/FRC2017VisionConcept/raw/master/doc/screenshot.png)
