---
layout: default
title: Coin Collector - Teacher Guide
---

# Coin Collector Game (Teacher Guide)

This guide helps you teach **Coin Collector** using a **problem decomposition** and **prompting-based learning** approach. The focus is on guiding students to discover solutions rather than giving them step-by-step instructions.

---

## Learning Objectives

By the end of this project, students will:
- Break down a complex problem into smaller, manageable parts
- Understand **decomposition** as a core computer science skill
- Use **MakeCode Arcade** to build a complete game
- Develop problem-solving and debugging skills
- Think critically about game design and user experience
- Reflect on their design choices

---

## Teaching Strategy: Prompting, Not Telling

Instead of saying "*Add this block here*," ask **questions** that guide students to their own solutions:

**❌ Don't:** "Drag the 'set player to sprite' block into the 'on start' block."

**✅ Do:** "How do you think we create a player sprite? What block might let us do that?"

This approach helps students:
- Develop problem-solving skills
- Remember solutions longer
- Build confidence in their abilities
- Learn to debug independently

---

## Lesson Structure

### Suggested Timeline
- **Session 1:** Introduction & Decomposition (15-20 mins)
- **Sessions 2-3:** Build the Player (20-30 mins each)
- **Sessions 3-4:** Coins & Scoring (20-30 mins each)
- **Sessions 5-6:** Enemy & Lives (20-30 mins each)
- **Sessions 6-7:** Timer & Winning (20-30 mins each)
- **Sessions 8+:** Polish, Extensions, Showcase

(Times are flexible based on your group's pace)

---

## Session 1: Introduction & Decomposition

### Warm-Up (5 mins)
Show students a simple game or ask: **"What makes a game fun?"**

Discuss elements like:
- Challenge
- Clear goals
- Rewards (score, progress)
- Variety or surprise

### Introduce the Project (5 mins)
Show the [presentation](./index.html) or describe the game:
- "We're building a game where you collect coins, avoid an enemy, and race against time."

### The Big Idea: Decomposition (10 mins)

**Ask:** "If we tried to build the whole game at once, what would be hard?"

Guide students to realize:
- There are many moving parts
- It's easier to build one piece at a time
- We can test each piece before adding the next

**Show the breakdown:**

| Component | What It Does |
|-----------|--------------|
| Player | Moves around, can be controlled |
| Coins | Appear, get collected, disappear |
| Enemy | Moves, catches player, causes game over |
| Score | Tracks collected coins |
| Lives | Tracks remaining lives |
| Timer | Counts down, ends game |

**Ask:** "Which piece should we build first? Why?"

(The **player** is usually the best starting point — students need something to control before adding the world around it.)

---

## Sessions 2-3: Build the Player

### Guiding Questions

Instead of telling students what to do, ask:

1. **"What should your player look like?"**
   - Help them choose or design a sprite
   - Discuss: Does it match the game theme? Is it easy to see?

2. **"Where should the player start?"**
   - Center? Corner? Random position?
   - How do we position a sprite on the screen?

3. **"How do we move the player?"**
   - Button presses? Arrow keys? Both?
   - What blocks control movement?
   - Prompt: "What's an 'event' that could trigger movement?"

4. **"Should the player stay on screen?"**
   - What happens if they go off the edge?
   - Should they wrap around or stop?

### Tips for Guidance

**If a student is stuck:**
- Ask: "What block do you think you need?"
- Say: "Look in the 'sprites' menu — what looks useful?"
- Encourage: "Try it and see what happens!"

**If they get it wrong:**
- Celebrate the attempt: "Good try! What happened?"
- Guide: "Does the player move the way you wanted? What should we change?"

**If they finish early:**
- Ask: "Can you move diagonally? What if you press two buttons at once?"
- Challenge: "Can you make the player faster or slower?"

### Testing Checkpoint
Ask: **"Can you move your player around the screen the way you want?"**

---

## Sessions 3-4: Coins & Scoring

### Guiding Questions

1. **"What should coins look like?"**
   - Pick a sprite or draw one
   - Keep it simple and recognizable

2. **"When should coins appear?"**
   - All at once? One by one? Every few seconds?
   - What blocks could make something repeat?
   - Prompt: "Look in 'loops' — what might repeat something every second?"

3. **"What happens when the player touches a coin?"**
   - Score goes up
   - Coin disappears
   - A new coin appears (or we spawn another)
   - What blocks detect overlap? (Hint: "sprites overlapping")

4. **"Where should we display the score?"**
   - Top of the screen? Corner?
   - Should we show a label like "Score: 5"?

### Common Misconceptions

**"Coins only appear once"**
- Guide: "If there are only 3 coins total, what happens after we collect them?"
- Prompt: "How do we make coins keep appearing?"

**"Score increases, but coins don't disappear"**
- Discuss: "What feels better — coins disappearing when collected, or coins overlapping forever?"
- Guide: "We probably want to destroy the coin after counting it."

### Testing Checkpoint
Ask: **"Can you collect coins and see your score go up? Do new coins appear?"**

---

## Sessions 5-6: Enemy & Lives

### Guiding Questions

1. **"What should the enemy look like?"**
   - Different from the player and coins
   - Make it clear it's a threat

2. **"How should the enemy move?"**
   - Stay still? Move randomly? Chase the player?
   - What blocks can move a sprite?
   - Discuss: Does it feel like a challenge?

3. **"What happens if the player touches the enemy?"**
   - Lose a life
   - What happens next? Does the player respawn?
   - Should there be a brief "safe time" so they can escape?

4. **"How many lives should the player have?"**
   - 3? 5? 1? Why?
   - Discuss game difficulty

5. **"What does 'game over' mean?"**
   - All lives lost? Something else?
   - What should the screen show?

### Difficulty & Balancing

**Ask:** "Is the game too easy or too hard? Why?"

- Too easy? Make the enemy faster, add more enemies, reduce starting lives
- Too hard? Slow the enemy, give more lives, let coins heal you

### Testing Checkpoint
Ask: **"Can you touch the enemy and lose a life? Does the game end when you lose all lives?"**

---

## Sessions 6-7: Timer & Winning

### Guiding Questions

1. **"How long should the game last?"**
   - 30 seconds? 60 seconds? 90 seconds?
   - Discuss: Is there enough time to collect coins AND avoid the enemy?

2. **"How do we count down time?"**
   - What variable tracks the timer?
   - What blocks decrease it every second?
   - Prompt: "Look in 'loops' — what repeats every 1 second?"

3. **"What happens when time runs out?"**
   - Show the final score
   - Stop all movement
   - Let players try again? (Game over, or keep playing?)

4. **"How do we 'win'?"**
   - Is there a target score?
   - Or do you just survive until time ends?

### Testing Checkpoint
Ask: **"Does the game end when time runs out? Can you see your final score?"**

---

## Session 8+: Extensions & Polish

Once the core game works, guide students toward extensions:

### For Students Who Want More Challenge

1. **"How could you make the game harder over time?"**
   - Speed up the enemy every 10 coins
   - Shorten the timer
   - Add more enemies

2. **"What's a special power-up you could add?"**
   - Shield that protects from enemy
   - Freeze enemy for 3 seconds
   - Extra life or extra time

3. **"How could players get better at your game?"**
   - Practice mode (no timer)
   - Difficulty levels (easy, normal, hard)
   - High score tracker

### For Students Who Want Creative Features

1. **"How would you customize your game?"**
   - Different art style
   - Different music/sounds
   - Different story or theme

2. **"How would you make it visually better?"**
   - Screen transitions
   - Particle effects when coins are collected
   - Camera effects

---

## Debugging & Common Issues

**Player won't move:**
- Check: Is the button event firing? (Test by adding a sound/effect)
- Check: Is the velocity set correctly?
- Ask: "What should happen when you press this button?"

**Coins don't appear:**
- Check: Is the "every 1 second" block running?
- Check: Is the coin being positioned on screen?
- Ask: "Where should coins appear? How do we pick a random spot?"

**Score doesn't update:**
- Check: Is the overlap event detected? (Add a sound to test)
- Check: Is score actually being changed?
- Ask: "How do we know the player touched the coin?"

**Game never ends:**
- Check: Is the timer decreasing?
- Check: Is the "game over" logic connected?
- Ask: "What should happen when timer = 0?"

**Enemy too easy/hard:**
- Speed: "Should we increase the velocity?"
- Behavior: "Should the enemy chase or move randomly?"
- Quantity: "Should there be more than one?"

---

## Encouraging Problem-Solving

**When students are stuck:**

1. **Restate the problem** — "So you want the coin to disappear after being collected?"
2. **Ask guiding questions** — "What blocks might destroy a sprite?"
3. **Suggest a resource** — "Let's look at the sprites menu together"
4. **Celebrate attempts** — "Great try! What happened when you ran it?"
5. **Test together** — "Let's see what this block does"

**When students finish quickly:**

- Ask them to teach another student
- Challenge them to add a feature
- Ask them to debug someone else's code
- Have them improve the design (colors, sprites, sounds)

---

## Reflection Questions

At the end of the project, discuss:

1. **"Which part was hardest to build? Why?"**
2. **"How did breaking it into parts help?"**
3. **"What surprised you about game design?"**
4. **"What would you do differently next time?"**
5. **"How do professional game designers use decomposition?"**

---

## Learning Outcomes

By the end of this project, students should be able to:

✅ **Decompose** a complex problem into smaller parts  
✅ **Plan** their code before writing it  
✅ **Implement** game logic using events and sprites  
✅ **Debug** code by testing each component  
✅ **Reflect** on their design and problem-solving process  
✅ **Extend** their game with new features  

---

## Resources for Teachers

- [MakeCode Arcade](https://arcade.makecode.org)
- [Arcade Tutorials](https://arcade.makecode.org/tutorials)
- [Sprite & Collision Guide](https://arcade.makecode.org/reference)
- [Game Design Tips](https://arcade.makecode.org/tutorials/game-design)

---

## Notes

- **Pacing:** Adjust based on your students' experience. Beginners may need more time per section.
- **Scaffolding:** Provide sentence starters: "I think we should... because..."
- **Collaboration:** Pair students so they can discuss design choices together.
- **Share:** Have students share their games and explain their design decisions.
