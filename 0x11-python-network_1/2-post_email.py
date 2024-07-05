#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)"""
if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request

    get_email = {"email": sys.argv[2]}
    email_encode = urllib.parse.urlencode(get_email).encode("ascii")
    urlrequest = urllib.request.Request(sys.argv[1], email_encode)
    with urllib.request.urlopen(urlrequest) as response:
        print(response.read().decode("utf-8"))
