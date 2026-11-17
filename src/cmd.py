import os, subprocess
from pathlib import Path
from dotenv import load_dotenv


# Load enviroment variables
load_dotenv()

# Target project root path
root_path = Path(f'{os.environ.get("TARGET_ROOT_PATH")}').absolute()

def run_git_cmd(cmd: str | list) -> subprocess.CompletedProcess:
  """
  Run git command into shell and return the output
  Args:
    cmd (str | list): git command to run
  """

  # handle command format
  if type(cmd) == str: cmd = cmd.split(" ")

  # Try run command
  try:
    cmdResult = subprocess.run(
      cmd, 
      cwd=root_path,
      check=True, 
      capture_output=True, 
      text=True
    )

  except subprocess.CalledProcessError as err:
    print("Erro de exeução:", cmd)
    print("Código de erro:", err.returncode)
    print("Mensagem:", err.stderr)

  # Check if successful
  return cmdResult