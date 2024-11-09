import os
import time
import warnings

import whisper

warnings.filterwarnings("ignore")


def whisper_transcribe(audio_file_path: str) -> None:

    start_time = time.time()

    model = whisper.load_model("turbo")
    result = model.transcribe(audio_file_path)

    with open(
        os.path.splitext(audio_file_path)[0] + "_transcribed.txt",
        mode="w",
        encoding="utf-8",
    ) as file:
        file.write(result["text"])

    print(
        "--- Successful transcription in %.0f seconds ---" % (time.time() - start_time)
    )
    return


if __name__ == "__main__":
    path = input(
        r"Please enter the path to an audio file (format options: mp3, mp4, mpeg, mpga, m4a, wav, or webm.):"
    )
    # makes Windows paths Unix compatible
    # if the path is local makes os.path.join(os.getcwd(), path)
    normalized_windows_path = os.path.abspath(path.strip(' "'))
    try:
        if not os.path.exists(normalized_windows_path):
            print("Error: File is not found. Check that you entered the right path.")
        else:
            whisper_transcribe(audio_file_path=normalized_windows_path)
    except Exception as error:
        print("An error in transcription process happened:", error)
    finally:
        _ = input("Press any button to exit.")
