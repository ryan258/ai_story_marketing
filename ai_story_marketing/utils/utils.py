# 📁 File: ai_story_marketing/ai_story_marketing/utils/utils.py

# 🛠️ Welcome to our utility belt! 🦸‍♂️
# This is where we keep all our cool tools for error handling and logging!

import logging  # This helps us keep track of what's happening in our app
from functools import wraps  # This helps us create cool decorator functions

# 📝 Let's set up our logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 🎭 This is our star player: the error handler!
def handle_errors(func):
    """
    🦸‍♂️ This is like a superhero cape for our functions!
    It catches any errors and helps us deal with them smoothly.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # 🚨 Uh-oh, something went wrong! Let's log it and return a friendly message.
            logger.error(f"An error occurred in {func.__name__}: {str(e)}")
            return {"error": "Oops! Something went wrong. Our AI agents are taking a quick nap. Please try again later!"}
    return wrapper

# 🏋️‍♂️ This function helps us log how long things take
def log_execution_time(func):
    """
    ⏱️ This is like a stopwatch for our functions!
    It tells us how long each part of our app takes to run.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute")
        return result
    return wrapper

# 🧪 Let's test our cool new tools!
def test_error_handling():
    @handle_errors
    def problematic_function():
        raise ValueError("Oops, I did it again!")

    result = problematic_function()
    assert "error" in result, "Error handling should return an error message"

def test_execution_time_logging():
    @log_execution_time
    def slow_function():
        import time
        time.sleep(1)

    slow_function()
    # Check your logs to see if the execution time was logged!

# 🎉 Hooray! We've created some awesome tools to help our app run smoothly!
# Now we can handle errors like pros and keep track of how fast our app is running! 🚀