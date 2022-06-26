# OnePieceRelease
One Piece Release checker based on Reddit

To set up the script you need: 

1. Install requirements:
`pip install -r requirements.txt`
2. Get Reddit ID and Secret ([G4Gs guide](https://www.geeksforgeeks.org/how-to-get-client_id-and-client_secret-for-python-reddit-api-registration/))
3. Copy .env.example to .env and fill with Client ID and Secret:
`cp .env.example .env`
4. Run `onepiece.py`:
`python3 onepiece.py -f get-latest-chapter`

Supported Functions:

* *download-chapter-spoilers*
* *get-latest-chapter*
* *get-latest-episode*
* *get-latest-spoiler*