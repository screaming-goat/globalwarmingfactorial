FROM python:slim
RUN apt-get update
RUN apt-get install -y git
RUN python3 -m pip install grpcio
RUN git clone https://github.com/screaming-goat/globalwarmingfactorial
WORKDIR globalwarmingfactorial/python
EXPOSE 36215
CMD python3 server.py
