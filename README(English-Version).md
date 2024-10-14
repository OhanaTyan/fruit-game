
# Fruit-Game

## Game Rules

1. There are a total of 5 types of fruit cards, labeled as `abcde`, with 4 cards of each type. There are 4 players.
   > The frontend can be modified appropriately so that they can actually be fruit cards.
2. At the beginning of the game, each player is randomly dealt 4 cards, and the remaining 4 cards are placed on the table. Each player can only see their own cards and the cards on the table. If, after dealing, a player's cards are all of the same type of fruit, or if the cards on the table are all of the same type of fruit, the cards are dealt again.
3. Each player takes turns to perform the following actions: first play one of their cards onto the table, then take one card from the table, but must ensure the following conditions:
   > 1. The card played and the card taken cannot be of the same type of fruit.
   > 2. After the operation, the 4 cards on the table cannot all be of the same type of fruit.
4. The player who first has all their remaining cards of the same type of fruit ranks first.
5. Even if a player has ranked first, the game continues, but during subsequent turns, the already winning player will be skipped. The player who ranks first at this point can choose to exit the game or watch. The second player to have all their cards of the same type ranks second, and the third ranks third, and so on.
6. About exiting the game: If a player has already won (meaning they have made all their cards of the same type), their exit from the game does not affect the other players; however, among the players who have not won, if one player of them chooses to exit, the game will end.
