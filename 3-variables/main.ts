input.onButtonPressed(Button.A, function () {
    count += 1
    basic.showNumber(count)
})
input.onButtonPressed(Button.AB, function () {
    count = 0
    basic.showNumber(count)
})
input.onButtonPressed(Button.B, function () {
    count += -1
    basic.showNumber(count)
})
input.onGesture(Gesture.Shake, function () {
    count = count * 2
    basic.showNumber(count)
})
let count = 0
basic.showNumber(count)
