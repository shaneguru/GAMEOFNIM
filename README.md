# Overview
The game of nim is said to be originated in China, since it is a resemblance of jiǎnshízi (picking stones), since it is not verified yet, its exact origin is uncertain. The
name ‘Nim’ was given by Charles L. Bouton, who also developed the complete the
game in 1901. [1]
There also are many variants of this game such as the 21 game, the 100 game,
greedy nim, Grundy’s nim and etc.
The rules of game of nim is,
1. It is a two-player game.
2. The players will take turns to remove pieces from one pile,
the player can remove any number of items from the
selected pile.
3. Depending on the version played:
    - Normal play: the last player to remove a piece wins
    the game.
    - Misère: the last player to remove a piece loses the
      game
      
 # Solution
While researching on a possible solution I came across different types of ways and
methods which it was solved on.
###### Nimsum
Nimsum is the cumulative XOR value of the number of pieces in each pile at any
point of the game. It is the most straightforward solution since it is deterministic
and computes the solution in polynomial time.
###### Minimax
Minimax is a backtracking algorithm that is used to for making decisions. It
traverses through the game tree which has all the possible solutions for a given
position using the breadth first search method. It also uses the zero-sum rule
which means one players gain will be equal to the other players loss.
###### Reinforcement learning and Genetic Algorithm
Game of nim can also be solved using machine learning and evolutionary
algorithms, during my research these areas was not explored since implementing
it was a bit complicating i.e. advanced level knowledge about reinforcement
learning was required to perfectly understand and tune the model. Moreover,
since we already had a solution which perfectly solves the problem in polynomial
time, I chose to stick with it. (nimsum)

## Implemented solutions
The solutions that I chose to implement was nimsum and minimax. Nimsum using
the normal version and minimax using misère.
###### Nimsum
Nimsum is based on the binary digital sum of the pile sizes and it is said to have
two positions.
  - A player will be in a winning position if the nimsum equals to zero upon
    making a move.
  - A player will be in a losing position if the nimsum is not equal to zero upon
    making a move.
    
![Picture1](https://user-images.githubusercontent.com/42903047/120615094-43b76700-c49b-11eb-8889-df06a40627d6.jpg)
***[Nimsum in various positions – Normal play]***

Before even making the first move we will know that the monkey will win the
game, by calculating the nimsum in the above picture. The alien will only win if
the monkey makes incorrect move that will make the nimsum back to non-zero
upon moving.
In the picture, you will be able to see that the nimsum is calculated by converting
the pieces in each pile into binary and then performing exclusive OR.

###### Minimax
Minimax is a search method for game trees. It uses depth first search to traverse
through the tree and it said to have a time complexity of O(Bm ), B being all the
possible moves at point in the game and m being the depth of the tree.
Performance of minimax can be greatly improved by using alpha-beta pruning,
which is a technique to stop evaluating moves if there was a better move before
![Picture2](https://user-images.githubusercontent.com/42903047/120615850-0a332b80-c49c-11eb-955a-687550bd8647.jpg)
***[Minimax Algorithm with alpha-beta pruning]***
This image shows how the minimax algorithm traverses through the tree, the minimax
algorithm has two players max and min. Max will try to find a move that will have the
maximum payoff and min will be trying to find a move which has the minimum payoff.

# Solution
In conclusion, the aim of this task was to complete the problem-based learning 3
of the artificial and computational intelligence unit at Deakin university. After
completing the task, I was able to learn about the game of nim, its different
solutions, specifically nimsum and minimax. The execution times of the
implementation of nimsum and minimax was studied and was compared in with
different pile sizes, which helped me to understand how slow the minimax
algorithm gets when the depth of the game tree increases.

# References
[1] Bouton, Charles L. “Nim, A Game with a Complete Mathematical Theory.” Annals of
Mathematics, vol. 3, no. 1/4, 1901, pp. 35–39. JSTOR, http://www.jstor.org/stable/1967631-
Accessed 17 Sept. 2020.
[2] Massachusetts Institute of Technology (2009). Theory of Impartial Games. Retrieved
September 17, 2020, from http://web.mit.edu/sp.268/www/nim.pdf
[3] Carrigan, A. (n.d.). Solving the Game of Nim. Retrieved September 17, 2020, from
https://mountainscholar.org/bitstream/handle/20.500.11919/1335/Win%20Nim.pdf?sequenc
e=1&amp;isAllowed=y
[4] Ferguson, T. (2020). GAME THEORY. Retrieved 2020, from
https://www.cs.cmu.edu/afs/cs/academic/class/15859-f01/www/notes/comb.pdf
###### Code
https://en.wikipedia.org/wiki/Nim
https://en.wikipedia.org/wiki/Minimax
https://github.com/NGoutcher/nim-gameai/blob/357a2eaefaf37c9d0d144334e976c9c473a7a050/nimgame.py
https://github.com/islammohsen/NimGame-Python/blob/master/project.py
https://docs.python.org/3/library/tk.html
