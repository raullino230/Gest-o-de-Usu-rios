def configure_all():
    pass


def configure_routes():
    app.register_blueprint(home_route)
app.register_blueprint(cliente_route)


def configure_db():
    pass