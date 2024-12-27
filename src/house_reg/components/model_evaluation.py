import pickle
from pathlib import Path
import mlflow
import dagshub
from urllib.parse import urlparse
import json
from house_reg.config.configuration import EvaluationConfig


class Evaluation:
    def __init__(self, config:EvaluationConfig):
        self.config = config

    @staticmethod
    def load_model(path):
        """Load a model from the given path."""
        with open(str(path), 'rb') as f:
            model = pickle.load(f)
        return model

    @staticmethod
    def load_data():
        """Load X_test and y_test from pre-saved files."""
        with open('artifacts/prepare_base_model/X_test.pkl', 'rb') as f:
            X_test = pickle.load(f)
        with open('artifacts/prepare_base_model/y_test.pkl', 'rb') as f:
            y_test = pickle.load(f)
        return X_test, y_test

    def evaluation(self):
        """Evaluate the model on the test data and save the score."""
        self.model = self.load_model(r"artifacts\prepare_base_model\model.pkl")

        X_test, y_test = self.load_data()
        self.score = self.model.score(X_test, y_test)
        self.save_score()

    def save_score(self):
        """Save the evaluation score to a JSON file."""
        scores = {"score": self.score}
        with open("scores.json", "w") as f:
            json.dump(scores, f)

    def log_into_mlflow(self):
        """Log parameters, metrics, and the model into MLflow, using DagsHub integration."""
        # Initialize DagsHub integration
        dagshub.init(
            repo_owner='harsh9769',
            repo_name='End-to-End_Price',
            mlflow=True
        )

        with mlflow.start_run():
            mlflow.log_param('model_path', str(self.config.path_of_model))
            mlflow.log_metric('score', self.score)

