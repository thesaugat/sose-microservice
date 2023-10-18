import re


class Utils:
    @staticmethod
    def validate(password):
        while True:
            if len(password) < 8:
                return "Make sure your password is at lest 8 letters", False
                # return False
            elif re.search('[0-9]', password) is None:
                return "Make sure your password has a number in it", False
                # return False

            elif re.search('[A-Z]', password) is None:
                return "Make sure your password has a capital letter in it", False
                # return False

            else:
                return 1
