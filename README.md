# Encryption

The program allows you to encrypt and decrypt sentences using a number of crypto-algorithms.
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
   
###ADDITIONAL CIPHERS:
7) If you want to encrypt with Gronsfeld cipher with parameter digits:
   python3 main.py --mode=Enc --path_from=<file_to_encrypt> --path_to=<file_to_decrypt> --typeCipher=Gronsfeld --params 'digits'=<digits>
   
8) If you want to decrypt with Gronsfeld cipher with parameter digits:
   python3 main.py --mode=Dec --path_from=<file_to_decrypt> --path_to=<file_to_write_unciphred> --typeCipher=Gronsfeld --params 'digits'=<digits>
   
9) If you want to encrypt with Stega cipher with parameter Image:
   python3 main.py --mode=Enc --path_from=<file_to_encrypt> --path_to=<dir_to_put_image> --typeCipher=Stega --params 'image_path'=<path_to_image>
   
10) If you want to decrypt with Stega cipher with parameter Image:
   python3 main.py --mode=Dec --path_to=<file_to_write_unciphred> --typeCipher=Stega --params 'image_path'=<path_to_image> 'mess_length' = <length_of_message(default = 50)>
   
