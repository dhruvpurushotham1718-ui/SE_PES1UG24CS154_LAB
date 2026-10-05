# Bubble Bobble Repair Lab

This project is a single-file Bubble Bobble-lite clone using **Pygame**. It introduces students to projectile-then-buoyant motion, trap-and-release enemy state, and combo scoring using a small, readable object-oriented codebase.

---

## What's Provided

A working Bubble Bobble-lite game with:

- A player that walks and jumps across a set of platforms and blows bubbles that travel forward before floating upward
- Enemies that wander and occasionally jump, and can be trapped inside a bubble on contact
- Popping a bubble containing a trapped enemy drops a fruit worth points, with combo bonuses for popping several bubbles in one airborne streak
- Levels, lives, and scoring

It has **one deliberate bug** and **three optional features** left as empty functions. You are expected to **analyze**, **interact with an AI assistant**, and **complete/fix** the game to make it fully functional and more interesting.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**

---

## Getting Started

### Setup

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```bash
pip install pygame
```

3. Run the game:

```bash
python game.py
```

**Controls:** Arrow keys to move, Up to jump, Space to blow a bubble, `R` to reset.


## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Fix the bubble-trapping bug

> A bubble is supposed to trap any enemy it touches shortly after being blown. In the current build, trapping only works on an almost pixel-perfect overlap between the bubble and the enemy, so bubbles that clearly brush past an enemy fail to trap it. The distance check in `trap_enemies` compares a *squared* distance against a threshold that was never squared to match it. Fix the threshold so the comparison is consistent.

### Task 2: Implement `bubble_tint(bubble)`

> Called once per bubble per frame in `draw`, as `color = bubble_tint(bubble) or ((120, 230, 255) if bubble.enemy is None else (255, 190, 230))`. It receives the `Bubble` object (check `bubble.enemy` to see whether it has a trapped enemy) and should return an `(r, g, b)` color, or `None` to keep the default. Idea: color bubbles by how close they are to expiring (`bubble.life`).

### Task 3: Implement `on_fruit_collected(fruit)`

> Called from `update()` the instant the player touches a fruit, right after its points are added and it's removed from play. It receives the `Fruit` that was collected. Its return value is ignored. Idea: a sparkle effect, or a running collected-fruit counter in the HUD.

### Task 4: Implement `bonus_life_threshold()`

> Called every frame in `update()`. It takes no arguments and should return an integer score value, or `None` to disable bonus lives entirely. Whenever the score crosses a multiple of that value for the first time, one life is awarded automatically — the bookkeeping (`self.bonus_awarded`) is already implemented, so you only need to choose the threshold. Idea: return `5000`.

---

## Expected Behavior

- Bubbles travel forward briefly before rising, and eventually float off the top of the screen if never popped
- A bubble touching an enemy traps it inside; popping that bubble from above releases a fruit
- Combo score for chained pops resets once the player lands back on a platform
- A trapped enemy that isn't popped in time escapes and resumes wandering
- Clearing every enemy on a level (with no unpopped trapped ones left) advances to the next level

---

## Folder Structure

```
bubble_bobble/
├── game.py
└── README.md
```

---

## Submission Checklist

Submission is only the following three things:

- [] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [] The Chat/LLM used page link, with the complete chat history
