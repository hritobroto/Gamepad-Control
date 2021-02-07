#pip install inputs

import inputs

#x=0
while True:
    #x+=1
    if(len(inputs.devices.gamepads) == 0): #checks if the controller is connected or not
        print("Please connect controller!")
    else:
        events = inputs.get_gamepad()  #gets events from the controller, i.e, button clicks and joystick movements
        for event in events:

            #All button mapping
            
            #print(event.ev_type, event.code, event.state)
            #print(event.code,event.state)
            if(event.code == 'BTN_SOUTH' and event.state == 1):
                print('A')
            if(event.code == 'BTN_NORTH' and event.state == 1):
                print('Y')
            if(event.code == 'BTN_WEST' and event.state == 1):
                print('X')
            if(event.code == 'BTN_EAST' and event.state == 1):
                print('B')
            if(event.code == 'ABS_Y' and event.state > 0):
                print('UP')
            if(event.code == 'ABS_Y' and event.state < 0):
                print('DOWN')
            if(event.code == 'ABS_X' and event.state > 0):
                print('RIGHT')
            if(event.code == 'ABS_X' and event.state < 0):
                print('LEFT')
            if(event.code == 'ABS_RY' and event.state > 0):
                print('RIGHT UP')
            if(event.code == 'ABS_RY' and event.state < 0):
                print('RIGHT DOWN')
            if(event.code == 'ABS_RX' and event.state > 0):
                print('RIGHT RIGHT')
            if(event.code == 'ABS_RX' and event.state < 0):
                print('RIGHT LEFT')
            if(event.code == 'ABS_RZ' and event.state == 255):
                print('R2')
            if(event.code == 'BTN_TR' and event.state == 1):
                print('R1')
            if(event.code == 'ABS_Z' and event.state == 255):
                print('L2')
            if(event.code == 'BTN_TL' and event.state == 1):
                print('L1')
            if(event.code == 'ABS_HAT0X' and event.state > 0):
                print('BUTTON RIGHT')
            if(event.code == 'ABS_HAT0X' and event.state < 0):
                print('BUTTON LEFT')
            if(event.code == 'ABS_HAT0Y' and event.state > 0):
                print('BUTTON DOWN')
            if(event.code == 'ABS_HAT0Y' and event.state < 0):
                print('BUTTON UP')
            if(event.code == 'BTN_THUMBR' and event.state == 1):
                print('BUTTON THUMB RIGHT')
            if(event.code == 'BTN_THUMBL' and event.state == 1):
                print('BUTTON THUMB LEFT')
            if(event.code == 'BTN_START' and event.state == 1):
                print('SELECT')
            if(event.code == 'BTN_SELECT' and event.state == 1):
                print('START')
