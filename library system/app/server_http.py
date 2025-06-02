from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import os
from login1 import authenticate

# Define a custom request handler
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Respond to GET requests
            self.send_response(200)  # Send a 200 OK status code
            # print(f"headers of html file: -> {self.headers}")
            self.send_header('Content-type', 'text/html')  # Set the content type to HTML
            self.end_headers()  # End the headers
            
            file_path = os.path.join('templates', 'index.html') #create path to frontend files
            print(f"file path ->{file_path}")
            if os.path.exists(file_path): #check if file exists
                with open(file_path, 'rb') as file: #file opened in binary mode
                    self.wfile.write(file.read()) #client receive this data as the body of the HTTP response.
            else:
                self.send_error(404, "file not found")
        
        #serve static files (CSS, JS etc)
        elif self.path.startswith('/static'):
            file_name = os.path.basename(self.path)
            file_path = os.path.join('static',file_name)
            # print(f"Attempting to server static file: -> {file_path}")

            #check if file exists
            if os.path.exists(file_path):
                self.send_response(200)

                # Set the appropriate Content-Type header based on the file extension
                if file_path.endswith('.css'):
                    # print(f"headers of css file: -> {self.headers}") #shows headers, helps in debugging
                    self.send_header('Content-type', 'text/css')
                elif file_path.endswith('.js'):
                #     # print(f"headers of .js file: -> {self.headers}")
                    self.send_header('Content-type', 'text/javascript')
                else:
                    self.send_header('Content-type', 'text/plain')

                self.end_headers()  # End the headers

                # Serve the file
                with open(file_path, 'rb') as file:
                    self.wfile.write(file.read())
            
            else:
                self.send_error(404, 'Static files Not found')
        else:
            self.send_error(404, 'Not found')


    def do_POST(self):
        #handle login request
        if self.path == '/login1':
            # Handle POST requests
            content_length = int(self.headers['Content-Length'])  # Get the length of the data
            post_data = self.rfile.read(content_length)  # Read the data
            message = post_data.decode('utf-8').split('=')[1]  # Extract the message from the form data
            data = urllib.parse.parse_qs(post_data.decode('utf-8')) #parses URL encoded data into dictionary
            print(f"data ->{data}")
            print(f"message -> {message}")
            username = data.get('username')[0]
            password = data.get('password')[0]

            #call autheicate funcation inside login
            if authenticate(username, password):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<h1>Login Successful!</h1>")
            else:
                self.send_response(401)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<h1>Login Failed</h1>")

# Function to run the server
def run(server_class=HTTPServer, handler_class=SimpleHandler):
    server_address = ('', 8000)  # Serve on all interfaces, port 8000
    httpd = server_class(server_address, handler_class)
    print("Starting server on port 8000...")
    httpd.serve_forever()  # Start the server

# Run the server if this script is executed
if __name__ == "__main__":
    run()

