Goals:   
(1)Become  familiar  with  some  of  the  cryptographic  libraries  and  functions
available on the system.
(2) View vulnerable states of a network server.

Details:
(1)
Generate  2  public-key/private-key  pairs,  one  for  encryption/decryption  and  one  for signing/verifying.
Take a file as input and call the appropriate routines to hash and sign
it, and also to encrypt it with a symmetric key and then encrypt the symmetric key with the public key of a recipient.  In addition, your program must be able to input a protected file,  decrypt  it,  hash  it,  and  verify the digital  signature  using  the  originator’s  public verification key.

During the lab demonstration of your program, the TA will supply a file to be protected.
The  TA  will  observe  the  protection  of  an  unprotected  file,  and  the  un-protection of a protected file.


I am using the python library [Cryptography](https://cryptography.io/).

https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/


Had this issue: https://github.com/JoshKaufman/ursa/issues/14


2)
https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/3/html/Security_Guide/ch-exploits.html

http://sectools.org/tag/vuln-scanners/

https://www.cvedetails.com/vulnerability-list/vendor_id-26/product_id-3436/version_id-92758/Microsoft-IIS-7.5.html

iis 7.5 Security Vulnerabilites
