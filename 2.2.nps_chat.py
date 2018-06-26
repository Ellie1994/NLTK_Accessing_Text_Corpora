# There is also a corpus of instant messaging chat sessions, originally collected by the Naval Postgraduate School. The corpus contains over 10,000 posts, anonymized by replacing usernames with generic names of the form "UserNNN". The corpus is organized into 15 files, where each file contains several hundred posts collected on a given date, for an age-specific chatroom (teens, 20s, 30s, 40s, plus a generic adults chatroom). 
# The filename contains the date, chatroom, and number of posts; e.g., 10-19-20s_706posts.xml contains 706 posts gathered from the 20s chat room on 10/19/2006.

import nltk
from nltk.corpus import nps_chat
chatroom = nps_chat.posts("10-19-20s_706posts.xml")

print(chatroom[123])
