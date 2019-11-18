# OBJECT DETECTION
Using Tensorflow 

### Installation


```sh
$ pip install -r requirements.txt 
$ run activate.bat 
$ protoc object_detection/protos/*.proto --python_out=.
"object_detection/protos/*.proto là đường dẫn tới các file .proto"
"nếu ta có cấu trúc thư mục là object-detection/object_detection/protos/*.proto thì sẽ làm như ví dụ"
$ python ../preprocessing.py
$ python ../main.py
```


[Link database](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md)

### Training 
```sh
$ python transform_image_resolution.py -h
$ python xml_to_scv.py -h 
$ python generate_tfrecord.py
...
Configuring training
- Model : faster_rcnn_inception_v2_pets
- Creating a label map (labelmap.pbtxt)
- Creating a training configuration
-- Line 9: change the number of classes to number of objects you want to detect (4 in my case)
-- Line 106: change fine_tune_checkpoint to the path of the model.ckpt file
--- eg : fine_tune_checkpoint: "C:/Users/Gilbert/Downloads/Other/models/research/object_detection/faster_rcnn_inception_v2_coco_2018_01_28/model.ckpt"
-- Line 123: change input_path to the path of the train.records file
-- Line 135: change input_path to the path of the test.records file
-- Line 125 and 137: change label_map_path to the path of the label map
--- eg : label_map_path: "C:/Users/Gilbert/Downloads/Other/models/research/object_detection/training/labelmap.pbtxt"
-- Line 130: change num_example to the number of images in your test folder

Training model 

$ python model_main.py --logtostderr --model_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config
$ tensorboard --logdir=training

Exporting inference graph
$ python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph
Testing object detector
- MODEL_NAME = 'inference_graph'
- PATH_TO_FROZEN_GRAPH = MODEL_NAME + '/frozen_inference_graph.pb'
- PATH_TO_LABELS = 'training/labelmap.pbtxt'

```
