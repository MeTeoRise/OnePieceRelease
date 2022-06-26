import argparse
import sys
from release_exporter import (
    download_chapter_spoilers,
    get_latest_chapter,
    get_latest_episode,
    get_latest_spoiler,
)
from setup import setup_reddit

function_list = [
    "download-chapter-spoilers",
    "get-latest-chapter",
    "get-latest-episode",
    "get-latest-spoiler",
]

if __name__ == "__main__":
    reddit = setup_reddit()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--function",
        type=str,
        help="This is a selector of function you would like to call",
        required=True,
    )
    parser.add_argument("--start-chapter", type=int, default=1027)
    parser.add_argument("--end-chapter", type=int, default=get_latest_chapter())

    args = parser.parse_args()

    match args.function:
        case "download-chapter-spoilers":
            download_chapter_spoilers(args.start_chapter, args.end_chapter)
        case "get-latest-chapter":
            latest_chapter = get_latest_chapter()
            print(f"Latest Chapter is: {latest_chapter}")
        case "get-latest-episode":
            latest_episode = get_latest_episode()
            print(f"Latest Episode is: {latest_episode}")
        case "get-latest-spoiler":
            latest_spoiler = get_latest_spoiler()
            if latest_spoiler:
                print(latest_spoiler)
            else:
                print("There is no new spoiler available")
        case other:
            print("Invalid function. Functions available:")
            for idx, f in enumerate(function_list, start=1):
                print(f"{idx}. {f}")
