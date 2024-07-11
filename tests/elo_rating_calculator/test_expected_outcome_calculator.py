import pytest

from src.elo_rating_calculator.expected_outcome_calculator import calculate_expected_outcome

test_data = [
    (1500, 1700, 400, 0.24),
    (1500, 1500, 127291, 0.5),
    (1700, 1500, 400, 0.76),
    (800, 600, 300, 0.82),
]


@pytest.mark.parametrize("own_rating,other_rating,c,expected_expected_outcome", test_data)
def test_calculate_expected_outcome(own_rating: int, other_rating: int, c: int, expected_expected_outcome: float) -> None:
    # When
    expected_outcome = calculate_expected_outcome(
        own_rating=own_rating,
        other_rating=other_rating,
        c=c,
    )

    # Then
    assert expected_outcome == expected_expected_outcome
