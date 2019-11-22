from setuptools import setup

INSTALL_REQUIREMENTS = [
    'flask',
    'flask-restful',
    'flask-socketio',
    'flask-httpauth',
    'flask-sqlalchemy']

# TESTS_REQUIREMENTS = [
#     'jsondiff == 1.1.2',
#     'pylint == 2.3.1',
#     'pytest == 4.4.1',
#     'vulture == 1.0',
#     'bandit == 1.6.0'
# ]

# EXTRAS = {
#     'testing': TESTS_REQUIREMENTS
# }

setup(
    name='rpgc_server',
    version='0.1',
    description='RPGChat Server',
    author="Fruktus",
    packages=['rpgc_server'],
    install_requires=INSTALL_REQUIREMENTS,
    setup_requires=INSTALL_REQUIREMENTS,
    # tests_require=TESTS_REQUIREMENTS,
    # extras_require=EXTRAS,
    # test_suite="tests",
    zip_safe=False
)
