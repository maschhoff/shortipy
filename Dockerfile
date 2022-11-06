# syntax=docker/dockerfile:1
FROM python
RUN python -V
WORKDIR /source
ENV FLASK_APP=shorti.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=4321
COPY /shortipy /source
RUN apt-get update && apt-get install build-essential python3-dev -y
RUN pip3 install -r /source/requirements.txt
CMD ["flask", "run"]
