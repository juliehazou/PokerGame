import random


class Card:
    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    SUITS = ["♠", "♣", "♦", "♥"]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        self._rank = rank
        self._suit = suit

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit


class Deck:
    def __init__(self):
        _cards = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                _cards.append(Card(rank, suit))
        self._deck = _cards

    @property
    def deck(self):
        return self._deck

    def __str__(self):
        return f"{self._deck}"

    def shuffle(self):
        random.shuffle(self._deck)

    def deal(self):
        return self._deck.pop(0)


if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck.deal())

# c1 = Card("A", "♠")
# print(c1)