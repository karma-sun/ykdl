#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO
# https://www.wasu.cn/Play/show/id/9284090

from ykdl.util.match import match1
from ykdl.util.html import get_content
from ykdl.extractor import VideoExtractor
from ykdl.videoinfo import VideoInfo

import json
from bs4 import BeautifulSoup

def parse_html(html):
    return BeautifulSoup(html)

class Wasu(VideoExtractor):
    name = u'Wasu (华数)'
    supported_stream_types = ['mp4']

    def prepare(self):
        info = VideoInfo(self.name)
        t = self.supported_stream_types[0]
        info.title = ''
        info.artist = ''
        info.stream_types.append(t)
        info.streams[t] = {'container': t, 'video_profile': 'current', 'src' : [''], 'size': 0}
        return info

site = Wasu()
