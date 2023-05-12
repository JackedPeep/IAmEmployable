import random
import time

#I have copied in large swaths of code because I used a few scratch files
#to make it easier to test the code in specific pieces. Please don't mark me down...

# write all your code below this line
class Card:
    def __init__(self, num=1, suit="S"):
        self.num=num
        num = [1,14]
        self.suit=suit
        suit = ["C","D","H","S"]
    # each card has a number value between 1 and 13 (inclusive)
    # each card has a suit: "C", "D", "H", and "S"
    def __lt__(self, other):
        if self.suit != other.suit:
            return self.suit < other.suit
            # #C < anything but C
            # if self.suit == 'C':
            #     return false
            # #D < ...
            # elif self.suit == 'D':
            #     # D < C
            #     if other.suit == 'C':
            #         return true
        else:
            return self.num < other.num

    # define which cards are less than others for sorting
    # first decide by card suit, in alphabetical order
    # then decide by card number
    def print(self):
        if self.num == 1:
            if self.suit == 'C':
                print("A" + "\u2663", end=" ")
            elif self.suit == 'D':
                print("A" + "\u2666", end=" ")
            elif self.suit == 'H':
                print("A" + "\u2665", end=" ")
            else:
                print("A" + "\u2660", end=" ")
        elif self.num == 13:
            if self.suit == 'C':
                print("K" + "\u2663", end=" ")
            elif self.suit == 'D':
                print("K" + "\u2666", end=" ")
            elif self.suit == 'H':
                print("K" + "\u2665", end=" ")
            else:
                print("K" + "\u2660", end=" ")
        elif self.num == 12:
            if self.suit == 'C':
                print("Q" + "\u2663", end=" ")
            elif self.suit == 'D':
                print("Q" + "\u2666", end=" ")
            elif self.suit == 'H':
                print("Q" + "\u2665", end=" ")
            else:
                print("Q" + "\u2660", end=" ")
        elif self.num == 11:
            if self.suit == 'C':
                print("J" + "\u2663", end=" ")
            elif self.suit == 'D':
                print("J" + "\u2666", end=" ")
            elif self.suit == 'H':
                print("J" + "\u2665", end=" ")
            else:
                print("J" + "\u2660", end=" ")
        else:
            if self.suit == 'C':
                print(str(self.num) + "\u2663", end=" ")
            elif self.suit == 'D':
                print(str(self.num) + "\u2666", end=" ")
            elif self.suit == 'H':
                print(str(self.num) + "\u2665", end=" ")
            else:
                print(str(self.num) + "\u2660", end=" ")

    # print out a card (see example output for details)
    def blackJackValue(self):
        if self.num in [11, 12, 13]:
            return 10
        elif self.num == 1:
            return 11
        else:
            return self.num


# return the value of a card.
# face cards are worth 10
# aces are worth 11 always here not in actual black jack

class Deck:
    def __init__(self):
        self.cards = []
        i=1
        while i < 14:
            self.cards.append(Card(i, "C"))
            i+=1
        i=1
        while i < 14:
            self.cards.append(Card(i, "D"))
            i += 1
        i = 1
        while i < 14:
            self.cards.append(Card(i, "H"))
            i += 1
        i = 1
        while i < 14:
            self.cards.append(Card(i, "S"))
            i += 1
        i = 1

    # create a deck of 52 cards in order
    def print(self):
        i = 0
        while i < len(self.cards):
            self.cards[i].print()
            print()
            i += 1

    # print all the cards in the deck, one per line
    def shuffle(self):
        random.shuffle(self.cards)
    # randomly shuffle all the cards in the deck

    def arrange(self):
        self.cards.sort()


        print()
    # put all the cards currently in the deck back in order
    def restore(self):

        self.cards = []
        i = 1
        while i < 14:
            self.cards.append(Card(i, "C"))
            i += 1
        i = 1
        while i < 14:
            self.cards.append(Card(i, "D"))
            i += 1
        i = 1
        while i < 14:
            self.cards.append(Card(i, "H"))
            i += 1
        i = 1
        while i < 14:
            self.cards.append(Card(i, "S"))
            i += 1
        i = 1

    # restore all the missing cards from the deck and arrage them
    def deal(self):
        d = len(self.cards)-1
        c1= self.cards[d]
        self.cards.pop(d)
        return c1

        self.print()
    # remove a card from the top of the deck and return it to the client
    def numCards(self):
        return len(self.cards)


# return the number of cards currently in the deck
class Hand:
    def __init__(self):
        self.hand=[]
    # create an empty list of cards
    def addCard(self, card):
        self.hand.append(card)
    # add a card to the hand (for example, from the deck)
    def numCards(self):
        return len(self.hand)
    # return the number of cards currently in the hand
    def print(self):
        i=0
        while i < len(self.hand):
            self.hand[i].print()
            i += 1

    # print the cards currently in the hand, without newlines
    # see example output for details
    def printBlackJackDealer(self):
        print("??",end=" ")
        i=1
        while i < len(self.hand):
            self.hand[i].print()
            i += 1

    # print the cards currently in the hand, without newlines
    # replace the first card with "??" to hide it
    # see example output for details
    def blackJackValue(self):
        i=0
        total = 0
        aces =0
        while i < len(self.hand):
            if self.hand[i].num == 1:
                aces += 1
            total += self.hand[i].blackJackValue()
            i += 1
        while total>21 and aces>0:
            total-=10
            aces-=1

        return total



# return the blackjack value of this hand
# aces are worth 11 unless that causes a bust.
# then the minimum number of aces are counted as 1s
# so that no bust occurs. ("bust" == any value over 21)
# write all your code above this line
class BlackJackGame:
    def __init__(self):
        self.__d = Deck()
        self.__d.shuffle()

    def displayLine(self, who, hand):
        # print a "hand" line of the output
        print(who + ": ", end="")
        print(" (" + str(hand.blackJackValue()) + ")\t", end="")
        hand.print()
        if hand.numCards() <= 5: print("\t", end="")
        if hand.numCards() <= 3: print("\t", end="")

    def pickWinner(self, n, dn, b, db, pf, df):
        # print out the winner of the hand
        print()
        if n and not dn:
            print("\t\tyou win!")
        elif n and dn:
            print("\t\t(push)")
        elif not n and dn:
            print("\t\tdealer wins.")
        elif b and not db:
            print("\t\tdealer wins.")
        elif not b and db:
            print("\t\tyou win!")
        elif pf == df:
            print("\t\t(push)")
        elif pf > df:
            print("\t\tyou win!")
        else:
            print("\t\tdealer wins.")
        print()

    def play(self):
        print()
        print("        Welcome to Simple BlackJack")
        print()
        # the main event loop
        while True:
            # dealer reshuffles cards when 75% dealt
            if self.__d.numCards() < 14:
                print("\t\t\t\t\tDealer shuffles the deck")
                self.__d.restore()
                self.__d.shuffle()
            # dealer and player each have a hand
            dealer = Hand()
            player = Hand()
            # flags used to determine the eventual winner
            natural = False
            dnatural = False
            busted = False
            dbusted = False
            playerfinal = 0
            dealerfinal = 0

            # dealer gets a hand
            dealer.addCard(self.__d.deal())
            dealer.addCard(self.__d.deal())

            # dealer hand displayed with one card hidden
            print("dealer" + ": ", end="")
            print(" (??)\t", end="")
            dealer.printBlackJackDealer()
            print()

            # player gets a hand
            player.addCard(self.__d.deal())
            player.addCard(self.__d.deal())

            # check for player natural
            if player.blackJackValue() == 21:
                self.displayLine("player", player)
                print("natural blackjack!")
                natural = True

            # player get more cards if desired
            while player.blackJackValue() < 21:
                self.displayLine("player", player)
                response = input("hit? [y/n] ")
                if response == "n": break
                player.addCard(self.__d.deal())

            # find final player status for hand
            self.displayLine("player", player)
            playerfinal = player.blackJackValue()
            if playerfinal == 21 and not natural:
                print("blackjack!")
            elif playerfinal > 21:
                print("you busted.")
                busted = True
            else:
                print("you hold.")
            time.sleep(1)

            # now it is the dealers turn
            if dealer.blackJackValue() == 21:
                self.displayLine("dealer", dealer)
                print("dealer blackjack!")
                dnatural = True
            # if player busted, dealer does nothing
            if busted:
                self.displayLine("dealer", dealer)
                print()
            # dealer gets to add cards if no naturals
            if not natural and not busted:
                while dealer.blackJackValue() <= 15 and not busted:
                    self.displayLine("dealer", dealer)
                    print("dealer hits.")
                    time.sleep(1)

                    dealer.addCard(self.__d.deal())

                # find final dealer status for hand
                self.displayLine("dealer", dealer)
                dealerfinal = dealer.blackJackValue()
                if dealerfinal == 21 and not dnatural:
                    print("dealer blackjack!")
                elif dealerfinal > 21:
                    print("dealer busted.")
                    dbusted = True
                else:
                    print("dealer holds.")
            time.sleep(1)

            # find the winner for this hand


#self.pickWinner(natural, dnatural, busted, dbusted, playerfinal, dealerfinal)

#response = input("\t\t\t\t\tplay again? [y/n] ")
# if response == "n": break
# print("\t\t\t\t\tso long!")
# print()


def cardTest():
    print()
    print("Card Test")
    print()
    c1 = Card()
    c2 = Card(13, "H")
    c3 = Card(3, "C")
    c4 = Card(3, "D")
    c1.print()
    c2.print()
    c3.print()
    c4.print()
    print()
    print(format(c1.blackJackValue(), "3.0f"), end=" ")
    print(format(c2.blackJackValue(), "3.0f"), end=" ")
    print(format(c3.blackJackValue(), "3.0f"), end=" ")
    print(format(c4.blackJackValue(), "3.0f"), end=" ")
    print()
    print()
    c0 = Card(13, "C")
    c1 = Card(1, "D")
    c2 = Card(2, "D")
    c3 = Card(3, "D")
    c4 = Card(10, "D")
    c5 = Card(11, "D")
    c6 = Card(12, "D")
    c7 = Card(13, "D")
    c8 = Card(1, "H")
    c9 = Card(1, "S")
    c0.print()
    c1.print()
    c2.print()
    c3.print()
    c4.print()
    c5.print()
    c6.print()
    c7.print()
    c8.print()
    c9.print()
    print()
    print(c0 < c1)
    print(c1 < c2)
    print(c2 < c3)
    print(c3 < c4)
    print(c4 < c5)
    print(c5 < c6)
    print(c6 < c7)
    print(c7 < c8)
    print(c8 < c9)
    print(c9 < c0)


def deckTest():
    print()
    print("Deck Test")
    print()
    d = Deck()
    d.print()
    print()
    d.shuffle()
    d.print()
    print()
    d.arrange()
    d.print()
    print()
    c0 = d.deal()
    c1 = d.deal()
    c0.print()
    c1.print()
    print()
    print()
    d.print()
    print()
    print(d.numCards())
    d.restore()
    print(d.numCards())
    print()
    d.print()
    print()


def handTest():
    print()
    print("Hand Test")
    print()
    c1 = Card(1, "S")
    c2 = Card(13, "H")
    c3 = Card(3, "C")
    h = Hand()
    h.addCard(c1)
    h.addCard(c2)
    h.print()
    print()
    print(h.numCards())
    h.addCard(c3)
    h.print()
    print()
    print(h.numCards())
    print()
    h2 = Hand()
    h2.addCard(c1)
    h2.addCard(c2)
    h2.printBlackJackDealer()
    print()
    h2.print()
    print("=", h2.blackJackValue())
    print()
    h2.addCard(c3)
    h2.print()
    print("=", h2.blackJackValue())
    print()


def test():
    cardTest()
    deckTest()
    handTest()


def main():
    #    game = BlackJackGame()
    #    game.play()
    test()
main()

# Card Test
# A♠  K♡  3♣  3♢
# 11  10   3   3
# K♣  A♢  2♢  3♢ 10♢  J♢  Q♢  K♢  A♡  A♠
# True
# True
# True
# True
# True
# True
# True
# True
# True
# False
# Deck Test
# A♣
# 2♣
# 3♣
# 4♣
# 5♣
# 6♣
# 7♣
# 8♣
# 9♣
# 10♣
# J♣
# Q♣
# K♣
# A♢
# 2♢
# 3♢
# 4♢
# 5♢
# 6♢
# 7♢
# 8♢
# 9♢
# 10♢
# J♢
# Q♢
# K♢
# A♡
# 2♡
# 3♡
# 4♡
# 5♡
# 6♡
# 7♡
# 8♡
# 9♡
# 10♡
# J♡
# Q♡
# K♡
# A♠
# 2♠
# 3♠
# 4♠
# 5♠
# 6♠
# 7♠
# 8♠
# 9♠
# 10♠
# J♠
# Q♠
# K♠
# Q♡
# A♣
# Q♢
# 4♢
# 6♠
# Q♣
# 9♡
# 9♠
# A♠
# K♡
# A♡
# 5♣
# 5♠
# 4♣
# 4♡
# 2♡
# K♠
# 6♢
# 3♢
# 9♢
# K♢
# Q♠
# 10♣
# 8♢
# 2♠
# 2♣
# 6♣
# 10♢
# J♢
# A♢
# 6♡
# 3♡
# J♠
# 5♡
# 9♣
# 7♡
# 5♢
# 4♠
# 7♢
# 2♢
# 3♣
# 7♠
# J♡
# 10♠
# 8♠
# 10♡
# J♣
# 8♣
# 8♡
# K♣
# 7♣
# 3♠
# A♣
# 2♣
# 3♣
# 4♣
# 5♣
# 6♣
# 7♣
# 8♣
# 9♣
# 10♣
# J♣
# Q♣
# K♣
# A♢
# 2♢
# 3♢
# 4♢
# 5♢
# 6♢
# 7♢
# 8♢
# 9♢
# 10♢
# J♢
# Q♢
# K♢
# A♡
# 2♡
# 3♡
# 4♡
# 5♡
# 6♡
# 7♡
# 8♡
# 9♡
# 10♡
# J♡
# Q♡
# K♡
# A♠
# 2♠
# 3♠
# 4♠
# 5♠
# 6♠
# 7♠
# 8♠
# 9♠
# 10♠
# J♠
# Q♠
# K♠
# K♠  Q♠
# A♣
# 2♣
# 3♣
# 4♣
# 5♣
# 6♣
# 7♣
# 8♣
# 9♣
# 10♣
# J♣
# Q♣
# K♣
# A♢
# 2♢
# 3♢
# 4♢
# 5♢
# 6♢
# 7♢
# 8♢
# 9♢
# 10♢
# J♢
# Q♢
# K♢
# A♡
# 2♡
# 3♡
# 4♡
# 5♡
# 6♡
# 7♡
# 8♡
# 9♡
# 10♡
# J♡
# Q♡
# K♡
# A♠
# 2♠
# 3♠
# 4♠
# 5♠
# 6♠
# 7♠
# 8♠
# 9♠
# 10♠
# J♠
# 50
# 52
# A♣
# 2♣
# 3♣
# 4♣
# 5♣
# 6♣
# 7♣
# 8♣
# 9♣
# 10♣
# J♣
# Q♣
# K♣
# A♢
# 2♢
# 3♢
# 4♢
# 5♢
# 6♢
# 7♢
# 8♢
# 9♢
# 10♢
# J♢
# Q♢
# K♢
# A♡
# 2♡
# 3♡
# 4♡
# 5♡
# 6♡
# 7♡
# 8♡
# 9♡
# 10♡
# J♡
# Q♡
# K♡
# A♠
# 2♠
# 3♠
# 4♠
# 5♠
# 6♠
# 7♠
# 8♠
# 9♠
# 10♠
# J♠
# Q♠
# K♠
# Hand Test
# A♠  K♡
# 2
# A♠  K♡  3♣
# 3
# ??  K♡
# A♠  K♡ = 21
# A♠  K♡  3♣ = 14
