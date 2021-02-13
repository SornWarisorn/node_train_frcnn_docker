import os
import sys

os.system('sudo mv protobuf /frcnn_docker/tensorflow1/models/research')
os.system('sudo mv os_research.py /frcnn_docker/tensorflow1/models/research')
os.system('sudo mv .bashrc /home/vsa01')


os.chdir('/frcnn_docker/Train_node/training')
os.system('python3 mv.py')




