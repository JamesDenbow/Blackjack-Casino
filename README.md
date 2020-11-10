# Blackjack-Casino (V 2.2.1)
A simple Blackjack game allowing a player to play against additional CPU players.

### About
This game is a single deck Blackjack game that allows a player to play up against up to 4 CPU players. Each CPU player can be given a name and have a difficulty setting from beginner, normal or expert. The user can then select what position at the table they wish to sit and how much money all players start out with. The first round would then begin by asking the user for their bet on the hand. The game will continue round after round until the user runs out of money. The game allows the user to hit, stay and double per standard blackjack rules.

### Dependancies
 * Python 3.8.2
 
### Known Bugs
 * Occasionally there is a failure to display the statistics and analysis panel during the turn
 * There is an occasional crash giving the error of "User_index is out of range" this is caused due to a problem that araises when calculating what place at the table the user controlled player is at.
 
 ### Future Additions
  * Version 2.3 - Add the ability to split hands per the standard rules of Blackjack.
  
 ### License
MIT License

Copyright (c) 2020 James Denbow

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
