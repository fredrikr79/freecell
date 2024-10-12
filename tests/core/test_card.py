import pytest
from ...src.core import card


class TestCard:
    def test_card_instantiation(self):
        assert (
            cards := [
                card.Card(card.Value(value), suit)
                for value in range(1, 14)
                for suit in card.Suit
            ]
        ), "All card values 1-13 of all suits must be instantiable"

        assert [c.value.get() for c in cards] == (
            list(range(1, 14)) * len(card.Suit)
        ), "All values must be set properly"

        value_strings: list[str] = (
            [c for c in "A23456789"] + ["10"] + [c for c in "JQK"]
        )

        assert [c.value.get() for c in cards] == [
            card.Value.from_string(s) for s in value_strings for _ in card.Suit
        ], "All values must be able to be generated from strings"

        suit_strings: list[str] = [c for c in "HSDC"]

        assert [c.suit for c in sorted(cards, key=lambda c: c.suit.name)] == [
            c.suit
            for c in sorted(
                [
                    card.Card(card.Value.from_string(vs), card.Suit.from_string(ss))
                    for vs in value_strings
                    for ss in suit_strings
                ],
                key=lambda c: c.suit.name,
            )
        ], "All suits must be able to be generated from strings"

        card_strings: list[str] = [
            vs + ss for vs in value_strings for ss in suit_strings
        ]

        assert cards == [
            card.Card.from_string(s) for s in card_strings
        ], "All cards must be able to be generated from strings"
