# the-cryptor

Text File encryption programme using python and an RSA Cipher

You have to click the Encrypt Button Once, and the results of encrypted data will automatical appear on the screen. However, If you click the Ecnrypt twice, or more, the program will continue ecnrypting over the ecnrypted file. Therefore to decrypt it to the original text file, you have to continue decrypting the file until it becomes readable text again.

To decrypt, Right Click on the taxt Area--> Select RUN--> (Pop Up tk Window appears)--> PIN [2143].

You have to enter the PIN otherwise an error message appears warning you entered wrong PIN. So make sure you enter correct PIN

The Decry Button is not working properly, I am still researching as to how I can Bind the same POPUP function I bound on the POPUP->RUN. 
There is a progress bar embeded inside the Decryption Funtion. However, I didn't understand how to call it such that it runs based on the decryption progress.

Something else I want to achieve is this: 
  #Files should encrypt to the Filepath I choose upon selecting the text file to encrypt. Right now the filepath is static.
  
  #The Welcome textfield should be disbaled.
  
  #The Encrypted Text field should be disabled to avert the danger of someone changing any number by accident
  
  #ETC...............
 
 # Things to Note
 * Do not edit contents in the cr_k_ii.txt and the cr_k_ii.txt. They contain the Private and public keys. Changing any figure in these files can disturbe the behaviour of the encryption process.
 
 * The cr_k_i.txt text file contains items I wrote personally. It is the file whose contents are being encrypted and decrypted. You can change the contents and write your own.
 
 * If the contents of the cr_k_i.txt file are already decrypted, an error  in the terminal command is generated: [ ValueError: not enough values to unpack (expected 3, got 1) ]. Therefore, Encrypt the file first. I am still trying to figure out how to suppress that error, and how to make the Decryption function to give a warning that the file is already decrypted.
 
+ Encrypting too many times can cause slow downs in decrypting process. Avoid ecnrypting too many times

* When you want to run the program using python on a windows os, you have to specify the absolute path, otherwise the FILEPATH errors will popup. Especially the filepath to the Public and Private Keys have to be specified eg: *file='C:\Users\User\Folder\Folder\file.txt'

# Changes (12 January 2019)
I have begun major changes. However, for now there are minor changes I wish to point out.
* I have cleaned the encryption and decryption codes. One file contains only code that it requires. Other files have been moved to their respective files.
* I have added a blank file named fil_et.txt. This textfile is blank because it is used to receive a file from the terminal command, or the textbox, before it it passed to the encryption functions. Once it has been used by the encryptor module, it is emptied of its contents immediately. At no point in time should there be a readable textfile wxcept dusing the time the user is typing. After they hit the encrypt button, everything should be a mystery.

