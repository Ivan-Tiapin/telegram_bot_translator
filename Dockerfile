FROM python:3.9-bullseye
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY *.py /app/
COPY *.json /app/
EXPOSE 443
CMD ["python", "bot.py"]
