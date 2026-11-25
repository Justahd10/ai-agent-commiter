import os, subprocess
from typing import TypedDict
from pathlib import Path
from dotenv import load_dotenv


# Load enviroment variables
load_dotenv()

git_cmds = [
  ('Arquivos modificados', ["git", "status"]),
  ('Linhas adicionadas e removidas', ["git", "diff"]),
  ('Resumo de alterações pendentes', ["git", "diff", "--stat"]),
  (f'Últimos 10 commits', ["git", "log", "-n", "10", "-p"]),
  ("Resumo de histórico", ["git", "log", "-n", "10", "--stat"])
]

class Commit(TypedDict):
  total_files: int
  files: list[str]
  message: str

def run_git_cmd(cmd: list[str]) -> subprocess.CompletedProcess:
  """
  Run git command into shell and return the output
  Args:
    cmd (str | list): git command to run
  """
  # Try run command
  cmdResult = subprocess.run(
    cmd, cwd=os.environ.get("TARGET_ROOT_PATH"), check=True, 
    capture_output=True, text=True
  )

  # Check if successful
  return cmdResult

def get_projects_changes() -> list[subprocess.CompletedProcess]: 
  """
  Get the content of all git commands
  Returns:
    str: text with git content
  """
  # Start git content
  git_content = ""

  # Append data into content
  for item in git_cmds:
    result = run_git_cmd(item[1])

    git_content = git_content + f"{item[0]}:\n {result.stdout}\n\n"

  return git_content

def save_project_changes(commits: list[Commit]):
  """
  Save project changes into git repository
  Args:
    commits (list[Commit]): list of commits to save
  """
  for commit in commits:
    print(f"Processando: {commit['total_files']} arquivos...")

    # Add files
    for f in commit['files']:
      print(f"Adicionando arquivo {f}...")
      run_git_cmd(f"git add {Path(f).absolute()}")

    # Commit changes
    print("Realizando commit...")
    run_git_cmd(f'git commit -m "{commit['message']}"')