FROM python:latest

RUN apt-get update
RUN apt-get install -y python3-tk tk-dev
RUN pip install matplotlib

WORKDIR /workdir

# COPY . .

# ENTRYPOINT ["python", "train_animate.py"]
