# Regicide
This is a single player game that simulates the Regicide Card game from [Badgers From Mars](https://badgersfrommars.com/).

The main diference here is that it's sigle player only, and (for now) is only a prompt game, there is no interface.

I'm not selling this code or earning any money from it, it's a public code so everyone could enjoy the game and check the code to learn more about programming.

# How to play
Regicide is a game where you have to defeat the royal family (the 3 royals of each suit) in the castle with the soldiers that you have. Each turn you send your soldiers to attack the royal member on top of the castle, if there is enough damage on board, it is defeated, but if not, you will take a hit too, and this hit makes you discard cards from hand.

You win when you clean up all the royals from the castle, and loses when you can't discard cards to take the hit.

To start the game, open the directory in your prompt and type:
```
python3 regicide.py
```

## Setup
Every game begins with a standard setup, the castle is build in a way that you have to defeat the Jackels first, then the Queens and finally the Kings. Every game the suit order of the castle will change. 

Then the remaining 40 cards of the deck will form the Tavern (these are your soldiers), from where draw cards. As your first hand, you always begin with 8 cards and that's also your max hand size.

## Turn steps
Each turn will have the same sequence of resolutions steps.

### 1 - Play card
You will type a card from hand the same way that they are prompted.
```
5 spades
```
The attack value of the card is the same as the number. Every card that you play deals damage to the royal. Besides playing a card you can 'yield' to the enemy, this way you won't play any card this turn. (I leave it to you to think about the usefulness of this.)

### 2 - Solving suit
Each suit has its own power, but two suit resolves at the moment that they are played, diamonds and hearts, the other two suits have their powers solved in future steps.
#### Hearts
Cards of hearts will take random cards, from the Discard pile, and add at the botton of the Tavern (Your soldiers have been healed). The number of cards healed this way is equal to the value of the played card, until the discard pile is empity. (Soldiers of hearts are like healers.)
#### Diamonds
Cards of diamonds will draw cards from the Tavern equals to the value of the played card, until your max hand size is reach or until the tavern is empity. (These are your mages.)
#### Clubs
Cards of clubs deals double damage to the royal, this happens at step 3. (These are your frontrank soldiers, who are the aggressive ones.)
#### Spades
Cards of spades that are on board, blocks the incoming damage from the royal, this happens at step 4. (These are your shildsmen, who protect you and your soldiers.)

### 3 - Check royal death
As you play cards, they are added to the board. The total damage of the cards must be greater or equal to the current royal life points (LP). Jackels have 20 LP and 10 attack power (AP), Queens have 30 LP and 15 AP, and Kings have 40 LP and 20 AP (Yeah, bro is huge). 

For example, you are facing a Jack of Hearts, as your first play, you play a 9 of spades from hand, this way the current damage on board is 9 and the Jack survive, then step 4 happens. After step 4 you can play another card, and you play a 6 of clubs (which deals double damage). So with a 9 of spades and a 6 of clubs on board, your total damage is 21, then the Jack of Hearts is dead.

When you kill a royal, two possibilites can happen, you kill them with total damage equal to its life or damage greater than its life. If the damage is greater, you put them in the Discard pile, but if you kill with damage equal to their LP, you put them in the top of the Tavern.

When the royal is that, all the cards on board are moved to the Discard pile (Yeah, they don't go back to your hand, they were wounded during the battle). Then a new royal appears and you go back to step 1.

### 4 - Take damage
If the royal is not dead, you will take damage equals to its attack. For each card of spades on board, the damage that you will take is reduced by the total power of the cards with spades.

To take damage, you have to discard cards until the total value of the cards discarded this way reaches at least the incoming damage. For instance, if you will take 10 damage from a Jack, you have to discards cards until the total value reaches at least 10, like a 6 spades and a 4 clubs, or 6 spades and a 5 hearts, the total value must be equal or greater than the incoming damage.

If you don't have enough cards in hand to take the damage, you lose the game.

After taking the damage, if you survive, you go back to step 1.

## Aces
The aces are companions, their value is 1 and they can be played with any other card. To do so, you have to choose a ace card first, then the game will ask you if you want to play another card. When you play an ace with another card you solve both suits and the total value is the sum of the values of both cards.

For instance, if you play a ace of diamonds with a 3 spades, you will draw 4 cards and in step 4 you will reduce damage by 4. If you play an ace with a card with the same suit, the suit only resolve once. (No, you can't double double the clubs cards.)

If you play an ace of dimonds with a card of hearts, or vice-versa, the hearts is solved before diamonds.

## Combos
If you have more than one card with the same value, you can play then together as long as the total value don't reach 10. So you can play a pair of 2s, 3s, 4s or 5s, triple 2s or 3s and quadruple 2s. You cannot play an ace with a combo but you can do a combo only with aces. If you play cards this way, each suit is resolve with total value equal to the sum of the cards' values. 

For instance, you a 3 of diamonds, clubs and spades, you will draw 9 cards, take 9 less damage from royal and deals 18 damage. If you play diamonds with hearts, the hearts will be solved first.

## Enemy immunity
The suit of the royal will counter the suit of the cards that you play. This means that, for example, if the current royal is a Jack of clubs, cards with clubs won't deal double damage against him. The same logic happens with other cards (Be careful with the enemies of diamonds, you can easily run out of cards).

## Jester
You begin the game with 2 jesters outside the tavern. If you play a jester, you discard your current hand and draw 8 new cards from the tavern (royals of diamonds don't counter this draw). You can only use a jester, on step 1, before playing a card (in this case, you type 'jester' instead of typing a card), or in step 4 before taking damage, in this case the game will ask you if you want to use it.

## Drawing a enemy
As above, when you defeat a royal, it can go to the discard pile or the tavern. They work as the other soldiers and their value is equal to their attack power. (I love when I defeat a royal of clubs and use then to defeat the same royal of spades. You one shoot then, so cool.)

## Game end
The game ends after you clean up the castle, a victory, or if you can't discard cards to take damage from the royal, a loss. If you win the game with both jester, it's a golden victory, if you use one jester, a silver victory and if you use both jesters, a bronze victory.

# Conclusions
This game is my way of trainning/studying programming, I didn't use any IA to code it, you can see that in the code because some of the functions are written in a non-ellegant way, I'm totally sure that there is a better/optimized way to code this game.

There are some features that I wanted to add, but I don't know how yet, and I don't want use IA for it. For example, I really wanted a way to save all the output of the game on a .txt file, so you can read all the choices that you made in a run. 

If you have any suggestion on how to improve the game, feel free to add a issue or a pull request.