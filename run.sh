#!/bin/bash
echo ""
echo ""
echo "				st33lbox	"
echo ""
echo ""
echo ""
echo ""
echo "first login as sudo"
sudo apt-get --yes --force-yes install firewalld openssh-client openssh-server
echo "installing firewalld & openssh"
echo "launching script"
sudo python3 st33l.py
echo "bye!"