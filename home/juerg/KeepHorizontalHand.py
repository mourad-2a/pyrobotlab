i01 = Runtime.start("i01", "InMoov")
hand = i01.startRightHand("COM15")
arduino = Runtime.getService("i01.right")

keepHorizontalOutPin = 13
boolean keepHorizontal = False

def keepHorizontalStart():
  arduino.digitalWrite(keepHorizontalOutPin, 1)
  keepHorizontal = True;
  i01.rightHand.wrist.detach()
  
def keepHorizontalStop():
  arduino.digitalWrite(keepHorizontalOutPin, 0)
  keepHorizontal = False;
  i01.rightHand.wrist.attach()
