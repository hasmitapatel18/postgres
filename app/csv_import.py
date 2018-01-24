from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Translated_products
from app import db
import csv
import sys


#setting the max size of fields to maximum
class CSVImport:
    def import_csv_to_db(self):
        with open('test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)  # skip the headers
            for row in reader:

                rep_name=(row[10])
                rep_class_name=(row[11])
                rep_family_name=(row[12])
                #dna_seq=(row[17])
                aa_seq=(row[18])
                #print(rep_name, rep_class, rep_family, aa_seq)

                rep_class = Rep_class.query.filter_by(name=rep_class_name).first()

                if(rep_class == None):
                    # Create rep class if not found and overwrite rep_class variable
                    rep_class = Rep_class(name=rep_class_name)
                    db.session.add(rep_class)
                    db.session.commit()

                rep_family = Rep_family.query.filter_by(name=rep_family_name).first()

                if(rep_family == None):

                    rep_family = Rep_family(name=rep_family_name, rep_class=rep_class)
                    db.session.add(rep_family)
                    db.session.commit()

                rep = Rep.query.filter_by(name=rep_name).first()

                if (rep == None):
                    rep = Rep(name=rep_name, rep_family=rep_family)
                    db.session.add(rep)
                    db.session.commit()

                aaseq = Translated_products(aa_seq=aa_seq, rep_rep=rep)
                db.session.add(aaseq)
                db.session.commit()

                # rn = rep_name
                # rn = Rep(name='repName')
                # db.session.add(rn)
                # db.session.commit()
                #
                # rc = rep_class
                # rc = Rep_class(name='repClass')
                # db.session.add(rc)
                # db.session.commit()
                #
                # rf=rep_family
                # rf = Rep_family(name='repFamily')
                # db.session.add(rf)
                # db.session.commit()
                #
                # aseq=aa_seq
                # aseq= Translated_products(name='aaseq')
                # db.session.add(aaseq)
                # db.session.commit()
