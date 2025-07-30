from setuptools import setup, find_packages

setup(
    name='azure-devops-demo-app',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask'
    ],
    entry_points={
        'console_scripts': [
            'run-app=demo_app.app:app.run'
        ],
    },
)
