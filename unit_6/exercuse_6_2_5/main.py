from unit_6.exercuse_6_2_5.file1 import GreetingCard
from unit_6.exercuse_6_2_5.file2 import BirthdayCard


if __name__ == "__main__":
    birthday_card = BirthdayCard(recipient="Ilay", sender="Itay", sender_age=19)
    greeting_card = GreetingCard(recipient="Bobi", sender="Dor")

    birthday_card.greeting_msg()
    greeting_card.greeting_msg()