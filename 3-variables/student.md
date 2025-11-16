# Lesson 3: Variables

In this lesson, you'll learn how to use **variables** on the Micro:bit to store and change information. By the end, you'll build a working **counter app** that increases, decreases, and resets numbers.

---

## What You'll Learn

* What a **variable** is.
* How to create a variable.
* How to increase and decrease a value.
* How to show changing numbers on the Micro:bit.
* How to make a counter, score keeper, or number changer.

---

## Steps

### 1. Open MakeCode

Go to **MakeCode for Micro:bit**: [https://makecode.microbit.org/](https://makecode.microbit.org/)

### 2. Start a New Project

* Click **New Project**
* Name it: `Variables`

---

### 3. Make a Variable

* Open the **Variables** menu.
* Click **Make a variable**.
* Name it: `count`.
* Drag `set count to 0` into the **on start** block.
* Add a **show number** block and set it to show `count`.

**Test it:**

* The Micro:bit should show **0** when it starts.

---

### 4. Button A: Increase the Number

* From **Input**, drag **on button A pressed**.
* From **Variables**, drag **change count by 1**.
* Add **show number count**.

**Test it:**

* Press A → the number goes **up**.

---

### 5. Button B: Decrease the Number

* From **Input**, drag **on button B pressed**.
* Add **change count by -1**.
* Add **show number count**.

**Test it:**

* Press B → the number goes **down**.

---

### 6. Reset the Counter

* Use **on button A+B pressed**.
* Add `set count to 0`.
* Add **show number count**.

**Test it:**

* Press A+B → resets back to 0.

---

### 7. Extra Challenge (Optional)

Try one of these:

* Change A to add **+5** instead of +1.
* Make a second variable called `score`.
* Shake the Micro:bit to **double** the count.

---

## Reflection

* Why is it useful to store numbers in variables?
* How could a counter or score system be used in a game?
* What else could you store in a variable?