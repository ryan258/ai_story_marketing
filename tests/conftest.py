# 📁 File: ai_story_marketing/tests/conftest.py

# 🧰 This is our special toolbox for pytest! 🔧
# It helps pytest find and run our tests correctly.

import sys
import os

# 🗺️ Add the project root directory to the Python path
# This is like giving pytest a map to find all our cool code!
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# 🎉 That's it! Now pytest knows where to look for our awesome code!
# We don't need to add any test functions here. They go in our test files.