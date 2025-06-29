# Setup

To setup you need to install python dependencies from requirements.txt:
```
pip install -r requirements.txt
```

Put in API_KEY var from `.env` API key to together.ai
```
API_KEY = your_API_key
```

To launch gradio app you need to launch `main.py`:
```
python main.py
```

# Model: deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free

I chose **deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free** because it offers:

- **Free API access**, suitable for budget-friendly projects.
- **Lightweight distillation** of Llama-70B, reducing resource usage while keeping strong performance.

# How the Application Works

This app uses **Gradio** to provide a graphical interface for text input and output.

For summarization, it relies on the **deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free** model.

Key features of the workflow:

- Supports direct text input and uploading **.txt** and **.docx** files.
- If the input text exceeds the model's token limit, the app:
  - Splits the text into smaller chunks.
  - Summarizes each chunk separately.
  - Combines these chunk summaries into one text.
  - Summarizes this combined text again to produce the final summary.

This chunking and recursive summarization approach enables efficient handling of very long texts while maintaining summary quality.
