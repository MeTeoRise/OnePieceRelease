import argparse
import sys
from release_exporter import download_chapter_spoilers, get_latest_chapter
from setup import setup_reddit

function_list=['download-chapter-spoilers']

if __name__ == "__main__": 
    reddit = setup_reddit()

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--function', type=str, help="This function downloads chapter spoilers from the range specified", required=True)
    parser.add_argument('--start-chapter', type=int, default=1027)
    parser.add_argument('--end-chapter', type=int, default=get_latest_chapter())

    args = parser.parse_args()

    match args.function:
        case 'download-chapter-spoilers':
            download_chapter_spoilers(args.start_chapter, args.end_chapter)
        case other:
            print('Invalid function. Functions available:')
            for idx, f in enumerate(function_list, start=1):
                print(f"{idx}. {f}")
    