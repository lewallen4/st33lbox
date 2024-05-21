#!/bin/bash

# Check if server.pem exists, if not, create it
if [ ! -f server.pem ]; then
  echo "Generating self-signed certificate..."
  openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes <<EOF
null
null
null
null
null
null
null
EOF
fi

# Start OpenSSL server in the background
echo "Starting OpenSSL server..."
openssl s_server -quiet -key server.pem -cert server.pem -port 9812 -WWW &

# Wait for the server to start
sleep 2

# Connect to the server from the client
echo "Connecting to OpenSSL server..."
openssl s_client -connect localhost:9812 -quiet <<EOF
/bin/sh -i
EOF
