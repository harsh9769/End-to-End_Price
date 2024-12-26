import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model._base import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from src.house_reg.config.configuration import PrepareTrainModelConfig


class PrepareTrainModel:

    def __init__(self,config=PrepareTrainModelConfig):

        self.config=config

    def data_set(self):

        data = pd.read_csv("artifacts\data_ingestion\Housing.csv")

        categorical_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus']
        label_encoders = {}
        for col in categorical_columns:
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col])
            label_encoders[col] = le
        self.X=data.drop(columns=["price"])
        self.y=data["price"]

    def train_model(self):
    
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        # Train the model
        reg = LinearRegression().fit(X_train, y_train)
        # Evaluate the model
        #print("Training R^2 Score:", reg.score(X_train, y_train))
        #print("Testing R^2 Score:", reg.score(X_test, y_test))
        with open(str(self.config.base_model_path),'wb') as f:
            pickle.dump(reg,f)

