#!/usr/local/bin/python3

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Word, line, character, and byte count")
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-c', '--bytes', action='store_true', help='Print the byte count')
    parser.add_argument('-l', '--lines', action='store_true', help='Print the line count')
    parser.add_argument('-w', '--words', action='store_true', help='Print the word count')
    parser.add_argument('-m', '--characters', action='store_true', help='Print the character count')

    args = parser.parse_args()
    file_content = args.file.read()

    if not any([args.bytes, args.lines, args.words, args.characters]):
        args.bytes = args.lines = args.words = True #default

    if args.bytes:
        byte_count = len(file_content)
        print(f'{byte_count:8} {args.file.name}')

    if args.lines:
        line_count = len(file_content.splitlines())
        print(f'{line_count:8} {args.file.name}')

    if args.words:
        word_count = len(file_content.split())
        print(f'{word_count:8} {args.file.name}')

    if args.characters:
        char_count = len(file_content.replace('\n', '').replace(' ', ''))
        print(f'{char_count:8} {args.file.name}')

if __name__ == "__main__":
    main()
