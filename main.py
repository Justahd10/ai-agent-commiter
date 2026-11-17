from src.cmd import run_git_cmd


# Run git commands into shell
print("Executando comandos do git e salvando informações...\n\n")

commits_count = "10"

status = run_git_cmd("git status")

diff = run_git_cmd("git diff")

diff_stat = run_git_cmd("git diff --stat")

log_details = run_git_cmd(f"git log -n {commits_count} -p")

log_stat = run_git_cmd(f"git log -n {commits_count} --stat")

print("Execução de comandos terminada.\n\n")

# Request to ai agent