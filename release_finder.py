from setup import setup_reddit

reddit = setup_reddit()


for chapter in range(1040, 1049):
    for idx, submission in enumerate(reddit.subreddit("OnePiece").search("One Piece chapter {0} spoilers".format(chapter), limit=1)):
        print(submission.title)
        print(submission.score)
        print(submission.author)
