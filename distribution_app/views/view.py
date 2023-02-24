from flask import Blueprint,render_template
from ..models.model import Manufacturer

bp = Blueprint('view', __name__)

@bp.route('/',methods=['GET'])
def manufacturers():
    title='Manufacturers'
    manufacturers_list=Manufacturer.query.all()
    return render_template('manufacturers.html',title=title,manufacturers_list=manufacturers_list)