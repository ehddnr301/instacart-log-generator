from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='instacart-log-generator',

version='0.1.4',

description='Generate fake log based on instacart dataset',

long_description= long_description,

long_description_content_type="text/markdown",

author='ehddnr301',

author_email='dy95032@gmail.com',

url='https://github.com/ehddnr301/instacart-log-generator',

license='MIT',

py_modules=['instacart_log_generator/INFO', 'instacart_log_generator/my_gen_log'],

python_requires='>=3.8',

install_requires=['numpy==1.22.0'],

packages=['instacart_log_generator'],

include_package_data=True,

package_data={'': ['sample.npy']}

)