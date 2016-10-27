from setuptools import setup, find_packages

setup(
    name='bonsai-cli',
    version='0.1',
    py_modules=['bonsai'],
    include_package_data=True,
    install_requires=[
        'Click',
        'psutil',
    ],
    entry_points='''
        [console_scripts]
        bonsai=bonsai:cli
    ''',
)

