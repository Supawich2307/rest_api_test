FROM python:3.9.6
COPY .  /app
WORKDIR /app
RUN pip3 install flask
RUN pip3 install waitress
RUN pip3 install requests
EXPOSE  5200
CMD ["python3", "src/server.py"]
