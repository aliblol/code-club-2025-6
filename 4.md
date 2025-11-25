# Radio Messaging

## {Introduction @unplugged}

Let’s learn how to use the **radio** 📡 on the @boardname@ to send messages **wirelessly** between two or more micro:bits!

By the end of this lesson, you’ll build a **wireless chat system** that can send numbers or short messages from one @boardname@ to another.  

---

## {Step 1}

Just like walkie-talkies, all @boardname@s must be on the **same radio channel** to communicate.

From the ``||radio:Radio||`` Toolbox category, get a  
``||radio:radio set group 1||`` block and place it inside the  
``||basic:on start||`` block.

```blocks
radio.setGroup(1)
```

> If you're working in a classroom, each group should choose a different number to avoid cross-talk.

---

## {Step 2}

Now we’ll send a number when Button **A** is pressed.

From ``||input:Input||`` get an  
``||input:on button A pressed||`` block.

Inside it, add a  
``||radio:radio send number||`` block and set it to **1**.

```blocks
input.onButtonPressed(Button.A, function () {
    //@highlight
    radio.sendNumber(1)
})
```

Press **A** on the simulator — your @boardname@ just sent a wireless message! 📡

---

## {Step 3}

Now let’s make the @boardname@ **receive** radio messages.

From ``||radio:Radio||`` get  
``||radio:on radio received receivedNumber||``.

Inside it, add a ``||basic:show number||`` block to display the number received.

```blocks
radio.onReceivedNumber(function (receivedNumber) {
    //@highlight
    basic.showNumber(receivedNumber)
})
```

Try it with **two micro:bits**:

* Press **A** on one  
* The other should show **1** ✨

---

## {Step 4}

Let’s send a second message using Button **B**.

From ``||input:Input||`` add  
``||input:on button B pressed||``.

Inside it, add another  
``||radio:radio send number||`` block, but set this one to **2**.

```blocks
input.onButtonPressed(Button.B, function () {
    //@highlight
    radio.sendNumber(2)
})
```

Now:

* **A** sends **1**  
* **B** sends **2**

Try sending them back and forth between two @boardname@s!

---

## {Step 5}

Want to go further? Try one of these challenges:

* Send words instead of numbers  
  👉 use ``||radio:radio send string||``
* Create a scoreboard  
  👉 A = +1, B = –1 using variables
* Add sounds when a message is received
* Only show a message if it matches a “password”
* Make a simple multiplayer game using radio + variables

---

## {Step 6}

If you have a @boardname@ device, connect it and click ``|Download|`` to send the program. Try wireless communication in the real world!

---

```validation.global
# BlocksExistValidator
```

```template
radio.setGroup(1)
```
