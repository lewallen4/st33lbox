#!/bin/bash

# Check if server.pem exists, if not, create it
if [ ! -f server.pem ]; then
  echo "Generating self-signed certificate..."
  openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes <<EOF







EOF
fi

# Start OpenSSL server in the background
echo "Starting OpenSSL server..."
# Use `stdbuf -i0 -o0 -e0` to make sure the I/O is not buffered
(stdbuf -i0 -o0 -e0 openssl s_server -quiet -key server.pem -cert server.pem -port 9812) &

# Wait for the server to start
sleep 2

# Connect to the server from the client
echo "Connecting to OpenSSL server..."
# Use `-ign_eof` to ensure the connection doesn't close
openssl s_client -connect localhost:9812 -quiet -ign_eof

# Provide a shell on the server side
/bin/sh -i
