#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.kwting.com/play/14144-0-0.html
# Kwting include mp3 info of all chapters in any single chapter page
# should always use --no-merge command-line switch

from ykdl.util.match import match1
from ykdl.util.html import get_content, parse_html
from ykdl.extractor import VideoExtractor
from ykdl.videoinfo import VideoInfo

import json
import urllib.parse

class Kwting(VideoExtractor):
    name = u'Kwting (酷我听书)'
    supported_stream_types = ['mp3']

    def prepare(self):
        info = VideoInfo(self.name)
        html = get_content(self.url)
        meta = parse_html(html)
        vilist_str = match1(html, 'VideoInfoList=unescape\("(.+)"\)')
        assert vilist_str
        infoList = urllib.parse.unquote(vilist_str)[11:].split('#')
        if '' in infoList: infoList.remove('')
        t = self.supported_stream_types[0]
        info.title = meta.find('title').text
        info.artist = ''
        info.stream_types.append(t)
        info.streams[t] = {'container': t, 'video_profile': 'current', 'src' : [item.split('$')[1] for item in infoList], 'size': 0}
        return info

site = Kwting()
