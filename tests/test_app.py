from app import load_data


def test_load_data_has_rows() -> None:
    df = load_data()
    assert len(df) > 0
    assert set(["service", "status", "requests"]).issubset(df.columns)
