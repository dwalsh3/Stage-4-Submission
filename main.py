# DAN'S NOTES WEBPAGE
# this is python script, along with app.yaml (app id: yellowstripes-1149) builds the notes page on google app engine 

#!/usr/bin/env python

import os
import jinja2
import webapp2
import cgi
import urllib
from google.appengine.ext import ndb
import pprint # debugging
pp = pprint.PrettyPrinter(indent=4)

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape = True, extensions=['jinja2.ext.autoescape'])


DEFAULT_WALL = 'Public'
def wall_key(wall_name=DEFAULT_WALL):
    """Constructs a Datastore key for a Wall entity.
    We use wall_name as the key."""
    return ndb.Key('Wall', wall_name)

class Post(ndb.Model):
    """A main model for representing an individual post entry."""
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


#via one behind this page https://www.udacity.com/course/viewer#!/c-cs253/l-676928821/e-668139084/m-647920898
class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params) # autoescape=False doesn't work here

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):

        title = "Dan's Nano-degree Notes"
        template_vars = {'title': title}
        template = jinja_env.get_template('base.html')

        # main page
        self.response.out.write(template.render(template_vars))

        # comments section
        wall_name = self.request.get('wall_name',DEFAULT_WALL)

        # Ancestor Queries, as shown here, are strongly consistent
        # with the High Replication Datastore. Queries that span
        # entity groups are eventually consistent. If we omitted the
        # ancestor from this query there would be a slight chance that
        # Greeting that had just been written would not show up in a
        # query.

        # [START query]
        posts_query = Post.query(ancestor = wall_key(wall_name)).order(-Post.date)

        # The function fetch() returns all posts that satisfy our query. The function returns a list of
        # post objects
        posts =  posts_query.fetch()
        # [END query]

        # Write Out Page here
        self.render('/comments.html',
            posts = posts,
            wall  = urllib.urlencode({'wall_name': wall_name}), 
            error = PostWall.error)
        PostWall.error = ''
 


class PostWall(Handler):
    error = '' #class variable
    def post(self):
        # We set the same parent key on the 'Post' to ensure each
        # Post is in the same entity group. Queries across the
        # single entity group will be consistent. However, the write
        # rate to a single entity group should be limited to
        # ~1/second.
        wall_name = self.request.get('wall_name',DEFAULT_WALL)
        post = Post(parent=wall_key(wall_name))

        # Get the content from our request parameters, in this case, the message
        # is in the parameter 'content'
        post.content = self.request.get('content')

        # Do other things here such as a page redirect
        if not(post.content): #empty is bad
            PostWall.error = "that wasn't much of a response."
        else:
            # Write to the Google Database
            post.put()

        self.redirect('/#comments')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', PostWall)
], debug=True)








