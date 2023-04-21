FROM python:latest
RUN mkdir /app
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


COPY . ./

CMD ["python","main.py"]
