from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name='cbrf_rates',
    version=version,
    author='Vitaliy Shishorin',
    author_email='moskrc@gmail.com',
    url='http://github.com/moskrc/cbrf_rates/',
    download_url='http://github.com/moskrc/cbrf_rates/archive/master.zip',

    description='Grab currency rates from cbr.ru (The Central Bank of the Russian Federation)',
    long_description=open('README.rst').read().decode('utf8'),
    license='MIT license',
    keywords='cbr cbrf rates money',

    packages=find_packages(),


    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['requests>=2.5.0', 'xmltodict>=0.9.0', ],
)
