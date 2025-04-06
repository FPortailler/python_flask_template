from flask import Blueprint

api = Blueprint("api", __name__)


@api.route("/health", methods=["GET"])
def health_check():  # dead: disable
    """
    Health check endpoint.
    Returns a simple JSON response to indicate the service is running.
    """
    return {"status": "healthy"}, 200
