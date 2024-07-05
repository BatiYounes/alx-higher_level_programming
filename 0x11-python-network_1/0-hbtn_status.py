#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        body_content = resp.read()
        print('Body response:')
        print(f'\t- type: {type(body_content)}')
        print(f'\t- content: {body_content}')
        print('\t- utf8 content: {}'.format(body_content.decode('utf-8')))
