# 🎁 Festive Card Coding Challenge
Create your own digital festive card!
You can choose one of three paths depending on what you enjoy most: HTML/CSS, Scratch, or micro:bit Arcade.
Your card should:
- Show a festive message (e.g., “Happy Holidays!” or “Merry Christmas!”).
- Include at least one animation or interactive element.
- Be fun, creative, and personal!

# ✨ Path 1: HTML/CSS Festive Card
- Open a new HTML file.
- Add a heading with your festive message
Example code:
```<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Festive Card</title>
</head>
<body>

<div class="card" role="region" aria-label="Festive card">
  <div class="snow" id="snow"></div>

  <header>
    <h1 id="title">Happy Holidays!</h1>
    <p id="subtitle">Wishing you a season full of fun and code 🎉</p>
  </header>

  <div class="tree" aria-hidden="true">
    <div class="leaf"></div>
    <div class="leaf"></div>
    <div class="leaf"></div>
    <div class="trunk"></div>
  </div>
<style>
  :root{
    --card-w: 360px;
    --bg: linear-gradient(180deg,#102240 0%, #1b3a73 60%, #7dd3fc 100%);
    --card-bg: linear-gradient(180deg,#fffef9, #fff1e6);
    --accent: #ff6b6b;
  }

  html,body{height:100%; margin:0; font-family: "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background:var(--bg); display:flex; align-items:center; justify-content:center; color:#073b4c;}
  .card{
    width:var(--card-w);
    border-radius:14px;
    padding:18px;
    background:var(--card-bg);
    box-shadow: 0 12px 30px rgba(2,6,23,0.45);
    text-align:center;
    position:relative;
    overflow:hidden;
  }

  header h1{margin:6px 0 2px; font-size:1.5rem;}
  header p{margin:0 0 12px; color:#4b5563;}

  /* Snow container uses pointer-events:none so it doesn't block clicks */
  .snow{position:absolute; inset:0; pointer-events:none; overflow:hidden;}
  .flake{
    position:absolute;
    color: #ffffffaa;
    font-size:18px;
    animation: fall linear infinite;
    will-change: transform, opacity;
  }
  @keyframes fall{
    0%{ transform: translateY(-20vh) rotate(0deg); opacity:0; }
    10%{ opacity:1; }
    100%{ transform: translateY(110vh) rotate(360deg); opacity:0.8; }
  }

  /* Tree graphic (simple CSS) */
  .tree{ margin: 10px auto 14px; width:120px; height:120px; position:relative; }
  .tree .leaf{ width:0; height:0; border-left:60px solid transparent; border-right:60px solid transparent; border-bottom:48px solid #0b7a3a; margin: -8px auto; }
  .tree .leaf:nth-child(2){ border-bottom-color:#0f9b4a; transform: translateY(-22px); }
  .tree .leaf:nth-child(3){ border-bottom-color:#16c06b; transform: translateY(-44px); }
  .tree .trunk{ width:28px; height:30px; background:#6b3b1a; margin: -50px auto 0; border-radius:3px; }

</style>
  <p style="font-size:12px; color:#6b7280; margin-top:12px;">From Alice :) </p>
```
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
