import base64
import getopt
import sys
from Crypto.Cipher import AES


def usage():
    print("Usage:")
    print("python jdCnLDecryptor.py --b64=<base64> [--jdkey=<jdkey>]")
    print("--b64 : base64 data to decrypt")
    print("--jdkey : optional jdkey. Using default JDownloader key by default")
    print("Showing example of decryption from https://jdownloader.org/knowledge/wiki/glossary/cnl2")


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "b64=", "jdkey="])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    b64 = None
    jdkey = None

    if len(opts) == 0:
        usage()
    else:
        for o, a in opts:
            if o == "--b64":
                b64 = a
            elif o == "--jdkey":
                jdkey = a
            else:
                assert False, "unhandled option"

    datab64 = "DRurBGEf2ntP7Z0WDkMP8e1ZeK7PswJGeBHCg4zEYXZSE3Qqxsbi5EF1KosgkKQ9SL8qOOUAI+eDPFypAtQS9A=="
    key = '\x31\x32\x33\x34\x35\x36\x37\x38\x39\x30\x39\x38\x37\x36\x35\x34'

    if b64 is not None:
        datab64 = b64
    else:
        print("Data: "+datab64)
    if jdkey is not None:
        bi = ""
        for a, b in zip(jdkey[::2], jdkey[1::2]):
            bi += bytes.fromhex(a+b).decode("ascii")
        key = bi
        print("Using key: "+key)
    else:
        print("Using default jdkey: "+str(key))

    iv = key

    print()
    decryptor = AES.new(key, AES.MODE_CBC, iv)
    f = decryptor.decrypt(base64.b64decode(datab64))
    print(f.decode("ascii"))


if __name__ == '__main__':
    main()


