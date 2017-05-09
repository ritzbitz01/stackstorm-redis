from lib import action

class RedisSetAction(action.RedisBaseAction):
    def run(self, key, value):
        return self.redis.set(key, value)
