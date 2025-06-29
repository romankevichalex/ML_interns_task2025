from together import Together
from dotenv import dotenv_values

MAX_TOTAL_TOKENS = 8193
MAX_NEW_TOKENS = 2048

def approximate_token_count(text):
    return len(text)/4

def deepseek_req(system_prompt, prompt):

    client = Together(api_key=dotenv_values(".env")["API_KEY"])

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
        messages=[
        {
            "role": "user",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": prompt
        }
        ],
        stream = True
    )
    output = ""

    for batch in response:
        current_batch = batch.choices[0].delta.content
        output += current_batch
        print(current_batch, end = "", flush=True)
    print()
    output = output.split("</think>")
    output = output[-1].lstrip()
    return output


def split_text_into_chunks(text, max_chunk_size):
    words = text.split()
    chunks = []
    current_chunk = []

    current_length = 0
    for word in words:
        if current_length + len(word) + 1 > max_chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word) + 1
        else:
            current_chunk.append(word)
            current_length += len(word) + 1

    if current_chunk:
        chunks.append(" ".join(current_chunk))
        
    return chunks

def summarize_chunks(chunks):
    summaries = []
    for i, chunk in enumerate(chunks):
        print(f"Summarizing chunk {i+1}/{len(chunks)}:")
        summary = summary_from_text(chunk)
        summaries.append(summary)
    return summaries




def summary_from_text(input_text):
    system_prompt = open("utils/system_prompt.txt").read()
    prompt = input_text
    if approximate_token_count(system_prompt) + approximate_token_count(prompt) > 0.8*MAX_TOTAL_TOKENS:
        chunks = split_text_into_chunks(prompt, max_chunk_size = 8000)
        chunk_summaries = summarize_chunks(chunks)
        system_prompt_for_chunk_summarization = open("utils/system_prompt_for_chunks.txt").read()
        summary = deepseek_req(system_prompt_for_chunk_summarization, "\n\n".join(chunk_summaries))
    else:
        summary = deepseek_req(system_prompt, prompt + "\n<think>")
    return summary