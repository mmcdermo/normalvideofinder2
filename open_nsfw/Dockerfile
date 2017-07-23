FROM caffe:cpu
COPY requirements.txt ./
RUN pip install -r ./requirements.txt
EXPOSE 5000
ENV FLASK_APP ./server.py