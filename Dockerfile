FROM python:3.10-slim
LABEL authors="Krzysztof Olech"


RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    libxrender-dev libx11-6 libxext-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev  && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 libxcb-xinerama0  -y

RUN apt-get remove qtchooser  -y
RUN apt-get install libqt5gui5 -y

RUN apt-get install libxcb-cursor0 -y

RUN pip install PyQt5
RUN pip install numpy
RUN pip install opencv-contrib-python-headless
RUN pip install setuptools
RUN pip install PyGetWindow
RUN pip install matplotlib
RUN pip install scipy
RUN pip install scikit-image



# Set up application workspace
COPY src /app/src
WORKDIR /app/src
ENV PYTHONPATH=/app/src

COPY Config Config

ENV QT_DEBUG_PLUGINS=1

# Run the PyQt5 application
CMD ["python", "Python/StartUP/main.py"]
