import os
START_COMMENT = "<!--START_SECTION:badges-->"
END_COMMENT = "<!--END_SECTION:badges-->"
REPOSITORY = os.getenv("INPUT_REPOSITORY")
GH_TOKEN = os.getenv("INPUT_GH_TOKEN")
COMMIT_MESSAGE = os.getenv("INPUT_COMMIT_MESSAGE")
CREDLY_USER = os.getenv("INPUT_CREDLY_USER")
CREDLY_SORT = os.getenv("INPUT_CREDLY_SORT")

BADGE_SIZE = os.getenv("INPUT_BADGE_SIZE", '110')
try:
    NUMBER_LAST_BADGES = int(os.getenv("INPUT_NUMBER_LAST_BADGES"))
except:
    NUMBER_LAST_BADGES = 0

CREDLY_BASE_URL= "http://www.credly.com"

LIST_REGEX = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"
