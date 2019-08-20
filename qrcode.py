#!/usr/bin/env python
import os
from MyQR import myqr

version, level, qr_name = myqr.run(
    'https://www.baidu.com',
    version=1,
    level='H',
    picture='timg.gif',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='timg_qrcode2.0.gif',
    save_dir=os.getcwd()
)
