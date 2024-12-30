# Example prompt for an LLM
DEFAULT_PROMPT = "Please process the following data: {data}"

def generate_prompt(data):
    return DEFAULT_PROMPT.format(data=data)