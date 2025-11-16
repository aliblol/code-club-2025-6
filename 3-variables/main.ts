/**
 * Lesson 2: Buttons & Gestures Example Code
 */
// Clear screen after a short delay
function clearAfterDelay () {
    basic.pause(500)
    basic.clearScreen()
}
// Button A pressed → show arrow up
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . # . .
        . # # # .
        # . # . #
        . . # . .
        . . # . .
        `)
    clearAfterDelay()
})
// A+B pressed → show heart
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Heart)
    clearAfterDelay()
})
// Button B pressed → show arrow down
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . # . .
        . . # . .
        # . # . #
        . # # # .
        . . # . .
        `)
    clearAfterDelay()
})
// Shake gesture → dice
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(randint(1, 6))
})
