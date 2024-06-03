import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
# Used to securely store your API key
from google.colab import userdata


# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=userdata.get('AIzaSyB3sbXgu5aIFRWgT3hCYTQjnP7D_Vrq1PM')

genai.configure(api_key=GOOGLE_API_KEY)

