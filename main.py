import unittest
import Slacker
from config_loader.ConfigLoader import ConfigLoader

if __name__ == '__main__':
    print('Running an example test')
    result = unittest.main('tests.ExampleTest').result

    webhook_url = ConfigLoader().get_config()['slack_webhook_url']
    slacker = Slacker.main(webhook_url, 'Slacker module appears to be functional')

