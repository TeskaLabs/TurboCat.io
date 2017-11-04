import logging, asyncio, socket
import aiohttp.web

from ..config import Config

###

L = logging.getLogger(__name__)

###

class WebApplication(aiohttp.web.Application):


	def __init__(self, app):
		super().__init__(
			#middlewares=[IndexMiddleware(), context_middleware()],
			debug=Config['general']['verbose']
		)
		self.servers = []

		#TODO: Support of HTTPS
		self.ssl_context = None
		
		self.hosts = ['localhost'] #(Config.get('api:web', 'listen'),)
		self.port = 7443 # Config.getint('api:web', 'port')
		self.backlog = 10 # Config.getint('api:web','backlog')

		#self.access_log = AccessLogger()
		#self.access_log.addHandler(app._log_handler)


	def start(self, app):
		
		self.router.add_static('/web', './web', show_index=False)
		self.router.add_get('/', self.serve_webapp)

		self.handler = self.make_handler() #access_log=self.access_log)
		app.fix(self.startup())

		# Start servers
		server_creations = []

		scheme = 'https' if self.ssl_context else 'http'
		for host in self.hosts:
			app.fix(
				app.loop.create_server(
					self.handler, host, self.port, ssl=self.ssl_context, backlog=self.backlog
				)
			)


	async def serve_webapp(self, request):
		resp = aiohttp.web.StreamResponse(
			status=200, reason='OK', 
			headers={'Content-Type': 'text/html'}
		)

		await resp.prepare(request)

		resp.write("""<!DOCTYPE html>
<html lang="en" ng-app="TurboCatWebApp">
	<head>
		<title>TurboCat.io @ {0}</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
	</head>
	<body>
		<nav class="navbar navbar-expand-md navbar-dark bg-dark">
      		<a class="navbar-brand" href="#">TurboCat.io @ {0}</a>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbars" aria-controls="navbars" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>

			<div class="collapse navbar-collapse" id="navbars" ng-controller="NavBarsController">
			</div>
		</nav>

		<main role="main" class="container">
			<div><h1>Loading ...</h1></div>
		</main>

		<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
		<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.6/angular.min.js"></script>
		<script src="./web/app.js"></script>
	</body>
</html>""".format(socket.gethostname()).encode('utf-8'))

		return resp
