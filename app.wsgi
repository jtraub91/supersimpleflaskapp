activate_this = '/srv/supersimpleflaskapp/venv/bin/activate_this.py'


with open(activate_this) as f:
    exec(f.read(), dict(__file__=activate_this))

    import app as application

