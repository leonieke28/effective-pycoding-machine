import os
import urllib.request
from collections import Counter

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, "feed")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/feed", tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
    data already loaded into the content variable"""
    categories = content.split("<category>")[1:]
    tags = [cat.split("</category>")[0] for cat in categories]
    counter = Counter(tags)
    return counter.most_common(n)
