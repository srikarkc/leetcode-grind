# Math and Logic Puzzles

1. Give 2 ropes that take exactly 1 hour to burn. Time exactly 15 minutes. Rope densities are uneven so it doesn't take exactly 1/2 hour to burn 1/2.

Answer:
Light rope 1 on both ends and rope 2 only on 1 end
When the rope 1 burns out, light the other end of rope 2
From the time the rope 2 2nd end burn meets the 1st burn, it takes 15 mins.

2. Given 9 balls and a balance, figure out the 1 heavier ball.

Answer:
Splitting into 4-4 groups makes the end case worse since we'll need 3 uses of the balance. So, instead split it into groups of 3, weigh the first two and then, 2 from the remaining.

3. Given 20 bottles of pills, 19 have 1g pills and 1 has 1.1g pill. Find the bottle with 1.1g pill with only 1 use of an exact scale.

Take 1 pill from the first bottle, 2 pills from the second bottle and so on and subtract 210g / 0.1. Based on the excess weight, can find the bottle.

4. Basketball game with 2 options - 1 shot or 2/3 shots.

Say 'p' is the probability of making 1 shot, then 2/3 shots -> 3p^2 - 2p^3

P(game1) > P(game2)
p > 3p^2 - 2p^3
(2p-1)(p-1) > 0
both terms should be negative since p < 1 => p - 1 < 0
(2p - 1) < 0
p < 1/2

So, for p between 0 & 0.5 - go with game 1 and p between 0.5 and 1, go with game 2.

5. Dominos - chess board (8*8) with corners cut off and given 31 domino pieces, will the board be covered evenly?

No. Chess board with 32 * 32 and corners cut-off will be 30 * 32 (black or white each exclusively).
31 domino pieces will cover 31 black & white square exactly but we need 30 and 32.

6. Ants on a triangle - probability of collision

Assume all things equal, when the ants move in the same direction, they collide. Either all move clockwise or all move anti-clockwise. The total options are 2^3 = 8.

P(collision) = 1 - P(no collision) = 1 - (2/8) = 3/4

For an n-vertex polygon -> 1 - (1/2)^(n-1)

7. Jug of water - given 3 and 5 L measure 4 L.

Fill 5 L and pour into 3L.
Pour 3L out.
Pour remaining 2L from 5L jug into 3L.
Fill 5L and pour 1L into 3L.
Remaining 4L in the 5L jug.

8. Blue-eyed island

It will take 'n' number of days for all blue-eyed people to leave where 'n' is the number of blue-eyed people.

9. Apocalypse

Gender ration will still remain about 0.5. Since in the long term, the ratio of boys to girls will be 1:1.

10. Egg drop problem - 100 floors 2 eggs. Minimize the number of drops for the worst case scenario.

Binary search does not work here since that makes the worst case as 50 drops for the 2nd egg.

If you drop each egg 10 floors, then the worst case is if the floor 99 is where the egg breaks so egg 1 breaks at floor 100 (10 drops) + egg 2 breaks at 9 drops = 19 drops (much better than 51 drops).

Say you have 10 floors, then start from floor 4, if egg 1 breaks, egg 2 checks 1, 2, 3.
then, floor 7, if egg 1 breaks, egg2 checks 5, 6
then, floor 9, if egg 1 breaks, egg2 checks 8
then floor 10

4 + 3 + 2 + 1 = 10 (which is equal to the number of floors)

x + (x - 1) + (x - 2) + ... + 1 = 100
x(x + 1) / 2 = 100
x = 13.65

round up x to 14 because rounding down x to 13 adds a lot more drops

11. 100 lockers - open all lockers in the first pass, 2nd pass, close every 2nd locker, every 3rd pass, toggle the 3rd locker and so on. How many lockers are open?

A door 'n' is toggled for every factor of 'n'.

A door is left open if it has odd number of factors.

The value of 'x' would odd if the number is a perfect square.

There are 10 perfect squares from 1 - 100. (1, 4, 9, 16, ...100)

So, 10 lockers are left open at the end.

12. Poison - 1000 bottles of soda - 1 poisoned. 10 strips

Use a binary search based approach.
