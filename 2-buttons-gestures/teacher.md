---
layout: default
title: Lesson 2 - Buttons & Gestures (Teacher)
---

# Lesson 2: Buttons & Gestures (Teacher Notes)

This is the **teacher guide** for Lesson 2.  
It includes tips and teaching strategies for using button and gesture inputs on the BBC Micro:bit.

---

## Learning Objectives
- Teach students to use **button A** and **button B** events.
- Introduce the **shake gesture** as an input.
- Create a simple program that responds to different inputs.

---

## Suggested Lesson Flow

1. **Introduction (5 mins)**  
   - Recap last week's lesson: showing text or icons.
   - Explain that today students will make the Micro:bit *react* when buttons are pressed or when it's shaken.
   - Demo button A → smiley face, button B → sad face, shake → random number.

2. **Demonstration (5 mins)**  
   - Show how to add `on button A pressed` and `on shake` blocks.
   - Explain the idea of **events**: code runs only when something happens.

3. **Student Activity (15-20 mins)**  
   - Students follow [student instructions](student.md).
   - Start with button icons, then add shake gesture, then combine into a controller.
   - Optional challenge: A+B pressed shows a special icon.

4. **Wrap-Up (5 mins)**  
   - Ask reflective questions:
     - "Which part was easy? Which part was tricky?"
     - "How could these inputs be useful when building the race car controller later?"
   - Remind students to **save their work** for future lessons.

---

## Common Issues & Fixes
| Problem | Solution |
|----------|----------|
| Micro:bit not connecting | Check cable or battery, try another USB port. |
| Code not working | Ensure blocks are inside the correct event block (button/shake). |
| Numbers not random | Make sure `pick random 1 to 6` is inside `show number`. |
| Icons overlapping | Remind students each button needs its own event block. |

---

## Demo Code Example
- [Finished Code](main.ts)

To edit this repository in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/aliblol/code-club-2025-6/2-buttons-gestures** and click import