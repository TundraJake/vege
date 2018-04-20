from flask_table import Table, Col
 
class Results(Table):
    id = Col('Id', show=False)
    bid = Col('bid')
    vege = Col('vege')
    bidding_user = Col('bidding_user')