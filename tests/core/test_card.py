import pytest
from ...src.core import card


class TestCard:
    def test_card_instantiation(self):
        assert (
            cards := [
                card.Card(card.Value(value), suit)
                for suit in card.Suit
                for value in range(1, 14)
            ]
        ), "All card values 1-13 of all suits must be instantiable"

        assert [c.value.get() for c in cards] == (
            [v for _ in card.Suit for v in range(1, 14)]
        ), "All values must be set properly"

        value_strings: list[str] = (
            [c for c in "A23456789"] + ["10"] + [c for c in "JQK"]
        )

        assert [c.value.get() for c in cards] == [
            card.Value.from_string(s).get() for _ in card.Suit for s in value_strings
        ], "All values must be able to be generated from strings"

        suit_strings: list[str] = [s for s in "HSDC"]

        assert [
            card.Suit.from_string(s).name[0] for s in suit_strings
        ] == suit_strings, "All suits must be able to be generated from strings"

        assert [c.suit for c in cards] == [
            c.suit
            for c in [
                card.Card(card.Value.from_string(vs), card.Suit.from_string(ss))
                for ss in suit_strings
                for vs in value_strings
            ]
        ], "All suits must be able to be generated from strings to make cards"

        card_strings: list[str] = [
            vs + ss for ss in suit_strings for vs in value_strings
        ]

        assert cards == [
            card.Card.from_string(s) for s in card_strings
        ], "All cards must be able to be generated from strings"
