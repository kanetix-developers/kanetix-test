FROM frolvlad/alpine-python3

WORKDIR /app

RUN pip install flask requests xmltodict

EXPOSE 8000