#!/bin/bash

# Check if server.pem exists, if not, create it
if [ ! -f server.pem ]; then
  echo "Generating self-signed certificate..."
  openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes <<EOF







EOF
fi

# Extract the public key from the server's certificate
echo "Extracting public key from server certificate..."
openssl x509 -pubkey -noout -in server.pem > server_pubkey.pem

# Start OpenSSL server in the background
echo "Starting OpenSSL server..."
# Use `stdbuf -i0 -o0 -e0` to make sure the I/O is not buffered
(stdbuf -i0 -o0 -e0 openssl s_server -quiet -key server.pem -cert server.pem -port 9812 | \
while IFS= read -r line; do
  if [[ "$line" == "GET_PUBLIC_KEY" ]]; then
    echo "Sending public key to client..."
    cat server_pubkey.pem
    echo "PUBLIC_KEY_SENT"
  else
    echo "$line"
  fi
done) &

# Wait for the server to start
sleep 2
