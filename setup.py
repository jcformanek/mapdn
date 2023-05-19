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
        "numpy==1.19.5",
        "pandas==1.1.3",
        "pandapower==2.7.0",
        "PyYAML",
        "matplotlib",
        "numba"
        ],
    )