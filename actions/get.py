from lib import action

class RedisGetAction(action.RedisBaseAction):
    def run(self, key, value):
        return self.redis.get(key)
