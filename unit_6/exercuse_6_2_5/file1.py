class GreetingCard:
    def __init__(self, recipient="Dana Ev", sender="Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print(f"Sender: {self._sender}")
        print(f"Recipient: {self._recipient}")


if __name__ == "__main__":
    card = GreetingCard()
    card.greeting_msg()