# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# verifyKeyCert-app.py
#
# Cripto-7.5.0 - Commmad line app to verify if the private key has the correspondant
#           certificate.
#
# Copyright (c) 2016 Universidade do Minho
# Developed by André Baptista - Devise Futures, Lda. (andre.baptista@devisefutures.com)
# Reviewed by Ricardo Barroso - Devise Futures, Lda. (ricardo.barroso@devisefutures.com)
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
###############################################################################
"""
Command line app that verifies if the private key has the correspondant certificate..
"""

import sys
import getopt
from eVotUM.Cripto import eccblind
from eVotUM.Cripto import shamirsecret
from eVotUM.Cripto import utils

def printUsage():
    print("Usage: python verifyKeyCert-app.py --cert <certificado> --msg <mensagem original> --sDash <Signature> -f <requerente>")

def parseArgs():
    if (len(sys.argv) != 8):
        printUsage()

    else:
        opts, args = getopt.getopt(sys.argv[1:], "hc:m:d:f:", ["help", "cert=", "msg=", "sDash=", "file="])
        msg = None
        eccPublicKeyPath = None
        sDash = None
        filename = None
        
        for o,a in opts:
        if o in ("-h", "--help"):
            printUsage()
            sys.exit()

        elif o in ("-c", "--cert"):
            eccPublicKeyPath = sys.argv[2]

        elif o in ("-m", "--msg"):
            msg = sys.argv[4]

        elif o in ("-d", "--sDash"):
            sDash = sys.argv[6]

        elif o in ("-f", "--File"):
            filename = sys.argv[8]

        else:
            print("Error: Unknown option.")
            printUsage()
            sys.exit(2)

        main(eccPublicKeyPath, msg, sDash, filename)

def showResults(errorCode, validSignature):
    if (errorCode is None):
        if (validSignature):
            print("Valid signature")
        else:
            print("Invalid signature")
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the public key")
    elif (errorCode == 2):
        print("Error: pR components are invalid")
    elif (errorCode == 3):
        print("Error: blind components are invalid")
    elif (errorCode == 4):
        print("Error: invalid signature format")

def main(eccPublicKeyPath, msg, sDash, filename):
    pemPublicKey = utils.readFile(eccPrivateKeyPath)
    components = utils.readFile(filename)
    blindComponents, pRComponents = components.split('\n')[:2]
    errorCode, validSignature = eccblind.verifySignature(pemPublicKey, signature, blindComponents, pRComponents, data)
    showResults(errorCode, validSignature)

if __name__ == "__main__":
    parseArgs(
