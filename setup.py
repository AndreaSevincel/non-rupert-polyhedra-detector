from setuptools import setup, find_packages

setup(
    name='non-rupert-polyhedra-detector',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A project to detect non-Rupert convex polyhedra using algorithms and machine learning.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'scipy',
        'scikit-learn',
        'matplotlib',
        'pandas',
        'jupyter'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)