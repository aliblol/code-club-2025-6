# Lesson 2: Buttons & Gestures

In this lesson, you'll learn how to use the **buttons** and **shake gesture** on the Micro:bit to make it display different icons or numbers. By the end, you'll create a mini controller and even a digital dice!

---

## What You'll Learn
- How to use button A and button B events.
- How to detect a shake gesture.
- How to show icons and numbers based on inputs.

---

## Steps

### 1. Open MakeCode
Go to [MakeCode for Micro:bit](https://makecode.microbit.org/) in your browser.

### 2. Start a New Project
- Click **New Project**
- Name it: `Controls`

### 3. Show Icons with Buttons
- From the **Input** menu, drag an **on button A pressed** block into the workspace.
- From the **Basic** menu, drag a **show icon** block inside it.
- Select a **smiley face** icon.
- Repeat these steps for **button B**, but choose a **sad face** icon.

**Test it:**
- Press A → smiley face appears.
- Press B → sad face appears.

---

### 4. Shake to Roll a Dice
- From the **Input** menu, drag an **on shake** block into the workspace.
- Inside it, place a **show number** block from **Basic**.
- From **Math**, drag **pick random 1 to 6** into the `show number` block.

**Test it:**
- Shake the Micro:bit → a random number between 1 and 6 appears!

---

### 5. Combine Buttons and Shake
Let's turn the Micro:bit into a simple controller:
- **Button A** = Arrow Up (forward)
- **Button B** = Arrow Down (backward)
- **Shake** = Square (stop)

**Update your code:**
- Change button A icon to **arrow up**.
- Change button B icon to **arrow down**.
- Change the shake block to **square**.

**Test it:**
- Press A → arrow up appears.
- Press B → arrow down appears.
- Shake → square appears.

---

### 6. Extra Challenge (Optional)
- Add an **on button A+B pressed** block.
- Show a special icon like a **trophy** or **heart**.

---

## Reflection
- What happens when you press A and B at the same time?
- How could this be useful when building the race car controller later?
