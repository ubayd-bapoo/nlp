import sys
import click
import logging
import uvicorn

from fastapi import FastAPI

from service_app.routers import RouterRegister

# Configure the logging settings
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", handlers=[logging.StreamHandler(sys.stdout)])
# Create a logger
logger = logging.getLogger(__name__)

app = FastAPI(title='Deel technical test',
              description="A FastAPI application with custom Swagger documentation for Deel technical test.",
              version="1.0.0")


@app.on_event("startup")
def startup_events():
    RouterRegister.register(app)


@click.command()
@click.option("--port", default=8000, type=click.INT, help="Port to serve on.")
@click.option("--host", default="0.0.0.0", type=click.STRING, help="Host to serve on.")
def serve(port, host):
    logger.info('Starting BDE application')
    uvicorn.run(
        "service:app",
        host=host,
        port=port,
    )
