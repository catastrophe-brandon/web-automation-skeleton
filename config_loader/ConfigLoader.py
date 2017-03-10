import yaml


class ConfigLoader(object):

    def __init__(self):
        self.config = None
        self.reason = None

    def load_config(self):
        if not self.config:
            with open('config.yaml', 'r') as f:
                self.config = yaml.load(f)
                if not self.validate_config(self.config):
                    self.config = None
                    self.reason = "Configuration did not pass validation"
                    print("Configuration loading failed because {}".format(self.reason))
        else:
            print('Config already loaded!')

    def validate_config(self, config):
        # TODO: validate config
        return True

    def get_config(self):
        if self.config is None:
            self.load_config()
        return self.config


