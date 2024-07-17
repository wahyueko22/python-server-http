from setuptools import setup, find_packages

setup(
    name="http-server-app",
    version="0.1",
    #packages=find_packages(),
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points={
        'console_scripts': [
            'http-server=server.server_http:main',
        ],
    },
)
