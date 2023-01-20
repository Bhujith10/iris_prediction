FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim
EXPOSE $PORT
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./main.py /code/main.py
COPY ./random_forest_classifier.joblib /code/random_forest_classifier.joblib
RUN pip install --no-cache-dir --upgrade -r requirements.txt
ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]
