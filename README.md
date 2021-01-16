<p align="center">
    <a href="https://github.com/lalitpagaria/app_store_reviews_reader/blob/master/LICENSE">
        <img alt="License" src="https://img.shields.io/github/license/lalitpagaria/app_store_reviews_reader?color=blue">
    </a>
    <a href="https://pypi.org/project/app-store-reviews-reader">
        <img src="https://img.shields.io/pypi/pyversions/app-store-reviews-reader" alt="PyPI - Python Version" />
    </a>
    <a href="https://pypi.org/project/app-store-reviews-reader/">
        <img alt="Release" src="https://img.shields.io/pypi/v/app-store-reviews-reader">
    </a>
    <a href="https://pepy.tech/project/app-store-reviews-reader">
        <img src="https://pepy.tech/badge/app-store-reviews-reader/month" alt="Downloads" />
    </a>
    <a href="https://github.com/lalitpagaria/app_store_reviews_reader/commits/master">
        <img alt="Last commit" src="https://img.shields.io/github/last-commit/lalitpagaria/app_store_reviews_reader">
    </a>
</p>

# App store reviews reader
To fetch app store reviews from publicly available RSS feeds.

App store provide RSS feed as follows -
```shell
https://itunes.apple.com/{country}/rss/customerreviews/id={app_id}/xml
```
It provide feed in `xml` and `json` format but `xml` feed have more information like `review_id` and `vote_count` etc. Hence `xml` feed is used along with `feedparser` to parse feed.

## Installation

Install via PyPi:
```shell
pip install app-store-reviews-reader
```
Install from master branch (if you want to try the latest features):
```shell
git clone https://github.com/lalitpagaria/app_store_reviews_reader
cd app_store_reviews_reader
pip install --editable .
```

# How to use
`AppStoreReviewsReader` require two parameters `app_id` and `country`. `app_id`  can be found at the end of the url of app in app store. For example -
```shell
https://apps.apple.com/us/app/xcode/id497799835
```
`310633997` is the `app_id` for xcode and `us` is country.

Now you can run the following [example](https://github.com/lalitpagaria/app_store_reviews_reader/tree/master/example) -
```python
import pprint
from datetime import datetime, timedelta

import pytz as pytz

from app_store.app_store_reviews_reader import AppStoreReviewsReader

# app_id, and country of xcode
reader = AppStoreReviewsReader(
    app_id="497799835",
    country="us"
)

# To fetch reviews entered in past 5 days
since_time = datetime.utcnow().astimezone(pytz.utc) + timedelta(days=-5)

# fetch_reviews will fetch all reviews if not parameters are passed.
# If `after` is passed then it will fetch all reviews after this date
# If `since_id` is passed then it will fetch all reviews after this review_id
reviews = reader.fetch_reviews(
    after=since_time
)

pp = pprint.PrettyPrinter(indent=4)
for review in reviews:
    pp.pprint(review.__dict__)

```
Review contains following information -
```python
@dataclass
class Review:
    version: str
    rating: int
    id: int
    title: str
    content: str
    date: datetime
    author_link: str
    author_name: str
    country: str
    vote_count: Optional[int] = 0
    vote_sum: Optional[int] = 0
```

