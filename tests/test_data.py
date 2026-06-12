import pandas as pd

from src.data import load_diamonds, train_test_split_diamonds


def test_load_diamonds():

    df = load_diamonds()

    assert isinstance(df, pd.DataFrame)

    assert not df.empty


def test_train_test_split():

    X_train, X_test, y_train, y_test = train_test_split_diamonds()

    assert len(X_train) > 0
    assert len(X_test) > 0
    assert len(y_train) > 0
    assert len(y_test) > 0
