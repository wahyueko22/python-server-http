import socket
import json

def parse_multipart_body(body, boundary):
    parts = body.split(boundary)
    files = {}
    for part in parts:
        if part:
            headers_end = part.find("\r\n\r\n") + 4
            part_headers = part[:headers_end].strip()
            part_body = part[headers_end:].strip()
            disposition = [h for h in part_headers.split("\r\n") if "Content-Disposition" in h][0]
            disposition_params = {k.strip(): v.strip('"') for k, v in [item.split('=') for item in disposition.split(';')[1:]]}
            if 'filename' in disposition_params:
                files[disposition_params['filename']] = part_body
    return files

def handle_binary_upload(body, headers):
    if 'Content-Type' in headers and 'multipart/form-data' in headers['Content-Type']:
        boundary = headers['Content-Type'].split("boundary=")[1]
        boundary = "--" + boundary
        files = parse_multipart_body(body, boundary)
        for filename, content in files.items():
            with open(filename, 'wb') as f:
                f.write(content.encode('latin-1'))  # Assuming content is binary

        response_content = json.dumps({"status": "success", "files": list(files.keys())})
        return (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json; charset=utf-8\r\n"
            f"Content-Length: {len(response_content)}\r\n"
            "\r\n"
            f"{response_content}"
        )
    else:
        try:
            json_data = json.loads(body)
            print(f"Received JSON data: {json_data}")
            response_content = json.dumps({"status": "success", "received": json_data})
            return (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: application/json; charset=utf-8\r\n"
                f"Content-Length: {len(response_content)}\r\n"
                "\r\n"
                f"{response_content}"
            )
        except json.JSONDecodeError:
            response_content = json.dumps({"status": "error", "message": "Invalid JSON"})
            return (
                "HTTP/1.1 400 Bad Request\r\n"
                "Content-Type: application/json; charset=utf-8\r\n"
                f"Content-Length: {len(response_content)}\r\n"
                "\r\n"
                f"{response_content}"
            )

def parse_header(request_data):
    # Step 2: Find the end of the headers
    headers_end = request_data.find("\r\n\r\n") + 4
    # Step 3: Extract headers part
    headers_data = request_data[:headers_end]
        
    # Step 4: Parse headers
    headers_lines = headers_data.split("\r\n")
    request_line = headers_lines[0]
    headers = {}
    for header_line in headers_lines[1:]:
        if header_line:
            key, value = header_line.split(":", 1)
            headers[key.strip()] = value.strip()

    # Print the request line and headers
    print(f"print headerrrr {request_line}")
    for key, value in headers.items():
        print(f"{key}: {value}")
    return headers

def handle_request(client_socket):
    # Receive the request data
    request_data = client_socket.recv(1024).decode('utf-8')
    print(f"Received request:\n{request_data}")
    
    headers = parse_header(request_data)
    
    # Split the request to get the request line
    request_line = request_data.splitlines()[0]
    print(f"Request line: {request_line}")
    
    # Extract the method and path from the request line
    method, path, _ = request_line.split()
    
    # Process GET and POST requests
    if method == 'GET':
        if path == '/':
            content = "<h1>Welcome to my HTTP server!</h1>"
        else:
            content = f"<h1>404 Not Found</h1><p>The requested URL {path} was not found on this server.</p>"
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            f"Content-Length: {len(content)}\r\n"
            "\r\n"
            f"{content}"
        )
    elif method == 'POST':
        # Find the start of the body
        body_start = request_data.find("\r\n\r\n") + 4
        body = request_data[body_start:]
        response = handle_binary_upload(body, headers)
    else:
        content = "<h1>405 Method Not Allowed</h1><p>Only GET and POST requests are allowed.</p>"
        response = (
            "HTTP/1.1 405 Method Not Allowed\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            f"Content-Length: {len(content)}\r\n"
            "\r\n"
            f"{content}"
        )
    
    # Send the response back to the client
    client_socket.sendall(response.encode('utf-8'))
    
    # Close the client socket
    client_socket.close()

def run_server(host='127.0.0.1', port=8181):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow the socket to be reused immediately after the program exits
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Serving HTTP on {host} port {port} ...")
    
    while True:
        # Accept a new client connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        
        # Handle the request
        handle_request(client_socket)

def main():
    run_server()
    
# Run the server
if __name__ == '__main__':
    run_server()
