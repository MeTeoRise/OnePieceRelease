from setup import setup_reddit
import os


reddit = setup_reddit()

directory = "{0}/chapters".format(os.path.dirname(os.path.realpath(__file__)))
if not os.path.isdir(directory):
    os.makedirs(directory)


for chapter in range(1040, 1051):
    for idx, submission in enumerate(reddit.subreddit("OnePiece").search("One Piece chapter {0} spoilers".format(chapter), limit=2)):
        if submission.title == "One Piece chapter {0} spoilers".format(chapter):
            os.chdir(directory)
            filename = "{0}.md".format(chapter)
            if not os.path.exists(filename):
                f = open(filename, "a")
                f.write(submission.selftext)
                f.close()
