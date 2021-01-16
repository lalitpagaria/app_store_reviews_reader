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
