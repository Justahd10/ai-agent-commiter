import os, requests
from dotenv import load_dotenv


# Load enviroment variables
load_dotenv()

def request_ai_commiter(system_msg: str, git_content: str) -> None | dict:
  response = requests.post(
    os.environ.get("WEBHOOK_URL"), 
    json={
      'project': os.environ.get("TARGET_ROOT_PATH"),
      'git_content': git_content,
      'system_message': system_msg
    }, 
    headers={ 'Content-Type': "application/json" }
  )

  return response.json()