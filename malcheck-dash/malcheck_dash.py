#!/usr/bin/env python
from malcheck_dash.config import app, db

if __name__ == "__main__":
    db.create_all()
    app.run()
