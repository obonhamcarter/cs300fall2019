# date: 1 Sept 2019

# note, an easy way to get to the python3 shell is the following:
docker run -t python3

# start docker server
bash --login '/Applications/Docker/Docker Quickstart Terminal.app/Contents/Resources/Scripts/start.sh'


# Build the container
docker build -t py_play .



#Running commands basic nomenclature:
#docker run -it --mount type=bind,source={WHEREVER CODE SHOULD COME FROM},target={WHEREVER CODE SHOULD SHOW UP IN CONTAINER} {CONTAINER NAME} {COMMAND}


# mount a directory and then run file.
docker run -it --mount type=bind,source=$PWD,target=/home/py_play py_play python3 program_template.py

# change the program to run.
docker run -it --mount type=bind,source=$PWD,target=/home/py_play py_play python3 myprog.py

# mount a directory and then get to bash to do some python3 work.
docker run -it --mount type=bind,source=$PWD,target=/home/py_play py_play



# no drive mounting
docker run -it py_play
