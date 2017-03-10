import requests
import json
import sys


class Slacker(object):

    def post_message(self, webhook_url, message):

        message_body = {
            'text': message
        }

        response = requests.post(webhook_url, data=json.dumps(message_body))
        if not response.status_code == 200:
            print('Failed to post to slack, status code was {}'.format(response.status_code))

    def build_message(self, success_flag, num_successful, num_failed, execution_time):
        """ Builds a simple reporting message to be dropped into Slack """
        # TODO
        return ''







