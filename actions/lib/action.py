from st2actions.runners.pythonrunner import Action

import redis


class RedisBaseAction(Action):

    def __init__(self, config):
        super(RedisBaseAction, self).__init__(config)
        self.redis = self._get_client()

    def _get_client(self):
        hostConfig = self.config['host']
        portConfig = self.config['port']
        dbConfig = self.config['db']

        client = redis.StrictRedis(host=hostConfig, port=portConfig, db=dbConfig)
        return client
