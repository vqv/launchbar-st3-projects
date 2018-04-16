#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import os.path
import json

path = '~/Library/Application Support/Sublime Text 3/Local/Session.sublime_session'

try:
  with open(os.path.expanduser(path)) as json_data:
    session = json.load(json_data)
  workspaces = session["workspaces"]["recent_workspaces"]
except:
  workspaces = []

items = [dict(title = os.path.splitext(os.path.basename(path))[0], 
              path = os.path.splitext(path)[0] + ".sublime-project",
              icon = "com.sublimetext.3") 
          for path in workspaces]

print json.dumps(items)