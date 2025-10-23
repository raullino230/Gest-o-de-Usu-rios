def configure_all(app):
    pass


def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route)


def configure_db(app):
    pass