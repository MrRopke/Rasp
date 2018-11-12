from sense_hat import SenseHat 
import random

sense = SenseHat() 
sense.clear((0,0,0)) 
blue = (0,0,255) 
sense.set_pixel(3,4,blue)
pixelX = 3
pixelY = 4


while True: 
 acceleration = sense.get_accelerometer_raw()
 x = acceleration['x']
 y = acceleration['y']
 z = acceleration['z']
 x=round(x, 0)
 y=round(y, 0)
 z=round(z, 0)

 print("x={0}, y={1}, z={2}".format(x, y, z))
  # Update the rotation of the display depending on which way up the 
  # Sense HAT is
 if x == -1 and pixelX > 0:
  sense.set_pixel(pixelX, pixelY, (0,0,0))
  pixelX = pixelX-1
  sense.set_pixel(pixelX, pixelY, blue)
 elif x == 1 and pixelX < 7:
  sense.set_pixel(pixelX, pixelY, (0,0,0))
  pixelX = pixelX+1
  sense.set_pixel(pixelX, pixelY, blue)
 if y == 1 and pixelY < 7:
  sense.set_pixel(pixelX, pixelY, (0,0,0))
  pixelY = pixelY+1
  sense.set_pixel(pixelX, pixelY, blue)
 elif y == -1 and pixelY > 0:
  sense.set_pixel(pixelX, pixelY, (0,0,0))
  pixelY = pixelY-1
  sense.set_pixel(pixelX, pixelY, blue)
