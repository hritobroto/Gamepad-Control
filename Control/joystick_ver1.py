import inputs

while True:

    if(len(inputs.devices.gamepads) == 0): #checks if the controller is connected or not
        print("Please connect controller!")
    else:
        events = inputs.get_gamepad()  #gets events from the controller, i.e, button clicks and joystick movements
        for event in events:

            
            #print(event.ev_type, event.code, event.state)
            #print(event.code,event.state)

            #Speed control
            if(event.code == 'BTN_SOUTH' and event.state == 1):
                print('A')
            if(event.code == 'BTN_NORTH' and event.state == 1):
                print('Y')
            if(event.code == 'BTN_WEST' and event.state == 1):
                print('X')
            if(event.code == 'BTN_EAST' and event.state == 1):
                print('B')

            #Direction Control
            if(event.code == 'ABS_RY' and event.state > 0):
                print('UP')
            if(event.code == 'ABS_RY' and event.state < 0):
                print('DOWN')
            if(event.code == 'ABS_RX' and event.state > 0):
                print('RIGHT')
            if(event.code == 'ABS_RX' and event.state < 0):
                print('LEFT')


            #Start and Select buttons
            if(event.code == 'BTN_START' and event.state == 1):
                print('SELECT')
            if(event.code == 'BTN_SELECT' and event.state == 1):
                print('START')
