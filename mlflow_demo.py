import mlflow
from prefect import flow, task

@task(name="mlflow-run", log_prints=True)
def mlflow_run():
  with mlflow.start_run():
    mlflow.log_metric("metric", 1.0)

@flow(name="mlflow-flow", log_prints=True)
def flow_hello():
    print("Hello, I'm a Flow!")
    print("I'm about to call a Task...")
    mlflow_run()

if __name__ == "__main__":
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("demo")

    flow_hello()
