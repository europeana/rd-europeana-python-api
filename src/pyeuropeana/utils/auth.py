import os

def get_api_key():
  API_KEY = os.environ.get('EUROPEANA_API_KEY')
  if not API_KEY:
    message = """
    EUROPEANA_API_KEY not set. Set EUROPEANA_API_KEY as an environment variable running 'export EUROPEANA_API_KEY=yourapikey' in the terminal.
    If running in Google Colab use os.environ['EUROPEANA_API_KEY'] = 'yourapikey'
    """
    raise Exception(message)
  return API_KEY