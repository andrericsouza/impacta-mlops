import argparse
import mlflow
import mlflow.sklearn

from src.data import train_test_split_diamonds

from src.model import train_model

from src.evaluate import regression_metrics


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument("--test_size", type=float, default=0.2)

    parser.add_argument("--random_state", type=int, default=42)

    parser.add_argument("--max_depth", type=int, default=5)

    return parser.parse_args()


def main():

    args = parse_args()

    mlflow.set_tracking_uri("http://localhost:5000")

    mlflow.set_experiment("diamond_price_experiment")

    X_train, X_test, y_train, y_test = train_test_split_diamonds(
        test_size=args.test_size,
        random_state=args.random_state,
    )

    with mlflow.start_run():

        mlflow.log_param("test_size", args.test_size)

        mlflow.log_param("random_state", args.random_state)

        model = train_model(X_train, y_train, max_depth=args.max_depth)

        predictions = model.predict(X_test)

        metrics = regression_metrics(y_test, predictions)

        mlflow.sklearn.log_model(sk_model=model, artifact_path="model")

        for metric_name, metric_value in metrics.items():

            mlflow.log_metric(metric_name, metric_value)

        mlflow.log_param("max_depth", args.max_depth)

        print("\nTreino concluído.")

        print(f"MAE: {metrics['mae']:.2f}")

        print(f"RMSE: {metrics['rmse']:.2f}")

        print(f"R2: {metrics['r2']:.4f}")


if __name__ == "__main__":
    main()
