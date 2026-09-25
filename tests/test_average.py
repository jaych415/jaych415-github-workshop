from app.main import parse_and_average


def test_average_simple():
    assert parse_and_average("1, 2, 3") == "Average: 2.0000"

def test_average_rejects_non_numeric() -> None:
    assert (
        parse_and_average("1, hello, 3")
        == "Error: non-numeric value detected"
    )