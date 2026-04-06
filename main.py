from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI working perfectly!"}






import dagshub
dagshub.init(repo_owner='zulqarnainzahid999',
             repo_name='all_classes_of_data_science',
             mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

