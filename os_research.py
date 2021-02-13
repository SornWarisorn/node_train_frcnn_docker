import os
import sys

os.chdir('/frcnn_docker/tensorflow1/models/research/object_detection/training/script')
os.system('python3 edit.py')

os.chdir('/frcnn_docker/tensorflow1/models/research')
os.system('alias python=python3')
os.system('./protobuf/bin/protoc object_detection/protos/*.proto --python_out=.')
#os.system('export PYTHONPATH=$PYTHONPATH:/home/vsa01/Desktop/tensorflow1/models/research:/home/vsa01/Desktop/tensorflow1/models/research/slim')
#os.environ['echo %PYTHONPATH%']
sys.path.append('/frcnn_docker/tensorflow1/models/research:/frcnn_docker/tensorflow1/models/research/slim')
sys.path.extend(["/frcnn_docker/tensorflow1/models/research:/frcnn_docker/tensorflow1/models/research/slim"])
os.system('python3 setup.py build')
os.system('sudo python3 setup.py install')
os.system('python3 object_detection/builders/model_builder_test.py')

os.chdir('/frcnn_docker/tensorflow1/models/research/object_detection')

os.system('python3 xml_to_csv.py')
os.system('python3 generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=images/train.record')
os.system('python3 generate_tfrecord.py --csv_input=images/test_labels.csv --image_dir=images/test --output_path=images/test.record')
os.system('python3 train.py --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config –checkpoint_dir=training/')
