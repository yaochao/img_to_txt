# Image transfer to txt

### Usage
* install dependence：

```shell
$ pip3 install -r requirements.txt
````

* command：

```shell
$ python3 img_to_txt.py [file/url] [size]
```

* args:

```shell
[file/url]: The local file path, or online pic URL.
[size]: Width of output txt, The larger the size, the clearer the picture .
```

### Example
```shell
$ python3 img_to_txt.py https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
```
This command executed, you will get a file in current folder named `out.txt`, and you will watch a string output in the console:

![google](https://github.com/yaochao/img_to_txt/blob/master/google.png?raw=true)

![google-txt](https://github.com/yaochao/img_to_txt/blob/master/google-txt.png?raw=true)

### Lience
MIT lience
