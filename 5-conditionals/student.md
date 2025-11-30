# Lesson 5: Conditionals (If / Else)

In this lesson, you'll learn how to use **conditionals** on the Micro:bit to make your program **change its behavior** based on different situations. By the end, you’ll use `if / else` statements to react to **movement (speed)** and **button input**.

---

## What You'll Learn

- What an **if / else** statement is and how it works
- How to use **comparisons** like `>`, `<`, and `=`
- How to change behavior based on **speed (movement)**
- How to change behavior based on **input** (button presses)

---

## Steps

### 1. Open MakeCode
Need step-by-step help? Go [here](https://makecode.microbit.org/#tutorial:09380-06242-91494-84811)

If you are happy to figure it out on your own, go to:
https://makecode.microbit.org/

Click **New Project** and name it:
`Conditionals`

---

### 2. Get the Speed (Acceleration)

The micro:bit has a motion sensor called an **accelerometer**. We can use it to measure how fast the device is moving.

- Go to **Input**
- Find **acceleration (strength)**
- This value will be our **speed**

---

### 3. Add an IF / ELSE Block

Now we’ll make the Micro:bit react differently depending on the speed.

- Go to **Input** → drag **on shake** into the workspace
- Go to **Logic** → drag **if / else** inside it

Condition:

```
acceleration (strength) > 800
```

This means:
- If the speed is **greater than 800** → do one thing
- Otherwise → do something else

---

### 4. Show Different Icons

Inside the **IF** section:
- Go to **Basic** → add **show icon**
- Choose a **Sad face 😞**

Inside the **ELSE** section:
- Add **show icon**
- Choose a **Happy face 🙂**

**Test it:**
- Shake the Micro:bit hard → 😞
- Shake it gently → 🙂

✅ You just used a conditional!

---

### 5. Use a Button + Conditional

Now let’s check the speed using **Button A**.

- Go to **Input** → drag **on button A pressed**
- Add **if / else** inside

Condition:

```
acceleration (strength) > 800
```

Inside **IF**:
- Show text: `FAST`

Inside **ELSE**:
- Show text: `SLOW`

**Test it:**
- Move the micro:bit fast, then press **A** → shows **FAST**
- Keep it still, then press **A** → shows **SLOW**

---

## Extra Challenges (Optional)

Try one or more:

- Add a **sound** when the speed is too high
- Change the **threshold** from 800 to 400 or 1200
- Add **Button B** to check a different value
- Use **AND / OR** conditions:
  ```
  if speed > 800 AND button B is pressed
  ```
- Send a **radio message** only when the condition is true

---

## Reflection

- Why is it useful for a program to make decisions?
- Where do you see IF / ELSE in real life?
- How could conditionals be used in a game or alarm system?
