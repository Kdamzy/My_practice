"""A script that genrate a love message using the name of the person you love"""
class Love:
    def __init__(self):
        """Initialise self"""
        self.user_name =""
        self.name = ""
        self.feelings = ""

    def user_input(self):
        """prompt user to enter name and how they really feel"""
        self.user_name = input("Enter your name: ")
        self.name = input("Enter the name of the person you love: ")
        self.feelings = input("How do you truly feel about {}? ".format(self.name))

    def generate_message(self):
        message = "Dear {},\nI  just wanted to let you know that {}.\n\nWith love,\n[Your Name]".format(
            self.name, self.feelings, self.user_name)
        return message

if __name__ == "__main__":
    letter_generator = Love()
    letter_generator.user_input()
    generated_message = letter_generator.generate_message()

    print("\nLove Message:\n")
    print(generated_message)
