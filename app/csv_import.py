from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information
from app import db
import csv
import sys


#setting the max size of fields to maximum
class CSVImport:
    def import_csv_to_db(self):
        with open('../2ORFs_final.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)  # skip the headers
            for row in reader:

                sw_score=(row[1])
                mili_div=(row[2])
                mili_del=(row[3])
                mili_ins=(row[4])
                geno_name=(row[5])
                geno_start=(row[6])
                geno_end=(row[7])
                geno_left=(row[8])
                strand=(row[9])
                rep_name=(row[10])
                rep_class_name=(row[11])
                rep_family_name=(row[12])
                rep_start=(row[13])
                rep_end=(row[14])
                rep_left=(row[15])
                dna_seq=(row[17])
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



                info = Information(sw_score=sw_score, rep_rep=rep)
                info.mili_div=mili_div
                info.mili_del=mili_del
                info.mili_ins=mili_ins
                info.geno_name=geno_name
                info.geno_start=geno_start
                info.geno_end=geno_end
                info.geno_left=geno_left
                info.strand=strand
                info.name=rep_name
                info.rclass=rep_class_name
                info.rfamily=rep_family_name
                info.rep_start=rep_start
                info.rep_end=rep_end
                info.rep_left=rep_left
                info.dna_seq=dna_seq
                info.aa_seq=aa_seq



                db.session.add(info)
                db.session.commit()
