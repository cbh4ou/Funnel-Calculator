from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    json
)
from flask_login import login_required, login_user, logout_user

from my_flask_app.extensions import login_manager
from my_flask_app.funnels.forms import FunnelForm
from my_flask_app.utils import flash_errors
from my_flask_app.funnels.view_commands import create_funnel
from my_flask_app.user.models import Funnel, Cost

blueprint = Blueprint("funnels", __name__, url_prefix="/funnel",static_folder="../static")

@blueprint.route("/create", methods=['POST'])
def funnel_creator():
    """List members."""
    f = request.form
    data = {}
    for key in f.keys():
        for value in f.getlist(key):
            data[key] = value
    print(data)
    create_funnel(data)

    if request.method == 'POST':
        # replace this with an insert into whatever database you're using
        return ('success', 200)

@blueprint.route("/editor")
def show_form():
    """About page."""
    form = FunnelForm(request.form)
    return render_template("public/funnelform.html", form = form)

