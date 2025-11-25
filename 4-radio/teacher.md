---
layout: default
title: Lesson 4 - Radio (Teacher)
---
# Lesson 4: Radio (Teacher Notes)

This is the **teacher guide** for Lesson 4.  
It includes lesson flow, strategies, and example code.

---

## Learning Objectives

* Students understand how the Micro:bit sends and receives wireless radio messages.
* Students can set a radio group/channel.
* Students can send numbers or strings to another Micro:bit.
* Students can receive and act on incoming messages.

---

## Suggested Lesson Flow

### 1. Introduction (5 mins)

* Ask: “How do walkie-talkies communicate?” → introduce the idea of radio signals.
* Explain that Micro:bits can send messages wirelessly if they are on the **same group number**.

### 2. Demonstration (5 mins)

Show how to:

* Set the radio group in **on start**
* Send a number with a button press
* Receive a number and display it

Emphasize:

* Devices must be on the **same group** to communicate.
* Pressing a button sends the message.

### 3. Student Activity (15–20 mins)

Students build:

* Button A → sends `1`
* Button B → sends `2`
* On receive → show the received number

Then test with a partner or group.

Optional challenges:

* Send a word or name.
* Create a score system.
* Add sounds or icons.
* Apply message filtering (e.g., only show messages that equal 5).

### 4. Wrap-Up (5 mins)

Ask reflective questions:

* “Where is wireless communication used in real life?”
* “What happens if different groups overlap?”
* “How could we combine variables + radio for a multiplayer game?”

---

## Common Issues & Fixes

| Problem                               | Solution                                                           |
| ------------------------------------- | ------------------------------------------------------------------ |
| Micro:bits aren’t communicating       | Check both devices use the **same radio group number**.           |
| Nothing shows on the screen           | Ensure **show number** is added inside the received event block.  |
| Messages interfere with other groups  | Assign different group numbers per pair or table.                 |

---

## Demo Code Example (JavaScript)

```javascript
radio.setGroup(1)

input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
})

input.onButtonPressed(Button.B, function () {
    radio.sendNumber(2)
})

radio.onReceivedNumber(function (receivedNumber) {
    basic.showNumber(receivedNumber)
})
