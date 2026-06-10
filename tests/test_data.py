from src.data import train_test_split_diamonds


def test_train_test_split():

    X_train, X_test, y_train, y_test = (
        train_test_split_diamonds()
    )

    assert len(X_train) > 0
    assert len(X_test) > 0
    assert len(y_train) > 0
    assert len(y_test) > 0