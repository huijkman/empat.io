#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.ext.webapp import template
import os

class MainHandler(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'site/index.html')
        template_values = {
        }
        self.response.out.write(template.render(path, template_values))

class MainNLHandler(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'site/index-nl.html')
        template_values = {
        }
        self.response.out.write(template.render(path, template_values))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'site/about.html')
        template_values = {
        }
        self.response.out.write(template.render(path, template_values))

class AboutNLHandler(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'site/over.html')
        template_values = {
        }
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/nl', MainNLHandler),
    ('/about', AboutHandler),
    ('/over', AboutNLHandler)
], debug=True)
