from flask_swagger_ui import get_swaggerui_blueprint

blueprint = get_swaggerui_blueprint(
    '/api/v1/swagger',
    '/static/openapi.yml',
    config = {
        'app_name': "Timezone API"
    }
)