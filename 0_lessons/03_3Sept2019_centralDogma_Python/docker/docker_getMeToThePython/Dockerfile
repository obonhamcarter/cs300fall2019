FROM ubuntu

RUN apt-get update

RUN \
  apt-get install -y python3

#RUN \
#  apt-get install -y

RUN useradd py_play
RUN mkdir /home/py_play
RUN export HOME=/home/py_play

WORKDIR /home/py_play

# Define default command.
CMD ["bash"]
