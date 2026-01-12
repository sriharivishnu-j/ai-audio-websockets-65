from setuptools import setup, find_packages

setup(
    name='realtime-ai-audio-analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastapi==0.70.0',
        'uvicorn==0.15.0',
        'numpy==1.21.2',
        'scipy==1.7.1',
    ],
)