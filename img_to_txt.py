#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/4/24


from PIL import Image
import numpy as np
import requests
import sys

OUT_IMG = 'out.txt'

abc = '##@@MMBB88NNHHOOGGPPEEXXFFVVYY22ZZCC77LLjjll11rrii;;;:::....  '
l = 256 / len(abc)


def remove_transparency(im, bg_colour=(255, 255, 255)):
    # Only process if image has transparency (http://stackoverflow.com/a/1963146)
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):

        # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
        alpha = im.convert('RGBA').split()[-1]

        # Create a new background image of our matt color.
        # Must be RGBA because paste requires both images have the same format
        # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
        bg = Image.new("RGBA", im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg

    else:
        return im


def pixel_to_black(fp, weight):
    try:
        img = Image.open(fp)
    except:
        print('请输入正确的图片路径或URL😝')
        return
    img = remove_transparency(img)
    img = img.convert("L")
    im_w, im_h = img.size
    img = np.array(img)
    h, w = img.shape
    # 如果weight超过像素
    weight_w = weight if w >= weight else w
    weight_h = weight if h >= weight else h
    weight = weight_w if weight_w < weight_h else weight_h
    # 最大字宽
    t_w = weight
    # 最大字高
    t_h = weight / (im_w / im_h) / 2
    width_times = int(w / t_w) if int(w / t_w) != 0 else 1
    high_times = int(h / t_h) if int(h / t_h) != 0 else 1

    tmp_high = []
    for high_index in range(int(h / high_times)):
        tmp_width = []
        for width_index in range(int(w / width_times)):
            tmp_block = []
            for y in range((high_index * high_times), ((high_index + 1) * high_times)):
                for x in range(width_index * width_times, (width_index + 1) * width_times):
                    tmp_block.append(img[y, x])
            avg_tmp_block = sum(tmp_block) / len(tmp_block)
            tmp_width.append(avg_tmp_block)
        tmp_high.append(tmp_width)
    return tmp_high


def black_to_alphabet(rgb_list):
    tmp_high = ''
    for i in rgb_list:
        tmp_width = ''
        for ii in i:
            a = abc[int(ii / l)]
            tmp_width += a
        tmp_width += '\n'
        tmp_high += tmp_width
    return tmp_high


def paint(uri, weight):
    if uri.startswith('http'):
        img = get_img(uri)
    else:
        img = uri
    rgb_list = pixel_to_black(img, weight)
    if not rgb_list:
        return
    s = black_to_alphabet(rgb_list)
    with open(OUT_IMG, 'w', encoding='utf-8') as f:
        f.write(s)
    return s


def get_img(url):
    print('️正在加载图片☺️\n')
    response = requests.get(url)
    if response.status_code == 200:
        with open('in.png', 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
            return 'in.png'


def main(args):
    try:
        uri = args[1]
        assert type(uri) == str
    except:
        uri = 'https://www.v2ex.com/static/img/v2ex@2x.png'
    try:
        weight = int(args[2])
        assert type(weight) == int
    except:
        weight = 80
    s = paint(uri, weight=weight)
    if not s:
        return
    print(s)


if __name__ == '__main__':
    main(sys.argv)
