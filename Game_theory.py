https://medium.com/@lohitmarodia/game-theory-competitive-programming-98120cc14da3



Game Theory [Competitive Programming]


Game Theory is a topic in competitive programming (certainly did not mean the one which evolved during 20th century world war, though that is also an interesting theory to read and ponder upon) , which is not that often asked, but usually problems do come up revolving around the topic in short contests with a mixture of other topics like range querying or greedy or dynammic programming.

Though this topic is more of an intuitive topic, but I shall try my best to develop your intuition in the same.

Pre Requisites: Logic in Computer Science (Naah, just joking :P, though need some logic to understand :3 )

Lets start with a simple problem.

Note: It is assumed in all problems, the characters play optimally (play to win).

Problem Statement:
Two players Alice (A) and Bob (B) are playing a game. The game consists of a pile of stones of size N. The game always begins with Alice making a move. A move means to either remove 1 stone or 2 stones from pile, and each person makes a move alternatively. The person to make the last move wins i.e. the person left with no stones to pick loses. [Recommend you to think about it yourself before moving ahead.]

Solution:
Lets try to analyze the problem from base cases. 
For N=1, A wins the game directly as A can directly pick up a stone, and B is left with none.
For N=2, A wins the game again (same reason as above).
For N=3, B wins the game disregard of whatever A moves.
For N=4, A wins the game again. A can pick up 1 stone and no matter what B does then, A can win.
Similary, when you write it for a few more Ns, you will realize that for multiples of 3, A will lose and in other cases A will win.

Hence, it can be deduced that the winning strategy is simply to bring down the opponent on a multiple of 3, cause for every non-multiple of 3, if you are at, you can reach a multiple of 3 (by removing one or two stones), and therefore you end up bringing the opponent at 3 stones, thereby winning the game. And if a player is already with multiple of 3 stones, he cannot bring other to a multiple of 3 state.

Therefore Multiple of 3 will be called a losing state and Non multiple of 3 will be called a winning state for the player about to move.

Let me bring in a new variety of the same problem. A superset of the above problem.

Problem Statement:
Two players Alice (A) and Bob (B) are playing a game. The game consists of a pile of stones of size N. The game always begins with Alice making a move. A move means to remove any number of stones in the range [3,5] , and each person makes a move alternatively. The person to make the last move wins i.e. the person left with no stones or less than 3 stones to pick loses. [Recommend you to think about it yourself before moving ahead.]

Solution:
For N=1, A loses, because cannot pick only 1 stone.
For N=2, A loses again, because she has to pick atleast 3 stones.
For N=3, A wins, cause she can pick 3 stones, and B will be left with none.
For N=4, A wins.
For N=5, A wins.
For N=6, A wins again, because she can pick up 4 stones, and hence B will be left with 2 stones, which he cannot pick.
For N=7, A wins again, because A can pick 5 stones, and again B is left with 2 stones only.
For N=8, A loses this time, because no matter how many stones he picks, B will always have a move to make and he will be able to reduce the pile to 0,1 or 2 stones.
Write a few more states ahead, and you will realize that, N = 8K, 8K+1, 8K+2 are losing states for the beginner how much ever he tries, he will lead the other player to a winning state.

So, I hope by now you would have understood that the trick is to analyze which states are winning states and losing states, identifying some bases cases, and then trying to think whether A can bring B to a losing state always.

The trick for any such problem, lets for picking coins in range [a,b] is to reduce the opponent always to a multiple of (a+b) always, because eventually, they will be left with (a+b) coins, whatever B plays, (let say X≥A coins) then A can easily pick rest of the coins (a+b-X), since a≤(a+b-X)≤ b always.

Few other variates also exist. Try the practice problem from another variate.

Practice Problem : CHEF AND COINS | CodeChef
Do checkout the editorial and comments even if you are able to solve it.

Properties of the Games above:

The games are sequential.
The games are impartial. (Will get back to partial impartial games in a while).
Both (or All) the players have complete information about the game i. e. there is no sort of secrecy involved in the game.
The game is guaranteed to end in finite number of moves. (No such way to pick up 0 coins, else, the game could have been different).
The game doesn’t end in a draw, that is, each game has a winner and loser.
Partial and Impartial Games:

An impartial game is defined as the game in which both players have the same set of moves to make, that is, there is no differentiation on the basis of who is playing given a situation or condition.

A partial is thereby a game in which the set of moves for both (or all) players differ and need not necessarily be same. For example, Chess is a partial game because one player is not allowed to move pieces of other player. Tic-Tac-Toe also is a partial game, because a player playing Criss cannot play Cross and a person playing Cross cannot play Criss. Also, the person playing Criss cannot complete his row/column/diagonal using the Crosses, and vice-versa.

Why introduce partial/impartial games concept? Because, every impartial game can be solved using Sprague-Grundy Theorem which essentially brings down every such game (impartial game) to the Game of Nim. (also called Nim-Game).

Mex Function and Grundy Numbers:
Before beginning with explanation of the Theorem or the Game of Nim, one needs to understand the Mex Function and Grundy Numbers.

Mex Function is simply defined as minimum excludant of a set, that is the minimum non-negative number not present in a set of given numbers.

Examples:
Mex ({0,1,3}) = 2
Mex ({1,2,3}) = 0
Mex({0,1,2}) = 3
Mex( {} ) = 0 ( Mex of Empty Set)

Grundy Numbers are defined for a state. Grundy Number of a state/position S is defined as the Mex of all Grundy numbers of states reachable from S.
It might be a bit confusing, but let me try to clear with an example.

Lets say N = 5 (pile of coins) and A and B are playing and a person can pick 1 or 2 coins at a time.

So, Lets calculate Grundy ( N = 5). Here, N=5 is a state.
The positions we can reach from N = 5 are N = 5–1 or N=5–2.
S: N = 5, Reachable States: S1: N=4, S2 : N=3

Therefore, Grundy ( N = 5) = Mex ( {Grundy(N=3) , Grundy(N=4) } ).

You can go on recursively, with (G(N=0)) = 0, since there is no reachable state from N=0, there it is same as Mex of Empty Set.

Hence you get G(N=1) = 1, G(N=2) = 2, G(N=3) = 0, G(N=4) = 1 and G(N=5) = 2.

Game of Nim (Nim Game)
Nim is played with a number of piles each containing some number of (not necessarily equal) stones. A turn of the game consists of removing any number of stones greater than 0 from any single pile. A subgame should in this case be considered to be a single pile since you can consider Nim with k piles to be a composite game consisting of k Nim games with one pile each. Notice that the subgames are independent in the sense that making a move in one of them does not change the position in any of the others.

I hope you understood, whats a nim game! Now, lets see some magic!

Sprague-Grundy Theorem

The Sprague-Grundy theorem says that a player(starter) loses iff (if and only if) the XOR of the Grundy number of the position in each subgame is 0. 
Now, in Nim with one pile the Grundy number of a position is very easy to calculate. It is simply the number of stones in the pile. You can prove this very easily by induction.

So, for a N piles having A1, A2, A3,…., AN stones in each, if,

G(A1) ^ G(A2) ^ G(A3) ^ … ^ G(AN) = 0, this means that the first player to move will lose. If the player is allowed to remove any number of stones from a pile, then G(X) = X, and the problem will become trivial.

Moral of the Story:

Determine whether the game is impartial or not (which it will always be).
Break the composite game into sub-games.
Then for each sub-game, calculate the Grundy Number at that position.
Then calculate the XOR of all the calculated Grundy Numbers.
If the XOR value is non-zero, then the player who is going to make the turn (First Player) will win else he is destined to lose, no matter what.
Proof of Sprague Grundy Theorem is beyond my capabilities.
Also, the implementation part of calculating Mex/Grundy Value is what I am leaving upto the reader, as there are many other resources available for the same.

Problems for Practice:
MMMGAME — M&M Game [SPOJ]
QCJ3 — The Game [SPOJ]
GAME3 — Yet Another Fancy Game [SPOJ]
GAME31 — The game of 31 [SPOJ]
Stone Game [CodeChef]
