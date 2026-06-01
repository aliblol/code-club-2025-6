---
layout: default
title: Coin Collector - Student Guide
---

# Coin Collector Game

Welcome! In this project, you'll design and build a complete game using **MakeCode Arcade**. The game is called **Coin Collector** — and you get to decide what happens!

---

## What Is This Game About?

In **Coin Collector**, a player character moves around the screen trying to collect coins while avoiding an enemy. The goal is to collect as many coins as possible before time runs out.

**Game Features:**
- A player you can control
- Coins to collect (they appear again and again)
- An enemy to avoid
- A score that increases when you collect coins
- Lives that decrease if you touch the enemy
- A timer that counts down to end the game

---

## Break It Down (Decomposition)

Big problems are easier to solve when you break them into smaller pieces.

**What are all the things our game needs?**

Think about each of these and write down what YOU think it should do:

1. **The Player** — What should the player look like? How should it move?
2. **Coins** — Where do coins appear? What happens when the player touches one?
3. **The Enemy** — How does the enemy move? What happens if it catches the player?
4. **Score** — When does the score increase? Where should it display?
5. **Lives** — How many lives should the player start with? What happens when lives reach 0?
6. **Timer** — How long is the game? What happens when time runs out?

---

## Your Challenge: Build It Step by Step

You'll build your game one piece at a time. For each step, I'll ask you **questions** to help you think through what to code. 

**Here's how it works:**
- Read the challenge
- Think about what blocks you might need
- Try building it
- Test your code
- Compare with the ideas below

---

## Step 1: The Player

**Challenge:** Create a player sprite that you can move around the screen using buttons or the arrow keys.

**Questions to guide you:**
- What should your player look like? (Pick or design a sprite)
- Where should it start? (Left, right, center, top, bottom?)
- How should it move? (Left/right only? All directions?)
- Should it stay on the screen or wrap around?

**Build it:**
- Start MakeCode Arcade: [makecode.arcade.org](https://arcade.makecode.org)
- Create a new project called `CoinCollector`
- Add a sprite and give it a variable name (e.g., `player`)
- Set its starting position
- Add movement controls
- Test it!

**Test:**
Can you move your player around the screen?

---

## Step 2: Coins & Scoring

**Challenge:** Make coins appear on screen. When your player touches a coin, add 1 to the score and make the coin disappear.

**Questions to guide you:**
- What should the coins look like?
- Should coins appear all at once, or one by one?
- How often should new coins appear?
- What happens when the player touches a coin?

**Build it:**
- Create a variable for `score` (starts at 0)
- Create a coin sprite
- Make coins appear using "every 1 second" block (in the loops menu)
- When the player overlaps the coin, add 1 to score and destroy the coin
- Display the score on screen using "show string" or a score label

**Test:**
Can you collect coins and see your score increase?

---

## Step 3: The Enemy

**Challenge:** Add an enemy sprite that moves around the screen. If the player touches it, lose a life.

**Questions to guide you:**
- What should the enemy look like?
- How should it move? (Random, in a pattern, chasing you?)
- Should it move fast or slow?
- What happens if you lose all your lives?

**Build it:**
- Create a variable for `lives` (starts at 3, or your choice)
- Create an enemy sprite
- Make it move using "move with velocity" or "move toward player"
- When the player overlaps the enemy:
  - Subtract 1 from lives
  - Teleport the player back to the starting position (so they get another try!)
- Display lives on screen
- If lives = 0, end the game with a "Game Over" message

**Test:**
Does the enemy work? Do you lose a life when you touch it?

---

## Step 4: The Timer & Winning

**Challenge:** Add a countdown timer. When time runs out, the game ends and shows your final score.

**Questions to guide you:**
- How long should the game last? (30 seconds? 60 seconds? Your choice!)
- Should the timer count down from a start time?
- What should happen when time runs out?

**Build it:**
- Create a variable for `timer` (set to your chosen time)
- Use "repeat every 1 second" to decrease the timer by 1
- Display the timer on screen
- When timer reaches 0:
  - Stop all movement
  - Show a message like "Time's up! You collected [score] coins!"
  - End the game

**Test:**
Does the game end when time runs out? Can you see your final score?

---

## Now You Have a Game!

Congratulations! You've built a complete game by breaking it down into smaller parts. Each part was simpler to solve than trying to build everything at once.

---

## Extra Challenges (Optional)

Once your game works, try adding these features:

### Challenge 1: Speed It Up
- As the score increases, make the enemy faster
- The game gets harder as you collect more coins!

### Challenge 2: Multiple Enemies
- Add a second enemy that moves differently
- Make the game more challenging

### Challenge 3: Power-Ups
- Create a special sprite that appears randomly
- When you collect it, gain extra lives or freeze the enemy

### Challenge 4: Sound & Effects
- Add sound effects when you collect a coin
- Add a buzzer when the enemy catches you
- Add a "victory sound" when you finish

### Challenge 5: Levels
- After collecting 10 coins, the game gets faster
- After 20 coins, enemies move even faster
- Create 3 difficulty levels!

### Challenge 6: High Score
- Keep track of your best score
- When you finish, compare to your high score

---

## Reflection & Design Thinking

Think about these questions:

1. **What made your game fun?** Was it the movement, the challenge, or something else?
2. **What was hard to code?** Which part took the longest to figure out?
3. **How did breaking it into steps help?** Would it have been harder to build the whole game at once?
4. **What would YOU add next?** What feature would make it even better?
5. **Why do video game designers use decomposition?** Why is it important to break big problems into smaller ones?

---

## Tips for Debugging

If something doesn't work:
- **Player won't move?** Check that you have button event blocks and movement code.
- **Coins not appearing?** Check that you're creating a coin every 1 second and displaying it.
- **Score not updating?** Make sure the overlap event is set up and score is displayed.
- **Enemy not moving?** Check that you have velocity or movement blocks for the enemy.
- **Game won't end?** Check that your timer block is connected to the "game over" logic.

---

## Resources

- [MakeCode Arcade](https://arcade.makecode.org)
- [MakeCode Arcade Tutorials](https://arcade.makecode.org/tutorials)
- [Arcade Documentation](https://arcade.makecode.org/reference)
