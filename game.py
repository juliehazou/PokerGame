from deck import Deck, Card


class Hand:
    """
    Create the Hand class, which will draw 5 cards and store them.
    """

    def __init__(self):
        """
        Draw 5 cards from the deck, using a for loop.
        return: A hand containing 5 cards dealt from a shuffled deck.
        """
        hand = []
        for i in range(5):
            hand.append(deck.deal())
        self._hand = hand

    @property
    def hand(self):
        """
        Returns the list of cards in the hand.
        return: list of 5 Card objects
        """
        return self._hand

    def __str__(self):
        # Displays the hand when printed
        return str(self.hand)

    @property
    def is_flush(self):
        """
        Checks if all cards in the hand are of the same suit.
        return: TRUE if flush, FALSE otherwise
        """
        for card in self.hand:
            if card.suit != self.hand[0].suit:
                return False
        return True

    @property
    def num_matches(self):
        """
        Counts total number of rank matches in the hand.
        return: int value based on hand type (pair = 2, 2pair = 4, trip = 6, etc.)
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    pass
                elif self.hand[i].rank == self.hand[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Checks if the hand has one pair.
        return: TRUE if it has 1 pair, FALSE otherwise
        """
        if self.num_matches == 2:
            return True
        return False

    @property
    def is_2pair(self):
        """
        Checks if the hand has two pairs.
        return: TRUE if it has 2 pairs, FALSE otherwise
        """
        if self.num_matches == 4:
            return True
        return False

    @property
    def is_trip(self):
        """
        Checks if the hand has three of a kind.
        return: TRUE if 3 cards have the same rank, FALSE otherwise
        """
        if self.num_matches == 6:
            return True
        return False

    @property
    def is_full(self):
        """
        Checks if the hand has a full house (3 of a kind + 1 pair).
        return: TRUE if full house, FALSE otherwise
        """
        if self.num_matches == 8:
            return True
        return False

    @property
    def is_quad(self):
        """
        Checks if the hand has four of a kind.
        return: TRUE if 4 cards have the same rank, FALSE otherwise
        """
        if self.num_matches == 12:
            return True
        return False

    @property
    def is_straight(self):
        """
        Checks if the hand is a straight (5 consecutive ranks).
        return: TRUE if straight, FALSE otherwise
        """
        if self.num_matches != 0:
            return False
        self.hand.sort()
        if Card.RANKS.index(self.hand[-1].rank) != Card.RANKS.index(self.hand[0].rank) + 4:
            return False
        return True

count = 0
matches = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    h = Hand()
    count += 1
    if h.is_straight:
        matches += 1

print(100 * (matches / count))