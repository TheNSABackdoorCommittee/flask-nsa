from setuptools import setup

def long_desc():
    with open('README.md', 'rb') as f:
        return f.read()

kw = {
    "name": "Flask-NSA",
    "version": "0.1.0",
    "url": "https://github.com/plausibility/flask-nsa",
    "license": "MIT",
    "author": "plausibility",
    "author_email": "chris@gibsonsec.org",
    "description": "Provide access to the NSA for your application user's secrets.",
    "long_description": long_desc(),
    "keywords": "nsa flask secrets privacy orwell 1984",
    "packages": [
        "flask_nsa"
    ],
    "zip_safe": False,
    "install_requires": ["flask"],
    "tests_require": "nose",
    "test_suite": "nose.collector",
    "classifiers": [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Legal Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Security",
        "Topic :: System :: Monitoring"
    ]
}

if __name__ == "__main__":
    setup(**kw)
