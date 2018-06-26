#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://y.qq.com/n/yqq/song/002zSeUQ0fvPVO.html
# -> https://c.y.qq.com/v8/fcg-bin/fcg_play_single_song.fcg?songmid=002zSeUQ0fvPVO&tpl=yqq_song_detail&format=json&g_tk=5381&loginUin=0&hostUin=0&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0
# support album
# https://y.qq.com/n/yqq/album/004AbEDb21klJr.html

from ykdl.util.match import match1
from ykdl.util.html import get_content, parse_html
from ykdl.extractor import VideoExtractor
from ykdl.videoinfo import VideoInfo

import json

class QQmusic(VideoExtractor):
    name = u'QQmusic (QQ音乐)'

    def prepare(self):
        info = VideoInfo(self.name)
        mid = match1(self.url, 'song/(\w+).html')
        html = get_content("https://c.y.qq.com/v8/fcg-bin/fcg_play_single_song.fcg?songmid={}&tpl=yqq_song_detail&format=json&g_tk=5381&loginUin=0&hostUin=0&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0".format(mid))
        data = json.loads(html)
        assert data['code'] == 0
        data = data['data']
        info.title = data[0]["title"]
        info.artist = data[0]["singer"][0]["title"]
        t = 'wma'
        info.stream_types.append(t)
        info.streams[t] = {'container': t, 'video_profile': 'current', 'src' : [data[0]["url"]], 'size': 0}
        return info

    def prepare_list(self):
        meta = parse_html(get_content(self.url))
        return ['https:' + tag.a['href'] for tag in meta.find('div', class_='mod_songlist').find_all('span', class_='songlist__songname_txt')]

site = QQmusic()
