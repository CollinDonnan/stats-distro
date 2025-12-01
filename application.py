"""
AWS Elastic Beanstalk entry point.

EB's Python platform expects a file named 'application.py' with a WSGI
application object named 'application'.
"""

from app import application

# AWS EB will use this 'application' object
__all__ = ['application']
