def create_routes(app,
                  health_controller,
                  resource_controller):
    app.add_url_rule('/api/healthcheck',view_func=health_controller.health_check, methods=['GET'])
    app.add_url_rule('/api/resource',view_func=resource_controller.read, methods=['GET'])
    app.add_url_rule('/api/resource',view_func=resource_controller.save, methods=['POST'])
