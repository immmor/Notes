from setuptools import setup, find_packages

setup(
    name='Notes',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask', 'flasgger'
    ],
    entry_points={
        'console_scripts': [
            'your_command=your_package.your_module:your_function',
        ],
    },
)