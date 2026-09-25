from app.main import parse_and_average


def test_average_simple():
    assert parse_and_average("1, 2, 3") == "Average: 2.0000"