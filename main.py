from pathlib import Path
from src.cmd import (
  run_git_cmd,
  get_projects_changes,
  save_project_changes
)
from src.api import request_ai_commiter


# Run git commands into shell
print("Inspecionando e gravando alterações...")
git_content = get_projects_changes()

# Get content from system message text file
print("Gravando system message do agente de ia...")
fp = Path(__file__).parent / "src" /"system_message.txt"

with open(fp, "r", encoding="utf-8") as file:
  system_message = file.read()

# Request to ai agent
print("Enviando requisição ao agente de ia...")
data = request_ai_commiter(system_message, git_content)

# Save changes
print("Salvando alterações...")
if data['status'] == "successful":
  commits = data['payload']['output']['commits']

  save_project_changes(commits)

else: print("Formato de resposta inesperado:\n", data)

# Sent to git hub
run_git_cmd("git push origin main")
print("Alterações enviadas.")