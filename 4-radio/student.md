# Lesson 4: Radio Messaging

In this lesson, you'll learn how to use the **Radio** feature on the Micro:bit to send and receive messages **wirelessly** between two or more Micro:bits. By the end, you’ll make a simple **wireless chat system** that sends numbers or short messages from one Micro:bit to another.

---

## What You'll Learn

* What the **radio** is and how it works.
* How to set a **radio group** so Micro:bits can talk to each other.
* How to **send messages or numbers** wirelessly.
* How to **receive and display messages**.

---

## Steps

### 1. Open MakeCode Tutorial

Go to:  
http://makecode.microbit.org/#tutorial:https://github.com/aliblol/code-club-2025-6/radio

---

### 2. Set the Radio Group

Just like walkie-talkies, Micro:bits must be on the **same channel** to communicate.

* Go to **Radio**.
* Drag `radio set group 1` into **on start**.

> In a classroom, each pair of students should choose a different group number so projects don’t overlap.

---

### 3. Send a Message (Button A)

* Go to **Input** → drag **on button A pressed**.
* Go to **Radio** → drag `radio send number 1`.

**Test it:**

* Press **A** → the Micro:bit sends “1” wirelessly.

---

### 4. Receive Messages

Now make the Micro:bit show something when it receives a radio message.

* Go to **Radio**.
* Drag **on radio received number**.
* Inside it, add **show number** (from **Basic**).
* Set it to show the received number.

**Test with two Micro:bits:**

* Press A on one → the other shows **1**.

---

### 5. Send a Different Message (Button B)

Let’s add a second button:

* Go to **Input** → on button B pressed.
* Add `radio send number 2`.

Now:

* Press A → sends 1  
* Press B → sends 2

---

### 6. Extra Challenges (Optional)

Try one or more:

* Send a **word instead of a number**  
    * Use `radio send string`.
* Create a counting system:
    * A = +1  
    * B = –1
* Add sounds when a message is received.
* Create a simple filter:
    * Only show the number if it matches a password.
* Combine with variables for a multiplayer scoreboard.

---

## Reflection

* Why is radio communication useful?
* Where might wireless messaging be used in real life?
* How could you combine variables + radio to make a multiplayer game?
