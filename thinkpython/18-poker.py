#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import shuffle


class Card(object):
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

	def __init__(self, suit=0, rank=2):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

	def __cmp__(self, other):
		t1 = self.suit, self.rank
		t2 = other.suit, other.rank
		return cmp(t1, t2)


class Deck(object):
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def pop_card(self):
		return self.cards.pop()

	def add_card(self, card):
		self.cards.append(card)

	def shuffle(self):
		shuffle(self.cards)

	# check how it works
	def sort(self):
		sorted(self.cards)

	def move_card(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop_card())

	def deal_hands(self, players, cards):
		for player in range(players):
			hand_name = 'player' + str(player)
			hand = Hand(hand_name)
			for card in cards:
				hand.add_card(self.pop_card())


class Hand(Deck):
	def __init__(self, label=''):
		self.cards = []
		self.label = label


if __name__ == '__main__':
	print Deck
	my_deck = Deck()
	for i in range(100):
		my_deck.shuffle()

	my_deck.deal_hands(4, 7)