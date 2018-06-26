#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.kugou.com/song/#hash=F944C618AAA6EA347955EFBD5887BA25&album_id=1993047
# -> http://www.kugou.com/yy/index.php?r=play/getdata&hash=F944C618AAA6EA347955EFBD5887BA25&album_id=1993047&_=1529066174579
# -> http://fs.w.kugou.com/201806152031/000711211afc5320a0d08744b80dac0a/G115/M0B/17/13/U5QEAFnv-CeABfhaADyJUBfRogc820.mp3

from ykdl.util.match import match1
from ykdl.util.html import get_content
from ykdl.extractor import VideoExtractor
from ykdl.videoinfo import VideoInfo

import json

class Kugou(VideoExtractor):
    name = u'Kugou (酷狗音乐)'
    supported_stream_types = ['mp3']

    def prepare(self):
        info = VideoInfo(self.name)
        hash = match1(self.url, 'hash=(\w+)')
        album_id = match1(self.url, 'album_id=(\d+)')
        assert hash, album_id
        t = self.supported_stream_types[0]
        html = get_content("http://www.kugou.com/yy/index.php?r=play/getdata&hash={}&album_id={}&_=1529066174579".format(hash, album_id))
        data = json.loads(html)
        assert data['err_code'] == 0
        data = data['data']
        info.title = data['audio_name']
        info.artist = data['author_name']
        info.stream_types.append(t)
        info.streams[t] = {'container': t, 'video_profile': 'current', 'src' : [data['play_url']], 'size': 0}
        return info

site = Kugou()
