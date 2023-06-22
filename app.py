from settings import app

from routes.auth.login import auth_login_blueprint
from routes.auth.create import auth_create_blueprint
from routes.applications.apply import applications_apply_blueprint
from routes.applications.get import applications_get_blueprint
from routes.applications.edit import applications_edit_blueprint
from routes.applications.delete import applications_delete_blueprint
from routes.inputs.get import inputs_get_blueprint
from routes.inputs.add import inputs_add_blueprint
from routes.inputs.update import inputs_update_blueprint
from routes.inputs.delete import inputs_delete_blueprint

app.register_blueprint(auth_login_blueprint)
app.register_blueprint(auth_create_blueprint)
app.register_blueprint(applications_apply_blueprint)
app.register_blueprint(applications_get_blueprint)
app.register_blueprint(applications_edit_blueprint)
app.register_blueprint(applications_delete_blueprint)
app.register_blueprint(inputs_get_blueprint)
app.register_blueprint(inputs_add_blueprint)
app.register_blueprint(inputs_update_blueprint)
app.register_blueprint(inputs_delete_blueprint)

if __name__ == "__main__":
    app.run()