#!/bin/bash

echo """
===========================================================
                AIXY PROJECT Voice Instalation
===========================================================
"""
sudo apt update
sudo apt install espeak libespeak-dev
sudo apt install mbrola
sudo apt install mbrola-us2

echo "Instalation completed with success!"