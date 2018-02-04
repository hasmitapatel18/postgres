from flask import Blueprint, render_template

from . import searchingaa

from app import db

from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information




@searchingaa.route('/')
def searchingaa():
    aaseqquery='SAATLESGMAVLQNDTIWPSNSTPRYIPKKNCSYSNKYMYVHSSIIQNSQKTLGNNGPAMDEWINKL*YIPTTEHSSTIKRNKVLETCYNMGEPQKYHAK*RK*DTKCHILYGFIYMKYLE*ANSQRQKADCGGKGWWRGRMSSNCLMG**KRPGTRRKQ*LHNTINGLNPTELSTLNWLTLYSVNFTLILK'
    aaquery=Information.query.filter_by(aa_seq=aaseqquery).first()
    class_search= (aaquery.rep_rep.rep_family.rep_class)
    family_search= (aaquery.rep_rep.rep_family)
    name_search= (aaquery.rep_rep)


    return render_template('searchingaa.html', class_search=class_search, family_search=family_search, name_search=name_search)
