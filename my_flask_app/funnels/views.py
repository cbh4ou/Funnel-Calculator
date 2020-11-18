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
from my_flask_app.funnels.view_commands import get_funnel_data, create_funnel, get_funnel_stats
from my_flask_app.user.models import Funnel, Cost
from my_flask_app.funnels.funnel_table import get_funnel_table, get_csv

blueprint = Blueprint("funnels", __name__, url_prefix="/funnel",static_folder="../static")

@blueprint.route("/create", methods=['POST','GET'])
@login_required
def funnel_creator():

    if request.method == 'POST':
        f = request.form
        data = {}
        for key in f.keys():
            for value in f.getlist(key):
                data[key] = value
        print(data)
        create_funnel(data)
        return ('success', 200)
    else:
        form = FunnelForm(request.form)

        return render_template("public/funnelform.html", form = form)

#Serves Edit Form and also sends data to Frontend to fill out form on load
@blueprint.route("/editor/<id>", methods=['POST','GET'])
@login_required
def edit_funnel(id):
    """About page."""
    if request.method == 'POST':
        d = get_funnel_data(id)
        return d
    else:
        form = FunnelForm(request.form)
        return render_template("public/editForm.html", form = form)

# Post Function for the Funnel Editor Form View : Updates Existing Funnel
@blueprint.route("/update/<id>", methods=['POST'])
def update_funnel(id):
    """About page."""
    if request.method == 'POST':
        d = get_funnel_data(id)
        return d
    

@blueprint.route("/stats/<id>", methods=['GET'])
def funnel_data(id):
    """ Retrieve Funnel Data"""
    json_rslt = get_funnel_stats(id)
    return render_template("public/funnelStats.html", data = json_rslt)

@blueprint.route("/stats/recalc/<id>", methods=['GET'])
def recalc_stats(id):
    """ Retrieve Funnel Data"""
    json_rslt = get_funnel_stats(id)
    return (json_rslt, 200)

@blueprint.route("/stats/table", methods=['GET'])
def build_table():
    """ Retrieve Funnel Data"""
    json_rslt = get_funnel_table()
    return (json_rslt, 200)
@blueprint.route("/stats/export/<funnel_id>", methods=['GET'])
def export_csv(funnel_id):
    """ Retrieve Funnel Data"""
    return (get_csv(funnel_id), 200)