"""This module provides functions to calculate the expected outcome of a match where both players
are rated using the elo system."""


def calculate_expected_outcome(own_rating: int, other_rating: int, c: int) -> float:
    """
    This function calculates the expected outcome of a match where both players are rated using
    the elo system. See calculation documented below. Keep in mind that this result will be
    rounded to 2 decimal points.

    E = 1 / ( 1 + 10^( (Rb - Ra) / c ) )

    Rb = the other player's elo
    Ra = your elo
    c = factor for differentiation between the elo's -> start with 400
    """
    return round(1 / (1 + 10 ** ((other_rating - own_rating) / c)), 2)
