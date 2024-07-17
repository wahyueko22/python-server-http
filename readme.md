

# http-server

An HTTP server is a software application that serves web content to clients (typically web browsers) over the Hypertext Transfer Protocol (HTTP).
This project is creating an http server in Python from scratch. Basically, an http is a protocol that sits on top of a TCP connection.
It's better that all of you understand the concept of the OSI 7 layer, at least from layer 4 until layer 7. Usually,  each operating system will provide a TCP socket connection by default, and then we only need a little tweaking to build an HTTP connection on top of the TCP connection.
On this current version is only focus on http method get and http method POST.

## Set up env

- verify the python-3 is installed : python --version or python3 --version,  the expectation is python 3.9 and above
- verify the pip3 as well : pip3 --version or pip --version
- create new virtaul environtment : python3 -m venv venv  or python -m venv venv
- activate the virtual env : myenv\Scripts\activate
- install the requirement : pip install -r requirements.txt

## update new library on requirement.txt
- pip freeze > requirements.txt

## Installation

You can build and install http-server-app by issuing this command: 
- pip3 install .

## Run the application
http-server

## Run manuaally from file
- open terminal and go to /src/server directory then issue this command : python sever_http.py