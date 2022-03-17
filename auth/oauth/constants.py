import os
import urllib.parse


CLIENT_SECRET = 'F2cf0dV9QjrSEj2XRUiNYvQ3A30Ar3wG'
CLIENT_ID = '51bWuca2XQWNa18fLbWmZrGt3M3NvRTX'
REDIRECT_URI = urllib.parse.quote_plus("http://localhost:8000/auth/get-token")
STATE = "random_string"