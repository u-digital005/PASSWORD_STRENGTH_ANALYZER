# PASSWORD_STRENGTH_ANALYZER
# Password Strength Analyzer

A simple Python tool that checks how strong your password is and gives suggestions to make it better.

---

## What is This?

When we create accounts on websites or apps, we always set a password. But most people use simple passwords like `123456` or `password` which are very easy to guess and not safe.

A **Password Strength Analyzer** solves this problem. It looks at your password and tells you how strong or weak it is based on certain rules. It also tells you what is missing in your password and suggests a stronger one.

## How It Works

The program checks your password against 6 rules — length, bonus length, uppercase letters, lowercase letters, numbers, and special characters. Every rule you pass adds 1 point to your score.

Based on the total score out of 6, the program decides the strength:

- **0 to 2 points** — Weak
- **3 to 4 points** — Moderate
- **5 to 6 points** — Strong

After checking, it shows you which rules you missed, so you know exactly what to fix. It also generates a random 14-character strong password as a suggestion.

## Features

- Checks your password against 6 security rules
- Shows a strength level: Weak, Moderate, or Strong
- Tells you exactly what is missing in your password
- Suggests a randomly generated strong password
- Remembers passwords used in the same session to avoid reuse

---



## Output
<img width="576" height="475" alt="Image" src="https://github.com/user-attachments/assets/502928fc-a7bf-491d-a7fa-3f74559d25ee" />
