# Tic Tac Toe
### Harvard CS50's Introduction to Artificial Intelligence with Python (Project 0)

This game is never going to let you win!

## Description
In this project, an **Artificial Intelligence** bot has been implemented that never lets you win. This is an implementation of **minimax** - an *adversial search* algorithm - to find out the *best* next move which will lead to human player either loosing or drawing the match.<br>
**Alpha-beta pruning** is also implemented to optimize the algorithm: `minValue()` and `maxValue()` return the `action` as soon as they find a solution with `utility` of  `-1` and `1` respectively.

## Screenshots
<p align="center" style="font-size:12px;color:dimgray;">Gameplay <strong>(GIF - 42 seconds)</strong></p>
<p align="center">
    <img src="assets/gameplay.gif" alt="Gameplay"/>
</p>
<hr>
<p align="center" style="font-size:12px;color:dimgray">Main Menu</p>
<p align="center">
    <img src="assets/main-menu.png" alt="Main Menu"/>
</p>
<hr>
<p align="center" style="font-size:12px;color:dimgray">Gameplay - 1</p>
<p align="center">
    <img src="assets/gameplay-1.png" alt="gameplay one"/>
</p>
<hr>
<p align="center" style="font-size:12px;color:dimgray">Gameplay - 2</p>
<p align="center">
    <img src="assets/gameplay-2.png" alt="gameplay two"/>
</p>
<hr>
<p align="center" style="font-size:12px;color:dimgray">Game End</p>
<p align="center">
    <img src="assets/endgame.png" alt="end game"/>
</p>
