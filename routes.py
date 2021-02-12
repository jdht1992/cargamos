from views import HelloWorld

def routes(api):
   api.add_resource(HelloWorld, '/')
