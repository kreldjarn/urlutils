from distutils.core import setup

setup(
    name='urlutils',
    version='0.0.7',
    packages=['urlutils',],
    include_package_data = True,
    license='BSD Licence',
    long_description=open('README.md').read(),
    author = 'Kristjan Eldjarn Hjorleifsson',
    author_email = 'kristjan@eldjarn.net',
)