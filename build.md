# Build Instructions
These instructions can be followed so that your assembled kit will be identical to the presenter and all of the example code will function without modification. We specify colors of the wires only to help people follow along, but there's no real difference between them if you have trouble finding the right color. 

## Parts
- Raspberry Pi
- Ribbon Cable
- T Header
- Stoplight LED
- 4 button membrane with 6 pin header
- 8 short jumper wires in the following colors:
  -  white
  -  orange
  -  blue
  -  yellow
  -  yellow
  -  red
  -  green
  -  black
- a resistor

## Wiring Guide
- insert one end of the resistor into the negative rail (labeled with a blue minus sign) at position 35 on the left side of the breadboard
- insert the other end into f35 on the right side of the board
- connect the green jumper from position a13 to a43
- connect the red jumper from position a12 to a42
- connect the yellow jumper from position a11 to a41
- connect the black jumper from position a25 to a40
- insert the stoplight component with the lights facing to the right and the GND pin starting at position e40:
  - GND should be at position e40
  - R should be at position e41
  - Y should be at position e42
  - G should be at position e43
- connect the yellow jumper from position f34 to j21
- connect the white jumper from position f33 to j11
- connect the blue jumper from position f32 to j13
- connect the orange jumper from position f31 to j14
- insert the 6 pin header into the end of the 5 pin ribbon cable of the 4 button membrane with the extra pin off to the right
- insert the assembled membrane buttons into the board such that the first pin is at position j35 and the extra pin is at j30
