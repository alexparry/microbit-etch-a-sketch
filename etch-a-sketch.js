/** 
Etch A Sketch on the micro:bit

Author: Alex Parry
License: CC BY-NC-SA 4.0
https://github.com/alexparry/microbit-etch-a-sketch

Draw an image by toggling the LEDs on and off using the buttons.
The blinking LED shows which LED you are currently on.
Press the micro:bit logo to turn an LED on or off.
Press the A button to change the X position and the B button to change the Y position.
Shake to clear.
 */

let state = 0
let xPos = 0
let yPos = 0

function store_initial_state() {
    //  Store whether the current LED is on (255) or off (0)
    if (led.pointBrightness(xPos, yPos) > 0) {
        state = 255
    } else {
        state = 0
    }
    
}

function set_led_from_state() {
    //  Plot or unplot the current LED based on the state
    if (state == 0) {
        led.unplot(xPos, yPos)
    } else {
        led.plot(xPos, yPos)
    }
}

input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    //  Toggle the brightness of the current LED on (255) or off (0)
    if (state == 0) {
        state = 255
    } else {
        state = 0
    }
})

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    //  Set the state of the current LED
    set_led_from_state()
    //  Move the current X position
    if (xPos == 4) {
        xPos = 0
    } else {
        xPos += 1
    }
    //  Store the state of the new position
    store_initial_state()
})

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    //  Set the state of the current LED
    set_led_from_state()
    //  Move the current Y position
    if (yPos == 4) {
        yPos = 0
    } else {
        yPos += 1
    }  
    //  Store the state of the new position
    store_initial_state()
})

input.onGesture(Gesture.Shake, function on_gesture_shake() {
    //  Clear the screen and reset the position and state
    basic.clearScreen()
    xPos = 0
    yPos = 0
    state = 0
})

basic.forever(function on_forever() {
    //  Make the current LED blink using the state brightness level
    while (true) {
        led.plotBrightness(xPos, yPos, 125)
        basic.pause(500)
        led.plotBrightness(xPos, yPos, state)
        basic.pause(500)
    }
})
