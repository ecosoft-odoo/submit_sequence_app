from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in submit_sequence_app/__init__.py
from submit_sequence_app import __version__ as version

setup(
	name="submit_sequence_app",
	version=version,
	description="Run Sequence On Submit",
	author="Ecosoft",
	author_email="kittiu@ecosoft.co.th",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
