# Encryption
How to use:
from command line run:

1) If you want to encrypt with Caesar cipher with parameter shift:
   python3 main.py --mode=Enc --path_from=<file_to_encrypt> --path_to=<file_to_decrypt> --typeCipher=Caesar --params 'shift'= <number_shift>
2) If you want to decrypt with Caesar cipher with parameter shift:
   python3 main.py --mode=Dec --path_from=<file_to_decrypt> --path_to=<file_to_write_unciphred> --typeCipher=Caesar --params 'shift'= <number_shift>
   
2.5) If you want to Hack the Caesar cipher, 
   python3 main.py --mode=Hack --path_from=<file_to_decrypt> --path_to=<file_to_write_unciphred> --typeCipher=Caesar

3) If you want to encrypt with Vigener cipher with parameter keyword:
   python3 main.py --mode=Enc --path_from=<file_to_encrypt> --path_to=<file_to_decrypt> --typeCipher=Vigener --params 'keyword'=<keyword>
   
4) If you want to decrypt with Vigener cipher with parameter keyword:
   python3 main.py --mode=Dec --path_from=<file_to_decrypt> --path_to=<file_to_write_unciphred> --typeCipher=Vigener --params 'keyword'=<keyword>
   
5) If you want to encrypt with Vernam cipher with parameter keyword(it's length should be equal the length of message):
   python3 main.py --mode=Enc --path_from=<file_to_encrypt> --path_to=<file_to_decrypt> --typeCipher=Vernam --params 'keyword'=<keyword>
   
6) If you want to decrypt with Vernam cipher with parameter keyword:
   python3 main.py --mode=Dec --path_from=<file_to_decrypt> --path_to=<file_to_write_unciphred> --typeCipher=Vernam --params 'keyword'=<keyword>