# Robot Control Plugin

Plugin for controling my robot

## Setup

Install manually using this URL:

    https://github.com/Zinc-OS/octoprint-robot-plugin/archive/master.zip



## Configuration

For a four servo robot. via the I2C bus

You will also need to enable i2c bus via ```sudo raspi-cofig``` throught the terminal, accessible through ```ssh pi@octopi.local:22```

then
```interface options>enable i2c>yes>finish```

For the raspi, addresses cannot be lower than 3, and the arduino only use addresses higher than 8, so the address must be an integer 8-127, and must be the same for the adruino and the raspi.

There are sliders in the robot control tab, and gcodes can be used with the format ```@servo[1..4]:[ANGLE]```, such as ```@servo2:90``` or ```@servo4:12```.
