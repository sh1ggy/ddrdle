# DDRDLE

DDRDLE is Wordle but for DDR players

## Prerequisites
- Ensure that you have Python3 & pip installed as this project requires flask
- Ensure that you have Docker installed
- The static/images folder assumes that you have the song jackets installed to the linked location. Adjust this Symbolic Link accordingly, alternatively, copy the files directly to the corresponding audio & images folder in /static. 
  - The file naming convention for the song jackets "songname-jacket.png"
  - The file naming convention for the song jackets "songname-song.mp3", ensure you convert .ogg files to .mp3

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
- Due to a lack of storage space on the hosting server, we are using volumes instead of having a Docker image that contains all the static content.
  - In order to go back to the ideal, simply remove all the `UNIDEAL` commented lines in the Docker configs

## Contact

For any questions or feedback, please reach out to me on Twtitter @ [AU_SHIGGY](https://x.com/au_shiggy)


## Credits
- This project uses the build files generated from [xiexingwu](https://github.com/xiexingwu)'s [DDR-BPM-Preprocess](https://github.com/xiexingwu/DDR-BPM-prep) repository, adjusted so that .ogg files would also be unzipped. 
- Credits to the Brisbane DDR community for helping with feedback during development.

### Collaborators

[<img src="https://github.com/propablo.png" width="60px;"/><br /><sub>ProPablo</sub>](https://github.com/propablo) |
 ------------------------------------------------------------------------------------------------------------------ |
