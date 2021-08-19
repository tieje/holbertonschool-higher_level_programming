#!/bin/bash 
#Uses post method for url and displays response's body
curl -s "$1" -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD'
