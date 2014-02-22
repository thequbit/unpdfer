from setuptools import setup

long_description = \
'''

A simple wrapper around pdfminer 201105115.

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
      'pdfminer==20110515',
    ],
    long_description=long_description,
    description='Converts pdfs to text',
    url='https://github.com/thequbit/unpdfer',
    classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Operating System :: POSIX',
    ],
)
