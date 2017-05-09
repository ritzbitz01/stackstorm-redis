from st2actions.runners.pythonrunner import Action

import redis


class RedisBaseAction(Action):

    def __init__(self, config):
        super(RedisBaseAction, self).__init__(config)
        self.redis = self._get_client()

    def _get_client(self):
        host = self.config['host']
        port = self.config['port']
        db = self.config['db']

        client = redis.StrictRedis(host=host, port=port, db=db)
        return client
