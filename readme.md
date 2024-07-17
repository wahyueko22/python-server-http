

# http-server

An HTTP server is a software application that serves web content to clients (typically web browsers) over the Hypertext Transfer Protocol (HTTP).
On current version only focus on http get and http POST.

## Set up env

- verify the python-3 is installed : python --version or python3 --version,  the expectation is python 3.9 and above
- verify the pip3 as well : pip3 --version or pip --version
- create new virtaul environtment : python3 -m venv venv  or python -m venv venv
- activate the virtual env : myenv\Scripts\activate
- install the requirement : pip install -r requirements.txt

## update new library on requirement.txt
- pip freeze > requirements.txt

for detail setup : https://docs.google.com/document/d/1HgP4rSnfkzfIbMdA9218JagS7Ey86ZgnAi9vmALFRWg/edit?usp=sharing

## Installation

You can build and install http-server-app by issuing this command: 
- pip3 install .

## Run the application
http-server

## Run manuaally from file
- open terminal and go to /src/server directory then issue this command : python sever_http.py