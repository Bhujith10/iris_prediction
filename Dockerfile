FROM python:3.9-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./main.py /code/main.py
COPY ./random_forest_classifier.joblib /code/random_forest_classifier.joblib
RUN pip install --upgrade -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]