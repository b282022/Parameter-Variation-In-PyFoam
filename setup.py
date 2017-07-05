import os, glob
from setuptools import setup


list_of_scripts = glob.glob(os.path.join('src', '*.py'))
list_of_scripts.remove('src/__init__.py')

required_installs = [
    'PyFoam==0.6.7',
    'numpy==1.12.1'
]


setup(
    name='ParameterVariationInOpenFOAM',
    packages=['src', 'tests'],
    version='0.1',
    scripts=list_of_scripts,
    entry_points={
        'console_scripts': [
            'pyfoam_automated.py = src.pyfoam_automated:main',
        ],
    },
    install_requires=required_installs

)
