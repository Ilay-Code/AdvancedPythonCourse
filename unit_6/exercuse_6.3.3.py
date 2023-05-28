import pyttsx3

def read_aloud(text):
    # Create a Text-to-speech engine
    engine = pyttsx3.init()

    # Set the rate of speech (optional)
    engine.setProperty('rate', 150)

    # Set the volume level (optional)
    engine.setProperty('volume', 1.0)

    engine.say(text)
    engine.runAndWait()


def main():
    sentence = "first time i'm using a package in next.py course"
    read_aloud(sentence)


if __name__ == '__main__':
    main()
