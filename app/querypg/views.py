from flask import Blueprint, render_template, request

from . import querypg

from app import db

from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information






@querypg.route('/')
def querypg():
    aaseqquery= request.args.get('aaseqquery')
    aaquery=Information.query.filter_by(aa_seq=aaseqquery).first()
    class_search= (aaquery.rep_rep.rep_family.rep_class)
    family_search= (aaquery.rep_rep.rep_family)
    name_search= (aaquery.rep_rep)


    return render_template('querypg.html', class_search=class_search, family_search=family_search, name_search=name_search)
