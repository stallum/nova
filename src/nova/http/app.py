from robyn import Robyn

from nova.http.routes.healthy import register_health_routes

app = Robyn(__file__)

register_health_routes(app)
