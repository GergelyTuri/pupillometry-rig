from setuptools import setup, find_packages

setup(
    name='pupillometry-rig',
    version='1.0.0',
    description='measuring pupil size in mice',
    author='Gergely Turi',
    author_email='gt2253@cumc.clumbia.edu',
    url='https://github.com/GergelyTuri/pupillometry-rig',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)