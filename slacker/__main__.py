from slacker.slacker import Slacker
import sys


def __main__(webhook_url, message):
    Slacker().post_message(webhook_url, message)

if __name__ == "__main__":

    if not len(sys.argv) == 3:
        print('You did not supply the correct information, try again.')
        exit(1)

    # Get the webhook URL from first argument
    webhook_url = sys.argv[1]
    print('Using webhook {}'.format(webhook_url))

    # pull the message from the command-line
    message = sys.argv[2]
    print('Sending message {}'.format(message))

    __main__(webhook_url, message)
