def on_forever():
    basic.show_string("Sup Ash!")
def on_button_pressed_a():
    basic.show_string("You are pretty rad")
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
        basic.show_string("You are cool, like ice")
        input.on_button_pressed(Button.B, on_button_pressed_b)
basic.forever(on_forever)