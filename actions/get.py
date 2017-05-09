from lib import action

class RedisGetAction(action.RedisBaseAction):
    def run(self, key):
        return self.redis.get(key)
