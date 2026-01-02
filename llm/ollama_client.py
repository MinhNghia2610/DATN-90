import subprocess
from config.setting import OLLAMA_MODEL

class OllamaClient:
    def ask(self, prompt):
        result = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL],
            input=prompt,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
