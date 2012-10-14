#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import with_statement, division, absolute_import

import urllib

import sublime
import sublime_plugin


class HttpFoobar(sublime_plugin.WindowCommand):
    def run(self, cmd):
        settings = sublime.load_settings('HTTPFoobar.sublime-settings')
        base_url = settings.get("base_url", "http://127.0.0.1:8888/default")
        params = urllib.urlencode({"cmd": cmd})
        url = base_url + "?" + params
        try:
            urllib.urlopen(url)
        except Exception, e:
            sublime.status_message(str(e))
