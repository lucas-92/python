#!/usr/bin/env python3
"""Multi language Hello World.

This software show the message 'Hello, World!' accordingly the language 
configured in the enviroment variable LANG.

How to use:

1 - Export the LANG enviroment variable:
    export LANG=pt_BR

2 - Execute:
    python3 hello.ppy
    or
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Lucas Santos"
__license__ = "Unlicense"

import os 

current_language = os.getenv("LANG", "pt_BR")[:5]

msg = "Olá, Mundo!"

if current_language == "en_US":
    msg = "Hello, World!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo"
elif current_language == "es_SP":
    msg = "Hola, Mundo"
elif current_language == "fr_FR":
    msg = "Bonjou Monde"
elif current_language == "ja_JP":
    msg = "こんにちは世界"

print(msg)
