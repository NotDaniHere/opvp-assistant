FROM python:3.9
RUN apt-get update
RUN apt-get install -y --no-install-recommends
WORKDIR /assistant
ADD main.py .
COPY requirements.txt .
COPY text.json .
RUN pip install -r requirements.txt
CMD python3 main.py