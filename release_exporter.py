from reddit import setup_reddit
import os


reddit = setup_reddit()

default_chapter_directory = "{0}/chapters".format(
    os.path.dirname(os.path.realpath(__file__))
)
if not os.path.isdir(default_chapter_directory):
    os.makedirs(default_chapter_directory)


def download_chapter_spoilers(start_chapter: int, end_chapter: int):
    """This is a function to download spoiler of chapters and write them as markdown in default_chapter_directory

    Args:
        start_chapter (int): start chapter you want to download
        end_chapter (int): last chapter you want to download
    """
    for chapter in range(start_chapter, end_chapter + 1):
        for idx, submission in enumerate(
            reddit.subreddit("OnePiece").search(
                "One Piece chapter {0} spoilers".format(chapter), limit=2
            )
        ):
            if submission.title == "One Piece chapter {0} spoilers".format(chapter):
                os.chdir(default_chapter_directory)
                filename = "{0}.md".format(chapter)
                if not os.path.exists(filename):
                    f = open(filename, "a")
                    f.write(submission.selftext)
                    f.close()


def get_latest_chapter() -> int:
    """Get last One Piece chapter released

    Returns:
        latest_chapter (int): last chapter available
    """

    submissions = list(
        reddit.subreddit("OnePiece").search('flair: "Current Chapter"', limit=1)
    )
    chapter_title = submissions[0].title

    latest_chapter = int(chapter_title.split()[-1])
    return latest_chapter


def get_latest_episode() -> int:
    """Get last One Piece episode released

    Returns:
        latest_episode (int): last episode available
    """

    submissions = list(
        reddit.subreddit("OnePiece").search('flair: "Current Episode"', limit=1)
    )
    episode_title = submissions[0].title

    latest_episode = int(episode_title.split()[-1])
    return latest_episode


def get_latest_spoiler() -> str:
    """Get last One Piece spoiler

    Arguments:
        latest_chapter (int): last chapter available
    """

    latest_chapter = get_latest_chapter()
    latest_spoiler = latest_chapter + 1
    submissions = list(
        reddit.subreddit("OnePiece").search(
            "One Piece chapter {0} spoilers".format(latest_spoiler), limit=2
        )
    )
    for submission in submissions:
        if submission.title == "One Piece chapter {0} spoilers".format(latest_spoiler):
            latest_spoiler = submission.selftext
            break
    else:
        latest_spoiler = ""

    return latest_spoiler


if __name__ == "__main__":
    latest_episode = get_latest_spoiler()
    print(latest_episode)
