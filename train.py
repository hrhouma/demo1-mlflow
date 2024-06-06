import mlflow
import mlflow.sklearn

with mlflow.start_run():
    mlflow.log_param("param1", value1)
    mlflow.log_metric("metric1", value1)
    mlflow.sklearn.log_model(model, "model")
