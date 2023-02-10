from microbit import*
#we make an infinite loop
while True:
    # we put the PIR read in a variable
    motion = pin1.read_digital()
    #we check if there is a motion detected then the buzzer will be turned on as an alarm
    if motion == 1:
        pin0.write_digital(1)
    else:
        #if there is no motion detected the buzzer will be off
        pin0.write_digital(0)
