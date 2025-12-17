import ollama

def ask_ollama(prompt):
    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": "Bạn là một AI quản gia nói tiếng Việt, lịch sự, ngắn gọn."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response["message"]["content"]
