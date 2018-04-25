# Image transfer to txt

### Usage
* install dependence：

```shell
$ pip3 install -r requests.txt
````

* command：

```shell
$ python3 img_to_txt.py [file/url] [size]
```

* args:

[file/url]: 本地图片路径，或者网络图片URL。The local file path, or online pic URL.
[size]: 输出文本的宽度，size越大，输出文本越清晰。 Width of output txt, The larger the size, the clearer the picture .

### Example
```shell
$ python3 img_to_txt.py http://ocas9civ7.bkt.clouddn.com/jzm.jpg
```
This command executed, you will get a file in current folder named `out.txt`, and you will watch a string output in the console:

![zz](http://ocas9civ7.bkt.clouddn.com/zz.png)

### Lience
MIT lience
