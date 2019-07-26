# Copyright 2016 Google Inc.
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

import webapp2
import jinja2
import os

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# The handler section
class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = the_jinja_env.get_template('templates/login.html')
        self.response.write(login_template.render())  # the response

    def post(self):
        pass

class ProfilePage(webapp2.RequestHandler):
    def get(self):
        profile_template = the_jinja_env.get_template('templates/profile.html')
        self.response.write(profile_template.render())  # the response

    def post(self):
        pass

class ArtistsPage(webapp2.RequestHandler):
    def get(self):
        top_artists_template = the_jinja_env.get_template('templates/artists.html')
        self.response.write(top_artists_template.render())  # the response

    def post(self):
        pass

class TracksPage(webapp2.RequestHandler):
    def get(self):
        index_template = the_jinja_env.get_template('templates/tracks.html')
        self.response.write(index_template.render())  # the response

    def post(self):
        pass
    
class RecentsPage(webapp2.RequestHandler):
    def get(self):
        recents_template = the_jinja_env.get_template('templates/recent.html')
        self.response.write(recents_template.render())  # the response

    def post(self):
        pass

class PlaylistsPage(webapp2.RequestHandler):
    def get(self):
        playlists_template = the_jinja_env.get_template('templates/playlists.html')
        self.response.write(playlists_template.render())  # the response

    def post(self):
        pass

app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/profile', ProfilePage),
    ('/artists', ArtistsPage),
    ('/tracks', TracksPage),
    ('/recent', RecentsPage),
    ('/playlists', PlaylistsPage)
], debug=True)
