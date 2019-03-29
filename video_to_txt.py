#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by yaochao at 2019/3/28
# https://www.geeksforgeeks.org/extract-images-from-video-in-python/

import cv2
from PIL import Image
import numpy as np
import time
import sys
import os

abc = '@MWNHB8$06XFVYZ27>1jli!;:,. '
l = 256 / len(abc)


def remove_transparency(im, bg_colour=(255, 255, 255)):
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
        alpha = im.convert('RGBA').split()[-1]
        bg = Image.new("RGBA", im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg

    else:
        return im


def img2pixel(img, charwidth=100):
    img = img.convert("L")
    w, h = img.size
    img = img.resize((charwidth, int(charwidth * (h / w) / 2.4)))
    data = np.array(img)
    return data


def pixel2char(data):
    chars = '\n\n'
    for row in data:
        for pixel in row:
            a = abc[int(pixel / l)]
            chars += a
        chars += '\n'
    return chars + '\n'


def main(args):
    start = time.time()
    if len(args) != 3:
        print("Usage: video_to_txt videopath charwidth")
        return

    # 获取视频的宽高和帧率信息
    vcap = cv2.VideoCapture(args[1])
    width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
    height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    fps = vcap.get(cv2.CAP_PROP_FPS)
    print(width, height, fps)

    # 开始按帧循环
    currentframe = 0
    while (True):
        t1 = time.time()
        ret, frame = vcap.read()
        if ret:
            pilimg = Image.fromarray(frame)
            data = img2pixel(pilimg, charwidth=int(args[2]))
            s = pixel2char(data=data)
            print(s)
            currentframe += 1
        else:
            break

        # 睡眠时间为fps分之一秒减去此帧已经使用过的时间
        time2sleep = (1 / fps) - (time.time() - t1)
        if time2sleep > 0: time.sleep(time2sleep)

    # 释放空间和窗口
    vcap.release()
    cv2.destroyAllWindows()
    print("costed time:", time.time() - start)


if __name__ == '__main__':
    main(sys.argv)
