FROM python:3.8.6-buster

COPY /Users/magloirendabagera/Desktop/credentials/crypto-resolver-307909-787f6458f2bc.json
COPY api /api
COPY TaxiFareModelAdvanced /TaxiFareModelAdvanced
COPY model.joblib /model.joblib
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
