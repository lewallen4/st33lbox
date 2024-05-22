#!/bin/bash

# Connect to the server
echo "Connecting to OpenSSL server..."
# Send a custom message to request the public key
echo "GET_PUBLIC_KEY" | openssl s_client -connect 3.143.17.150:9812 -quiet -ign_eof
