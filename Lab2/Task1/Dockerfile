FROM python

WORKDIR /lab2

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python","main.py"]