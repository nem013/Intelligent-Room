# number of hours spent on this code = 4

# Author(s) :
#
# -     n3m013, github : https://github.com/nem013

# To do :
#
# -     For the code to work proprely the "state" variable has to reassigned to a
#       "null" value (!= 1 or 0), it has something to do with the "last_state" thing
#       For now the code activates the function everytime when sb enters or goes out the
#       room, so for the future, it has to do nothing the second time sb entered/went out
#       of the room.

# -     Clean a little bit ... XD

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# setup of sensor 1 (TOP side) on GPIO pin 15 (board pin 10) :
gpio1 = 15
GPIO.setup(gpio1, GPIO.IN)

#setup of sensor 2 (BOTTOM side) on GPIO pin 18 (board pin 12) :
gpio2 = 18
GPIO.setup(gpio2, GPIO.IN)

state = -1              # if state = 0, then left the room, if state = 1, then entered the room
last_state = -1

last_time_val = 0       # last time when one of the two sensors was triggered
time1 = time2 = time.time()             # definition of the time variable for sensor 1          # definition of the time variable for sensor 2

sensor1_triggered = False
sensor2_triggered = False

while True:
    if (time.time() - last_time_val) > 1:   # The integer here is the interval in seconds during which the sensor is "frozen", in the purpose of not to
                                                # take two consecutive measures too quickly. It has the purpose to prevent wrong in-out measures.
        val1 = GPIO.input(gpio1)
        val2 = GPIO.input(gpio2)

        if val1 == 0 and (sensor1_triggered == False):
            time1 = time.time()     # time at which sensor 1 triggered
            sensor1_triggered = True

        if val2 == 0 and (sensor2_triggered == False):
            time2 = time.time()     # time at which sensor 2 triggered
            sensor2_triggered = True

        if sensor1_triggered and sensor2_triggered :
            if ((time1 < time2)):   # if the difference is negative, then someone has left the room
                state = 0
                if state != last_state :        # this has the purpose of a "when" function, it checks if the current "new" state is different from                                        last_state = state      # previous one. It prevents from executing a function each and every time when the  statement is s>                                        last_time_val = time2

                            # Call/write your function here :
                            print("Out of the room")

            elif ((time1 > time2)): # if the difference is positive, then someone entered the room
                state = 1
                if state != last_state :        # same purpose as above
                    last_state = state
                    last_time_val = time1

                    # Call/write your function here :
                    print("In the room")

            sensor1_triggered = sensor2_triggered = False   # sets that both of the sensors have to "reactivate"
            last_state = -1