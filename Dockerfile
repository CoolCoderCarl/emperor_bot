FROM python:3.7.9

COPY ["bot.py", "/opt/"]
COPY requirements.txt requirements.txt

RUN  pip3.7 install -r requirements.txt

CMD python3.7 /opt/bot.py
