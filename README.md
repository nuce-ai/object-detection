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
