from redis import Redis
from rq import Queue
from dotenv import load_dotenv
import os

# ============================================================
# 1. Load environment variables from .env file
# ============================================================

queue = Queue(connection=Redis(
        host="localhost",
        port="6379"
    
))

queue.enqueue_call(process_query)

