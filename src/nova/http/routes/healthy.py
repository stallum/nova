from robyn import Robyn

def register_health_routes(app: Robyn) -> None:

    @app.get("/health")
    async def health(request):
        return {
            "status": "healthy",
            "application": "NOVA",
            "version": "0.1.0",
        }
