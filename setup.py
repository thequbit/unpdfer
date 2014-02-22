from setuptools import setup

long_description = \
'''Yada

Yada
'''

setup(
    name="unpdfer",
    version="0.0.1",
    license="GPL3",
    author="Timothy Duffy",
    author_email="tim@timduffy.me",
    py_modules=["unpdfer"],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
      'pdfminer==20110515'
    ],
    long_description=long_description,
    description='Yada yada yada',
    url='https://github.com/thequbit/unpdfer',
    classifiers=[],
)
