from setuptools import setup

setup(
    name='flask-application',
    packages=['application'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)