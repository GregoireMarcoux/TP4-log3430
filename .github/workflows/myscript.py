import os

badhash = "1d87482"
goodhash = "bfdccab" 

os.system(f"git bisect start {badhash} {goodhash}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")