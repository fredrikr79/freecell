from __future__ import annotations
from dataclasses import dataclass
from enum import auto, Enum
from string import digits


@dataclass
class Card:
    value: Value
    suit: Suit

    @staticmethod
    def from_string(s: str) -> Card:
        return Card(Value.from_string(s[:1]), Suit.from_string(s[-1:]))


@dataclass(frozen=True)
class Value:
    _value: int

    def __post_init__(self):
        if self._value not in range(1, 14):
            raise ValueError(
                "_CardValue must be in range 1-13, was " + str(self._value)
            )

    @staticmethod
    def from_string(s: str) -> Value:
        if s in digits[2:] or s == "10":
            return Value(int(s))
        value_mappings = {"A": 1, "J": 11, "Q": 12, "K": 13}
        if s in value_mappings:
            return Value(value_mappings[s])
        raise ValueError("_CardValue cannot be constructed from " + s)

    def get(self) -> int:
        return self._value


class Suit(Enum):
    HEARTS = auto()
    SPADES = auto()
    DIAMONDS = auto()
    CLUBS = auto()

    def is_black(self) -> bool:
        return self in [Suit.SPADES, Suit.CLUBS]

    def is_red(self) -> bool:
        return not self.is_black()

    @classmethod
    def from_string(s: str) -> Suit:
        suit_mappings = {
            "H": Suit.HEARTS,
            "S": Suit.SPADES,
            "D": Suit.DIAMONDS,
            "C": Suit.DIAMONDS,
        }
        if s not in suit_mappings:
            raise ValueError("Suit must be one of 'HSDC', was" + s)
        return suit_mappings[s]
