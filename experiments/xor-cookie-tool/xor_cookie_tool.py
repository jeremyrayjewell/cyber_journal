#!/usr/bin/env python3
import base64
import argparse
import json
import itertools
import sys


def xor(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])


def decode_cookie(cookie, known_plaintext):
    try:
        decoded = base64.b64decode(cookie)
    except Exception as e:
        print(f"[!] Failed to decode base64: {e}")
        sys.exit(1)

    known_bytes = known_plaintext.encode()
    key = bytes([c ^ p for c, p in zip(decoded, known_bytes)])
    print(f"[+] Guessed key (raw bytes): {key}")
    print(f"[+] Guessed key (UTF-8): {key.decode(errors='ignore')}")
    plaintext = xor(decoded, key)
    print(f"[+] Decrypted content:\n{plaintext.decode(errors='ignore')}")


def encode_cookie(json_string, key):
    data = json_string.encode()
    key_bytes = key.encode()
    encrypted = xor(data, key_bytes)
    encoded = base64.b64encode(encrypted)
    print(f"[+] Encrypted cookie:\n{encoded.decode()}")


def main():
    parser = argparse.ArgumentParser(description="XOR Cookie Tool for Natas-style challenges")
    subparsers = parser.add_subparsers(dest='mode', required=True)

    # Decode
    decode_parser = subparsers.add_parser('decode', help='Decode an XOR-encrypted cookie')
    decode_parser.add_argument('--cookie', required=True, help='Base64-encoded cookie value')
    decode_parser.add_argument('--known', required=True, help='Known plaintext JSON')

    # Encode
    encode_parser = subparsers.add_parser('encode', help='Encode a JSON string with a known key')
    encode_parser.add_argument('--json', required=True, help='JSON string to encode')
    encode_parser.add_argument('--key', required=True, help='Key to use for XOR encryption')

    args = parser.parse_args()

    if args.mode == 'decode':
        decode_cookie(args.cookie, args.known)
    elif args.mode == 'encode':
        encode_cookie(args.json, args.key)


if __name__ == '__main__':
    main()
