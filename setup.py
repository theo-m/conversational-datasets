#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os

from setuptools import find_packages
from setuptools import setup

# Package meta-data.
NAME = "conversational_datasets"
DESCRIPTION = ""
URL = "https://github.com/PolyAI-LDN/conversational-datasets"
EMAIL = "matt@matthen.com"
AUTHOR = "Matthew Henderson"
REQUIRES_PYTHON = "==2.7.13"
VERSION = 0.1

# See: https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/
# At the end of section "Multiple File Dependencies" to understand the need for the
# following ugly block.
REQUIRED = [
    "absl-py==0.7.0",
    "apache-beam==2.5.0",
    "astor==0.7.1",
    "avro==1.8.2",
    "backports.weakref==1.0.post1",
    "bert-tensorflow==1.0.1",
    "cachetools==3.1.0",
    "certifi==2018.11.29",
    "chardet==3.0.4",
    "Click==7.0",
    "configparser==3.7.3",
    "crcmod==1.7",
    "dill==0.2.6",
    "docopt==0.6.2",
    "entrypoints==0.3",
    "enum34==1.1.6",
    "fasteners==0.14.1",
    "flake8==3.7.6",
    "flake8-polyfill==1.0.2",
    "funcsigs==1.0.2",
    "functools32==3.2.3.post2",
    "future==0.16.0",
    "futures==3.2.0",
    "gapic-google-cloud-pubsub-v1==0.15.4",
    "gast==0.2.2",
    "glog==0.3.1",
    "google-apitools==0.5.20",
    "google-auth==1.6.3",
    "google-auth-httplib2==0.0.3",
    "google-cloud-bigquery==0.25.0",
    "google-cloud-core==0.25.0",
    "google-cloud-dataflow==2.5.0",
    "google-cloud-pubsub==0.26.0",
    "google-gax==0.15.16",
    "googleapis-common-protos==1.5.8",
    "googledatastore==7.0.1",
    "grpc-google-iam-v1==0.11.4",
    "grpcio==1.19.0",
    "h5py==2.9.0",
    "hdfs==2.2.2",
    "httplib2==0.9.2",
    "idna==2.8",
    "isort==4.3.4",
    "Keras-Applications==1.0.7",
    "Keras-Preprocessing==1.0.9",
    "Markdown==3.0.1",
    "mccabe==0.6.1",
    "mock==2.0.0",
    "monotonic==1.5",
    "numpy==1.16.2",
    "oauth2client==2.0.1",
    "pbr==5.1.3",
    "pep8-naming==0.5.0",
    "ply==3.8",
    "proto-google-cloud-datastore-v1==0.90.4",
    "proto-google-cloud-pubsub-v1==0.15.4",
    "protobuf==3.7.0",
    "pyasn1==0.4.5",
    "pyasn1-modules==0.2.4",
    "pycodestyle==2.5.0",
    "pyflakes==2.1.1",
    "python-gflags==3.1.2",
    "pytz==2018.9",
    "PyVCF==0.6.8",
    "PyYAML==3.12",
    "requests==2.21.0",
    "rsa==4.0",
    "scikit-learn==0.20.3",
    "scipy==1.2.1",
    "six==1.10.0",
    "sklearn==0.0",
    "tensorboard==1.12.0",
    "tensorflow==1.12.0",
    "tensorflow-estimator==1.10.12",
    "tensorflow-hub==0.3.0",
    "termcolor==1.1.0",
    "tqdm==4.31.1",
    "typing==3.6.6",
    "urllib3==1.24.2",
    "Werkzeug==0.14.1",
    "zstandard==0.11.1"
]


# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    scripts=[],
    packages=find_packages(exclude=("tests",)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
    classifiers=[]
)
