from flask import Flask

from .app.configs import CONFIGS


def create_app(environment="development"):
    app = Flask(__name__)

    print(f"Applying configs for {environment.upper()} environment")
    app.config.from_object(CONFIGS[environment])
    from .app import api_bp as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api/")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
