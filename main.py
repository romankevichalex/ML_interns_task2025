from utils.summarizing import summary_from_text
from utils.file_parsing import parse_docx
import gradio as gr

def parse_file(input_file):
    if input_file.endswith(".txt"):
        return open(input_file).read()
    elif input_file.endswith(".docx"):
        return parse_docx(input_file)
    else:
        return ""

def create_summary(input_text):
    if input_text == "":
        return gr.update(value = "Empty text or wrong file format")
    summary = summary_from_text(input_text)
    return gr.update(value = summary)

with gr.Blocks(title = "Summary app", fill_height = True) as demo:
    with gr.Row():
        input_text = gr.Textbox(label = "Input text", placeholder = "Put your text here")
        input_file = gr.File(label = "Upload .txt or .docx file", file_types = [".txt", ".docx"])
    summary_button = gr.Button("Create a summary")

    summary = gr.Textbox(label = "Summary", placeholder = "...")

    input_file.upload(parse_file, inputs = input_file, outputs = input_text)
    summary_button.click(create_summary, inputs = input_text, outputs = summary)

demo.launch()
