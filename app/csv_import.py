from app import db
import csv
import sys

#setting the max size of fields to maximum
csv.field_size_limit(sys.maxsize)

class CSVImport:
    def import_csv_to_db(self):
        with open('test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)  # skip the headers
            for row in reader:
                print(row)
                rep_name=(row[10])
                rep_class=(row[11])
                rep_family=(row[12])
                #dna_seq=(row[17])
                aa_seq=(row[18])
                # Check exact syntax
                #rn = rep_name
                #rn = Rep (rn=repName)
                #db.session.add(rn)
                #db.session.commit()

                #rc = rep_class
                #rc = Rep_class(rc=repClass)
                #db.session.add(rc)
                #db.session.commit()

                #rf=rep_family
                #rf = Rep_family(rf=repFamily)
                #db.session.add(rf)
                #db.session.commit()

                #as=aa_seq
                #as= Translated_products(as=aaseq)
                #db.session.add(as)
                #db.session.commit()
