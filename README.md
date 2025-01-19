# DDRDLE

DDRDLE is Wordle but for DDR players, for now based on the song jacket.

## Prerequisites
- Ensure that you have Python3 & pip installed as this project requires flask
- Ensure that you have Docker installed
- The static/images folder assumes that you have the song jackets installed to the linked location. Adjust this Symbolic Link accordingly. 
  - The file naming convention for the song jackets "songname-jacket.png"
  - The file naming convention for the song jackets "songname-song.ogg"

## Installation

To get started with DDRDLE, follow these steps:

1. Clone the repository:
  ```bash
  git clone https://github.com/sh1ggy/ddrdle.git
  ```
2. Navigate to the project directory:
  ```bash
  cd ddrdle
  ```
3. Install the dependencies:
  ```bash
  pip install ./requirements.txt
  ```

## Usage

To start the game, run the following command:
```bash
python app.py
```

## Building
- Given that you have all the statically downloaded files, place the audio and image files in `./static/audio` and `./static/images` respectively
- Once that's done run the Docker instance via `docker-compose up -d`

## Notes
- Due to a lack of storage space on the server, we are using volumes instead of having a Docker image that contains all the static content.
  - In order to go back to the ideal, simply remove all the `UNIDEAL` commented lines in the Docker configs

## Contact

For any questions or feedback, please reach out to me at [tyronewessnolasco@gmail.com](mailto:tyronewessnolasco@gmail.com) or on Twitter 
