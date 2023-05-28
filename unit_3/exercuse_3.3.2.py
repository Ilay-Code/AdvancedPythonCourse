class UnderAge(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"Your age ({self.age}) is less than 18. In {18-self.age} years, you'll be able to reach Ido's birthday."


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


def main():
    send_invitation("John", 17)
    send_invitation("Sarah", 20)


if __name__ == "__main__":
    main()