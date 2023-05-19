from setuptools import find_packages, setup

setup(
    name='var_voltage_control',
    version='0.0.1',
    author='Anon Anonymous',
    author_email='anon@anonymous.com',
    packages=find_packages(),
    url='',
    license='',
    description='Var Voltage Control',
    long_description="",
    install_requires=[
        "numpy",
        "pandas",
        "pandapower",
        "PyYAML",
        "matplotlib",
        "numba"
        ],
    )