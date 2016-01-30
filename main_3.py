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
    loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

# print out template_dir to see how the file path is being constructured. Logs in Google App Engine (GAE).
print "###############" 
print "template_dir:"
print template_dir
print ""
print "jinja_env:"
print pp.pprint(jinja_env)

# string substitution to render comment html
HTML_TEMPLATE = """
<div class=lessons-etc>
    <p>
        <img src="/images/comment_icon_final_bold.gif" 
            height=20px 
            align=center 
            style="padding-right:20px"> 
        <span style="color:#979797">   Write an anonymous response . . .</span> 
    </p>
    <form action="/sign?%s" method="post">
        <div>
            <textarea name="content" rows="3" cols="60"></textarea>
            <br>
        </div>
        <div>
            <input type="submit" value="publish">
            <br>
            <br>
            Responses
        </div>
        <div style="color: red">%(error)s</div>
    </form>
    <!-- user comments start here -->
    <div class=responses>
        %s
    </div>
</div>
"""



DEFAULT_WALL = 'Public'
def wall_key(wall_name=DEFAULT_WALL):
  """Constructs a Datastore key for a Wall entity.
  We use wall_name as the key.
  """
  return ndb.Key('Wall', wall_name)

class Post(ndb.Model):
    """A main model for representing an individual post entry."""
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        title = "Dan's Nano-degree Notes"
        template_vars = {'title': title}
        template = jinja_env.get_template('base.html')

        # main page
        self.response.out.write(template.render(template_vars))

        # comments section

        # def write_HTML_TEMPLATE(self, error=""):
        #     self.response.out.write(HTML_TEMPLATE % {"error": error})

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

        # Create our posts html
        posts_html = ''
        for post in posts:
            posts_html += '<blockquote class=ind_responses>' + cgi.escape(post.content) + '</blockquote>\n'

        global error
        error = ""
        error_param       = {'error': error}
        sign_query_params = urllib.urlencode({'wall_name': wall_name})
        # Render our page
        rendered_HTML = HTML_TEMPLATE % (sign_query_params, error_param, posts_html)

        # Write Out Page here

        self.response.out.write(rendered_HTML)
 




class PostWall(webapp2.RequestHandler):
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

        if len(post.content) == 0:
            error = "whoa"
        else:
            # Write to the Google Database
            post.put()

            # Do other things here such as a page redirect
            self.redirect('/?wall_name=' + wall_name)



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', PostWall)
], debug=True)








