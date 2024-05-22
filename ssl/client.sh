#!/bin/bash


# Get client address
read -p "	Enter client IP: " cliip
echo "	connecting to: $cliip"

# Connect to the server
echo "Connecting to OpenSSL server..."
# Send a custom message to request the public key
echo "GET_PUBLIC_KEY" | openssl s_client -connect ${cliip}:9812 -quiet -ign_eof | \
while IFS= read -r line; do
  if [[ "$line" == "PUBLIC_KEY_SENT" ]]; then
    # Start reading the public key from the server
    echo "Receiving public key from server..."
    # Skip the next line (-----BEGIN PUBLIC KEY-----)
    read -r line
    # Read the public key lines and save them to a file
    while IFS= read -r line; do
      if [[ "$line" == "-----END PUBLIC KEY-----" ]]; then
        break
      else
        echo "$line" >> server_pubkey.pem
      fi
    done
    echo "Public key received and saved as server_pubkey.pem"
  else
    echo "$line"
  fi
done
