#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask.cli import FlaskGroup

from app import app


cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()
