openai_api_key = "replace here"
output_ppt_file = "output/output.pptx"
endpoint = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}