# JDownloader-CnL-Decryptor

Utility to decrypt messages encrypted by the C'n'L component of JDownloader

## Usage

```
python jdCnLDecryptor.py --b64=<base64> [--jdkey=<jdkey>]
```
--b64 : base64 data to decrypt

--jdkey : optional jdkey in hex string. Using default JDownloader key by default

Showing example of decryption from https://jdownloader.org/knowledge/wiki/glossary/cnl2

![](img.png)

Data: DRurBGEf2ntP7Z0WDkMP8e1ZeK7PswJGeBHCg4zEYXZSE3Qqxsbi5EF1KosgkKQ9SL8qOOUAI+eDPFypAtQS9A==

Using default jdkey: 1234567890987654

Result: http://rapidshare.com/files/285626259/jDownloader.dmg

## Requirements

```
pycryptodome 3.19.0
```