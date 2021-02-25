import logging
from datetime import datetime, timezone

from google.cloud import speech_v1p1beta1 as speech

EXTENSION = "mp3"
AUDIO_OUTPUT_DIR = "resources"


async def check_health():
    try:
        client = speech.SpeechClient()
        logging.info("GCP Speech To Text is reachable")
        return {
            "health": 'green'
        }
    except Exception as e:
        logging.error("GCP Speech To Text is unreachable")
        return {
            "health": "red",
            "exception": e
        }


async def apply_speech_to_text(audio):
    logging.info(f"Type of data: {type(audio)}")
    file_name = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    content = await audio.read()

    # Create a speech client object
    client = speech.SpeechClient()

    # Set audio and config
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=44100,
        language_code="en-IN",
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))

    return {
        "transcript": response.results[0].alternatives[0].transcript,
        "confidence": response.results[0].alternatives[0].confidence
    }
