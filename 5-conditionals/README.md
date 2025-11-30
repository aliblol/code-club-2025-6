# Lesson 4: Radio Messaging

In this lesson, you'll learn how to use the **Radio** feature on the Micro:bit to send and receive messages **wirelessly** between two or more Micro:bits. By the end, you’ll make a simple **wireless chat system** that sends numbers or short messages from one Micro:bit to another.

---

## What You'll Learn

* What the **radio** is and how it works.
* How to set a **radio group** so Micro:bits can talk to each other.
* How to **send messages or numbers** wirelessly.
* How to **receive and display messages**.

---

## {Step 1 @fullscreen}

Click on the ``||basic:Basic||`` category in the Toolbox. 
Drag the ``||basic:show leds||`` block into the ``||basic:forever||`` block. 
Then in the ``||basic:show leds||`` block, click on the squares to draw a heart design.

## {Step 2}

Drag another ``||basic:show leds||`` block underneath the first.

```blocks
basic.forever(function() {
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .`);
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .`);
})
```

## {Step 3}

Look at the @boardname@ on the screen. Do you see a flashing heart animation? ⭐ Great job! ⭐ 

## {Step 4}

If you have a @boardname@ device, connect it to your computer and click the ``|Download|`` button. Follow the instructions to transfer your code onto the @boardname@ and watch the hearts flash! 