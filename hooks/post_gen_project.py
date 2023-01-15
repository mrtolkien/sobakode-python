"""Project post-generation setup.
"""
import os

# Setting up poetry
os.system("poetry install")
# Adding pre-commit
os.system("git init")
os.system("poetry run pre-commit install")
# Running the default test for validation
os.system("poetry run pytest")
