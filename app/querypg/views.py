from flask import Blueprint, render_template

from . import querypg

from app import db

from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information




@querypg.route('/')
def querypg():
    aaseqquery='LPNQISKLVIKLVTKIMWYWHKDR*ID*WNQIKFIHTQKLN**QKTH*KQMKKVQIV*QR*NI*KHIWGKKRKLDIY*RKGNWIPTSHPTPKSIPGG*NT*M'
    aaquery=Information.query.filter_by(aa_seq=aaseqquery).first()
    searchname= (aaquery.rep_rep.rep_family.rep_class)

    return render_template('querypg.html', searchname=searchname)
