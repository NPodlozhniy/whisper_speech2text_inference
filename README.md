
## Description

Simple inference of [Whisper AI](https://github.com/openai/whisper) speech-2-text model for non-technical users.
Run the program as usual with double click instead of writing specific scripts in Command Line Interface.

All you need is just to provide a path to an audio file (full or local if it's in the folder where you run `.exe`) and receive a transcript in the same folder next to the audio file in a few minutes.
In addition to Latin, Cyrillic alphabet is supported.

### Prerequisites

You supposed to have two programs installed in your system

1. Python >= 3.10 (download from [python.org](https://www.python.org/downloads/)
2. ffmpeg >= 7.1 (download from [ffmpeg.org](https://ffmpeg.org/download.html#build-windows)

You may check it the programs are installed properly with `python --version` and `ffmpeg -version` commands accordingly

### Quick Start

Start transcribing audio in a few minutes following these steps

1. Clone this repository to your local computer and navigate to the folder
2. Install the dependencies with `pip install -r requirements.txt`
3. Compile the Python code to an executable file with `pyinstaller --onefile --collect-data=whisper transcript.py`
4. This command creates two new folders, `transcript.exe` file in the `dist` directory is what you need
5. Make a shortcut for `.exe` file and use it like a regular app from the desktop - done!
