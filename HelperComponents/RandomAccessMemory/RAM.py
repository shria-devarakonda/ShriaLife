#todo: flesh this out

import redis as RAMTool

class RAMConnector:
    instance = None
    redis_connection = None
    
    def __init__(self):
        if self.instance:
            raise Exception("use RAMConnector.create()")
        RAMConnector.instance = self
        self.RAM_connection = self.create_connection()
        
    def create(self):
        if not RAMConnector.instance:
            RAMConnector.instance = RAMConnector()
        return RAMConnector.instance
    
    def create_connection(self):
        RAM_connection = RAMTool.Redis(host='RandomAccessMemory', port=6379)
        return RAM_connection

    def set_ram(self, kv):
        RAM_conn = self.RAM_connection
        RAM_conn.set('key', 'value')

    def get_ram(self, key):
        RAM_conn = self.RAM_connection
        value = RAM_conn.get(key)
        print(f"The value of {key} is {value}")
        return value

    def event(self, key, val):
        from datetime import datetime
        RAM_CONN = self.RAM_connection
        val = f"{val} at {datetime.now()}"
        RAM_CONN.lpush(key, val)