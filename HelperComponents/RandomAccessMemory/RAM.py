#todo: flesh this out

import redis

# Connect to Redis
r = redis.Redis(host='RandomAccessMemory', port=6379)

# Set a key-value pair
r.set('key', 'value')

# Get a value by key
value = r.get('key')
print(value)
