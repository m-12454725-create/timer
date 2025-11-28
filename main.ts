let time = 0
input.onButtonPressed(Button.A, function () {
    while (!(input.buttonIsPressed(Button.B))) {
        basic.pause(10)
        time += 1
        basic.showNumber(time)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(time)
})
