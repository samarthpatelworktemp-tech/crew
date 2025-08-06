# tools/markdown_saver.py

import os
from typing import Annotated
from pydantic import BaseModel
from crewai.tools import BaseTool

class MarkdownSaverInput(BaseModel):
    content: Annotated[str, "Markdown content to save"]
    title: Annotated[str, "title without extension"]

class MarkdownSaverTool(BaseTool):
    name: str = "MarkdownSaver"
    description: str = "Saves markdown content to a specified folder as a .md file"
    args_schema: type[MarkdownSaverInput] = MarkdownSaverInput
    output_folder: str = "output_docs"

    def _run(self, content: str, title: str) -> str:
        os.makedirs(self.output_folder, exist_ok=True)
        file_path = os.path.join(self.output_folder, f"{title}.md")

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return f"✅ File saved at: `{file_path}`"
        except Exception as e:
            return f"❌ Failed to save file: {str(e)}"
