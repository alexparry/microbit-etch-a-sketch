"""
Etch A Sketch on the micro:bit

Author: Alex Parry
License: MIT
https://github.com/alexparry/microbit-etch-a-sketch

Draw an image by toggling the LEDs on and off using the buttons.
The blinking LED shows which LED you are currently on.
Press pin 0 to turn an LED on or off.
Press the A button to change the X position and the B button to change the Y position.
Shake to clear.
"""

state = 0
xPos = 0
yPos = 0

def store_initial_state():
    global state
    # Store whether the current LED is on (255) or off (0)
    if led.point_brightness(xPos, yPos) > 0:
        state = 255
    else:
        state = 0

def set_led_from_state():
    # Plot or unplot the current LED based on the state
    if state == 0:
        led.unplot(xPos, yPos)
    else:
        led.plot(xPos, yPos)

def on_pin_pressed_p0():
    global state
    # Change the brightness of the current LED on (255) or off (0)
    if state == 0:
        state = 255
    else:
        state = 0
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global xPos
    # Set the state of the current LED
    set_led_from_state()
    # Move the current X position
    if xPos == 4:
        xPos = 0
    else:
        xPos += 1
    # Store the state of the new position
    store_initial_state()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global yPos
    # Set the state of the current LED
    set_led_from_state()
    # Move the current Y position
    if yPos == 4:
        yPos = 0
    else:
        yPos += 1
    # Store the state of the new position
    store_initial_state()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global xPos, yPos, state
    # Clear the screen and reset the position and state
    basic.clear_screen()
    xPos = 0
    yPos = 0
    state = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    # Make the current LED blink using the state brightness level
    while True:
        led.plot_brightness(yPos, xPos, 125)
        basic.pause(500)
        led.plot_brightness(xPos, yPos, state)
        basic.pause(500)
basic.forever(on_forever)
