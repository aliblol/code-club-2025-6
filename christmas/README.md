# 🎁 Festive Card Coding Challenge
Create your own digital festive card!
You can choose one of three paths depending on what you enjoy most: HTML/CSS, Scratch, or micro:bit Arcade.
Your card should:
- Show a festive message (e.g., “Happy Holidays!” or “Merry Christmas!”).
- Include at least one animation or interactive element.
- Be fun, creative, and personal!

# ✨ Path 1: HTML/CSS Festive Card
- Open a new HTML file.
- Add a heading with your festive message:
```<h1>Happy Holidays!</h1>```
- Style it with CSS:
```body {
  background: linear-gradient(to bottom, #003366, #66ccff);
  color: white;
  text-align: center;
  font-family: 'Comic Sans MS', cursive;
}
h1 {
  animation: glow 2s infinite alternate;
}
@keyframes glow {
  from { text-shadow: 0 0 5px white; }
  to { text-shadow: 0 0 20px gold; }
}```
- Add extras:
- Snowflakes using div elements with CSS animations.
- A festive image (tree, star, snowman).
- A button that changes the background color when clicked.

# 🎨 Path 2: Scratch Festive Card
- Create a new Scratch project.
- Add sprites: Santa, tree, snowman, or design your own.
- Add a backdrop (snowy night, fireplace, etc.).
- Code your card:
- When green flag clicked → show message with say "Merry Christmas!".
- Animate sprites (e.g., Santa waves, snow falls).
- Add sound (bells, music).
- Extensions:
- Make the card interactive (click the tree to light it up).
- Add a “surprise” animation when spacebar is pressed.

# 🎮 Path 3: micro:bit Arcade Festive Card
- Open MakeCode Arcade.
- Create a new project.
- Add a sprite for your festive character (Santa, snowman, tree).
- Show a message:
```game.splash("Happy Holidays!")```
- Animate:
- Move sprites across the screen.
- Add snowflakes falling (small sprites moving downward).
- Extensions:
- Play a festive tune with music.playMelody.
- Add interactivity (press A to show a gift, press B to change background).

# 🌟 Challenge Extensions
- Add randomness (snowflakes fall at different speeds).
- Add interactivity (click, press, or shake to reveal surprises).
- Add personalization (your name, favorite festive emoji, or a custom drawing).
