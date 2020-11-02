from my_flask_app.user.models import Funnel, Cost

def create_funnel(form_data):
    fe_options = form_data['feoptions']
    bump_options = form_data['bumpoptions']
    upsell_options = form_data['upselloptions']
    Funnel.create(funnel_name = '1', aov = 1, epc = 2)

    for num in range(1,int(fe_options)):
        Funnel.create(funnel_name = '1', aov = 1, epc = 2)

