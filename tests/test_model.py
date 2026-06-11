from sklearn.pipeline import Pipeline

from src.data import load_diamonds, split_features_target

from src.model import train_model


def test_pipeline_training():

    df = load_diamonds().sample(500, random_state=42)

    X, y = split_features_target(df)

    model = train_model(X, y, max_depth=3)

    assert isinstance(model, Pipeline)
