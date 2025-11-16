---
layout: default
title: Lesson 3 - Variables (Teacher)
---
# Lesson 3: Variables (Teacher Notes)

This is the **teacher guide** for Lesson 3.
It includes the lesson flow, strategies, and example code.

---

## Learning Objectives

* Students understand what variables are.
* Students can change a variable using button inputs.
* Students can show changing values on the Micro:bit screen.
* Students can build a simple counter program.

---

## Suggested Lesson Flow

### 1. Introduction (5 mins)

* Ask: "What if we want to remember a number?" → introduce variables.
* Show an example: press A to increase a number on your Micro:bit.

### 2. Demonstration (5 mins)

* Show how to:

  * Create a variable
  * Set its starting value
  * Change it with buttons
  * Display it
* Emphasize that a variable is *stored information*.

### 3. Student Activity (15–20 mins)

* Students follow their instructions.
* Build the counter → then add decreasing → then reset.
* Optional challenges for early finishers.

### 4. Wrap-Up (5 mins)

* Ask reflective questions:

  * "How could we use variables in a game?"
  * "What happens if we decrease below 0?"
* Remind students to save their project.

---

## Common Issues & Fixes

| Problem               | Solution                                                                    |
| --------------------- | --------------------------------------------------------------------------- |
| Number doesn't change | Ensure the student added **change count by** inside the right button block. |
| Screen doesn't update | Add **show number count** after changing the variable.                      |
| Reset doesn't work    | Make sure `set count to 0` is inside **A+B** event.                         |

---

## Demo Code Example (JavaScript)

```javascript
let count = 0
basic.showNumber(count)

input.onButtonPressed(Button.A, function () {
    count += 1
    basic.showNumber(count)
})

input.onButtonPressed(Button.B, function () {
    count += -1
    basic.showNumber(count)
})

input.onButtonPressed(Button.AB, function () {
    count = 0
    basic.showNumber(count)
})
```

---

## Extension Examples

### Score Keeper

```javascript
let score = 0
input.onButtonPressed(Button.A, function () {
    score += 5
    basic.showNumber(score)
})
input.onButtonPressed(Button.B, function () {
    score += 1
    basic.showNumber(score)
})
```

### Shake to Multiply

```javascript
let value = 1
input.onGesture(Gesture.Shake, function () {
    value = value * 2
    basic.showNumber(value)
})
```

### Temperature in a Variable

```javascript
let temp = 0
input.onButtonPressed(Button.A, function () {
    temp = input.temperature()
    basic.showNumber(temp)
})
```