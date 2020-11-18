from my_flask_app.user.models import Funnel, Cost
import json
import sys
from sqlalchemy import inspect

def update_funnel(funnel_id):
    pass
def create_funnel(form_data):
    fe_options = int(form_data['feoptions'])
    bump_options = int(form_data['bumpoptions'])
    upsell_options = int(form_data['upselloptions'])

    Funnel.create(funnel_name = form_data['funnelname'],
                traffic = 1000, 
                advertising_cost = int(form_data['cpa_cost']),
                shipping_cost = int(form_data['encore_cost']),
                callcenter_cost = int(form_data['call_cost']),
                fe_percent = form_data['fe_tr'],
                        )

    funnel = Funnel.query.filter_by(funnel_name=form_data['funnelname']).first()

    print(funnel.funnel_name)
    for prod_num in range(1,fe_options+1):
        prod_name = f"prod{prod_num}"
        prod_price = f"prod_price{prod_num}"
        prod_cost = f"prod_cost{prod_num}"
        prod_tr = f"prod_tr{prod_num}"
 
        Cost.create(
        product_name=form_data[prod_name],
        cost = form_data[prod_cost], 
        price = form_data[prod_price],
        shipping= form_data[prod_price],
        take_rate = form_data[prod_tr],
        product_type = 'FE',
        funnel_id= funnel.id
        )

    for prod_num in range(1,bump_options+1):
        prod_name = f"order_bump{prod_num}"
        prod_price = f"ob_price{prod_num}"
        prod_cost = f"ob_cost{prod_num}"
        prod_tr = f"ob_tr{prod_num}"
 
        Cost.create(
        product_name=form_data[prod_name],
        cost = form_data[prod_cost], 
        price = form_data[prod_price],
        shipping= form_data[prod_price],
        take_rate = form_data[prod_tr],
        product_type = 'OB',
        funnel_id= funnel.id
        )
    for prod_num in range(1,upsell_options+1):
        prod_name = f"up_name{prod_num}"
        prod_tr = f"up_tr{prod_num}"
        up_cost_average = f"up_cost_avg{prod_num}"
        total_orders = f"total_orders{prod_num}"
        products_offered = f"total_orders{prod_num}"
        total_revenue = f"total_revenue{prod_num}"
 

        Cost.create(product_name=form_data[prod_name],
        price = float(form_data[total_revenue])/int(form_data[total_orders]),
        shipping= form_data[prod_price],
        take_rate = form_data[prod_tr],
        product_type = 'US',
        incoming_traffic = form_data['upsell_traffic1'],
        total_orders = form_data[total_orders],
        products_offered = form_data[products_offered],
        up_cost_avg = form_data['up_cost_avg1'],
        cost = form_data[up_cost_average], 
        total_revenue = form_data[total_revenue],
        funnel_id= funnel.id
        )
    get_funnel_stats(int(funnel.id))

def get_funnel_stats(funnel_id):
    steps = Cost.query.filter_by(funnel_id=funnel_id).all()
    funnel = Funnel.query.filter_by(id=funnel_id).first()

    # Calculate Front End Bump Metrics

    front_end = FE_metrics()
    front_end.orders = (funnel.fe_percent/100 * 1000) 
    for step in steps:
        if step.product_type == 'FE':
            front_end.revenue += ((float(front_end.orders) * step.take_rate/100) * step.price)
            front_end.cost += ((float(front_end.orders) * step.take_rate/100) * step.cost) 
    front_end.cost += (float((funnel.fe_percent/100 * 1000))  * (funnel.shipping_cost+ funnel.callcenter_cost + funnel.advertising_cost))
    front_end.calc_profit()  

    # Calculate Order Bump Metrics
    bumps = OB_metrics()
    for step in steps:
        if step.product_type == 'OB':
            fe_orders = (funnel.fe_percent/100 * 1000) 
            bumps.revenue += ((float(fe_orders) * step.take_rate/100) * step.price)
            bumps.cost = ((float(fe_orders) * step.take_rate/100) * step.cost)  
    bumps.calc_profit()

     # Calculate Upsell Metrics
    ups_list =[]
    for step in steps:
        ups = US_metrics()
        if step.product_type == 'US':
            ups.orders = step.total_orders
            ups.revenue += (ups.orders * step.price)
            ups.cost = ((float(fe_orders) * step.take_rate/100) * step.cost)
            ups_list.append(ups)

    funnel_obj = Funnel_metrics()
    funnel_obj.traffic = 1000
    funnel_obj.name=funnel.funnel_name
    ups = US_metrics()
    for upsell in ups_list:
        funnel_obj.cost += upsell.cost
        funnel_obj.revenue += upsell.revenue
        funnel_obj.orders += upsell.orders
        upsell.calc_profit()
        ups.profit += upsell.profit
        funnel_obj.profit += upsell.profit
        funnel_obj.orders += upsell.orders

    # KPI Calculations
    funnel_obj.cost += front_end.cost + bumps.cost 
    funnel_obj.revenue += front_end.revenue + bumps.revenue 
    funnel_obj.profit += front_end.profit + bumps.profit 
    funnel_obj.orders += front_end.orders 
    funnel_obj.aov = funnel_obj.revenue/funnel_obj.orders
    funnel_obj.net_aov = funnel_obj.profit/funnel_obj.orders
    funnel_obj.epc = funnel_obj.revenue/funnel_obj.traffic
    funnel_obj.net_epc = funnel_obj.profit/funnel_obj.traffic
    funnel_obj.frontend_percent = (front_end.profit/funnel_obj.profit) * 100
    funnel_obj.ob_percent = (bumps.profit/funnel_obj.profit) * 100
    funnel_obj.upsell_percent = (ups.profit/funnel_obj.profit) * 100
    funnel_obj.round_numbers()

    return funnel_obj.__dict__

def get_funnel_data(funnel_id):
    funnel = Funnel.query.filter_by(id=funnel_id).first()
    steps = Cost.query.filter_by(funnel_id=funnel_id).all()
    main_dict = {"funnel": None, "frontend": [], "orderbump": [], "upsell": []}
    d = object_as_dict(funnel)
    main_dict['funnel'] = d
    for step in steps:
        if step.product_type == 'FE':
            main_dict['frontend'].append(object_as_dict(step))
        elif step.product_type == 'OB':
            main_dict['orderbump'].append(object_as_dict(step))
        elif step.product_type == 'US':
            main_dict['upsell'].append(object_as_dict(step))
    print(main_dict)
    return d

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

class FE_metrics(object):
    def __init__(self):
        for cls in reversed(self.__class__.mro()):
            if hasattr(cls, 'init'):
                cls.init(self)

    def init(self):
        self.revenue = 0
        self.cost = 0
        self.take_rate = 0   
        self.unique_views = 0  
        self.profit = 0
        self.orders = 0
    def calc_profit(self):
        self.profit= self.revenue - self.cost

class OB_metrics(object):
    def __init__(self):
        for cls in reversed(self.__class__.mro()):
            if hasattr(cls, 'init'):
                cls.init(self)

    def init(self):
        self.revenue = 0
        self.cost = 0
        self.take_rate = 0   
        self.unique_views = 0  
        self.profit = 0

    def calc_profit(self):
        self.profit= self.revenue - self.cost

class US_metrics(object):
    def __init__(self):
        for cls in reversed(self.__class__.mro()):
            if hasattr(cls, 'init'):
                cls.init(self)

    def init(self):
        self.revenue = 0
        self.cost = 0
        self.take_rate = 0   
        self.unique_views = 0  
        self.profit = 0 
        self.orders = 0

    def calc_profit(self):
        self.profit= self.revenue - self.cost

class Funnel_metrics(object):
    def __init__(self):
        for cls in reversed(self.__class__.mro()):
            if hasattr(cls, 'init'):
                cls.init(self)

    def init(self):
        self.upsell_percent = 0
        self.frontend_percent = 0
        self.ob_percent=0
        self.net_aov = 0
        self.net_epc = 0
        self.name = ''
        self.traffic = 0
        self.revenue = 0
        self.cost = 0
        self.profit = 0 
        self.aov = 0
        self.epc = 0
        self.orders = 0

    def calc_profit(self):
        self.profit= self.revenue - self.cost
    def round_numbers(self):
        self.revenue = round(self.revenue,2)
        self.cost = round(self.cost,2)
        self.profit = round(self.profit,2)
        self.aov = round(self.aov,2)
        self.epc = round(self.epc,2)
        self.net_aov = round(self.net_aov,2)
        self.net_epc = round(self.net_epc,2)
        self.upsell_percent = round(self.upsell_percent,2)
        self.frontend_percent = round(self.frontend_percent,2)
        self.ob_percent=round(self.ob_percent,2)