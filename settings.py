SEARCH_KEY = "AIzaSyDa799Q-mHzU-azKwRciKQnU4_0spYEfzs"
SEARCH_ID = "93dfb7c5347ee4ddb"
COUNTRY = "INDIA"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT = 20

import os
if os.path.exists("private.py"):
    from private import *