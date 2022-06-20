from setup import setup_reddit
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
    chapter = 1053
    submissons = list(
        reddit.subreddit("OnePiece").search('flair: "Current Chapter"', limit=1)
    )
    chapter_title = submissons[0].title

    latest_chapter = int(chapter_title.split()[-1])
    return latest_chapter


# if __name__ == "__main__":
#     latest_chapter = get_latest_chapter()
#     print(latest_chapter)
