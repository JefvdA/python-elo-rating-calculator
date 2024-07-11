import pytest

from src.elo_rating_calculator.elo_rating_calculator import calculate_new_elo_ratings

test_data = [
    (1500, 1700, 1, 32, 400, 1524, 1676),
    (1800, 1500, 0.5, 42, 300, 1783, 1517),
]


@pytest.mark.parametrize("current_rating_a,current_rating_b,actual_outcome,k,c,expected_new_rating_a,"
                         "expected_new_rating_b", test_data)
def test_calculate_new_elo_ratings(
        current_rating_a: int,
        current_rating_b: int,
        actual_outcome: int,
        k: int,
        c: int,
        expected_new_rating_a: int,
        expected_new_rating_b: int,
) -> None:
    # When
    new_rating_a, new_rating_b = calculate_new_elo_ratings(
        rating_a=current_rating_a,
        rating_b=current_rating_b,
        actual_outcome=actual_outcome,
        k=k,
        c=c,
    )

    # Then
    assert expected_new_rating_a == new_rating_a
    assert expected_new_rating_b == new_rating_b
