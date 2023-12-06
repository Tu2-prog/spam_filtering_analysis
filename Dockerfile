FROM python:3.11.3


WORKDIR /code
COPY . /code
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ARG AUTH_TOKEN
ENV AUTH_TOKEN=${AUTH_TOKEN}

EXPOSE 8000

ENTRYPOINT ["python", "spam_filtering_backend/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
