time = 0

def on_button_pressed_a():
    global time
    while not (input.button_is_pressed(Button.B)):
        basic.pause(10)
        time += 1
        basic.show_number(time)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global time
    time = 0
    basic.show_number(time)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
