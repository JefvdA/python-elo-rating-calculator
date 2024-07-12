"""
This module provides methods for calculating elo ratings.
"""


from src.elo_rating_calculator.expected_outcome_calculator import calculate_expected_outcome


def calculate_new_elo_ratings(
        rating_a: int,
        rating_b: int,
        actual_outcome: int,
        k: int,
        c: int,
) -> tuple[int, int]:
    """
    This function calculates the new elo rating from the result of a match where both players are
    rated using the elo system. See calculation documented below. Rn = Ro + K * (S - E)

    Rn = new elo
    Ro = old elo
    K = factor for how big elo change should be -> start with 32
    S = actual outcome (WIN = 1, DRAW = 0.5, LOSS = 0)
    E = expected outcome (see `expected_outcome_calculator` for the information)
    """
    rating_diff_a = round(k * (actual_outcome - calculate_expected_outcome(rating_a, rating_b, c)))
    return rating_a + rating_diff_a, rating_b - rating_diff_a
