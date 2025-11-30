---
layout: default
title: Lesson 5 - Conditionals (Teacher)
---
# Lesson 5: Conditionals (Teacher Notes)

This is the **teacher guide** for Lesson 5.  
It includes lesson flow, strategies, and example logic using **if / else statements**.

---

## Learning Objectives

- Students understand how **conditionals (if / else)** work
- Students can use **comparison operators** such as `>`, `<`, and `=`
- Students can change behavior based on **input (buttons)**
- Students can change behavior based on **movement (acceleration speed)**

---

## Suggested Lesson Flow

### 1. Introduction (5 mins)

- Ask: "How does a computer make a decision?" (e.g., traffic lights, video games, speed cameras)
- Explain that an **if / else** statement helps the Micro:bit decide what to do
- Introduce the term **condition** (a question with a true/false answer)

Examples:
- IF it is raining → take an umbrella
- IF speed > limit → show warning


---

### 2. Demonstration (5–7 mins)

On the board or projector, demonstrate:

- Where to find **if / else** in the **Logic** toolbox
- Where to find **acceleration (strength)** in the **Input** toolbox
- Creating this condition:

```
acceleration (strength) > 800
```

Inside the condition:
- IF true → show **Sad** icon 😞
- ELSE → show **Happy** icon 🙂

Explain:
- The Micro:bit constantly measures how fast it is moving
- It checks the condition and chooses what to do

---

### 3. Student Activity (15–20 mins)

Students must:

1. Add **on shake** block
2. Put an **if / else** inside
3. Use this condition:

```
acceleration (strength) > 800
```

4. Add icons:
   - IF → Sad face
   - ELSE → Happy face

Then add a second conditional:

- **On button A pressed** → check speed
- IF → show "FAST"
- ELSE → show "SLOW"

Encourage students to test:
- Gentle movement
- Strong shaking
- Completely still


---

### 4. Extension / Fast Finishers

Challenge students to:

- Change the threshold number
- Add **Button B** to do the opposite
- Play a **warning sound** if speed is too high
- Use a double condition:

```
if speed > 800 AND button B is pressed
```

Optional real-world links:
- Car speed warning systems
- Automatic doors
- Alarm systems

---

## Common Issues & Fixes

| Problem | Fix |
|------|-----|
| Icons don’t change | Make sure the **if / else** is inside **on shake** or **on button A** |
| Always shows same icon | Student may have used `<` instead of `>` or wrong number |
| Nothing happens | Check they used **acceleration (strength)** not direction |
| Too sensitive / not sensitive | Adjust number to 400 / 1200 |

---

## Example Code (JavaScript)

```javascript
input.onGesture(Gesture.Shake, function () {
    if (input.acceleration(Dimension.Strength) > 800) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Happy)
    }
})

input.onButtonPressed(Button.A, function () {
    if (input.acceleration(Dimension.Strength) > 800) {
        basic.showString("FAST")
    } else {
        basic.showString("SLOW")
    }
})
```

---

## Reflection (Teacher Prompts)

- Where do we use conditionals in everyday life?
- Why is decision-making important in programming?
- How could this be used in a safety system or a game?

