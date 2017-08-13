from setuptools import find_packages, setup

dependencies = ['click']

setup(
    name='ticket',
    version='0.1.0',
    url='https://github.com/dp28/ticket',
    license='MIT',
    author='Daniel Patterson',
    author_email='dan24patt@gmail.com',
    description='Command line tool to make it easier to work with git & pivotal tracker',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'ticket = ticket.cli.app:app',
        ],
    },
)
