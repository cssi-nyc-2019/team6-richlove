# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

# the handler section
class MainHandler(webapp2.RequestHandler):
  def get(self):  # for a get request
    self.response.write('Greeting')  # the response

class ChinaHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write( "China officially the People's Republic of China (PRC), is a country in East Asia \
      and the world's most populous country, with a population of around 1.404 billion.[10] \
      Covering approximately 9,600,000 square kilometers (3,700,000 sq mi), \
      it is the third- or fourth-largest country by total area.[k][16] Governed by the Communist Party of China, \
      the state exercises jurisdiction over 22 provinces, five autonomous regions, \
      four direct-controlled municipalities (Beijing, Tianjin, Shanghai, and Chongqing), and the special\
      administrative regions of Hong Kong and Macau.")    


# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/China', ChinaHandler)
  ], debug=True)
