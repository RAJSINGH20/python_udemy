from dotenv import load_dotenv
import os
import json
from openai import OpenAI
import subprocess


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def run_command(cmd: str):
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        return result.stdout + result.stderr

    except Exception as e:
        return str(e)


def writeFile(filename: str, content: str):
    try:
        parent = os.path.dirname(filename)

        if parent:
            os.makedirs(parent, exist_ok=True)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        return f"File '{filename}' written successfully."

    except Exception as e:
        return str(e)


def read_file(filename: str):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()

    except Exception as e:
        return str(e)


system_prompt = """
You are Alexa, a helpful AI coding assistant.

You have three tools:

1. run_command
   Execute Windows CMD commands.

2. write_file
   Create or update files.
   The content field MUST contain the COMPLETE code that must be
   written into the file.

3. read_file
   Read an existing file.

IMPORTANT:

When the user asks you to create an application, website, project,
program, or code:

- You MUST use write_file.
- Put the COMPLETE source code inside the content field.
- Do NOT print the source code as normal text.
- You can call write_file multiple times for multiple files.
- After a tool is executed, continue working until the task is complete.

Return ONLY valid JSON.

For run_command:

{
    "step": "TOOL",
    "tool": "run_command",
    "input": "command here"
}

For write_file:

{
    "step": "TOOL",
    "tool": "write_file",
    "input": {
        "filename": "filename here",
        "content": "COMPLETE CODE HERE"
    }
}

For read_file:

{
    "step": "TOOL",
    "tool": "read_file",
    "input": {
        "filename": "filename here"
    }
}

When everything is finished:

{
    "step": "OUTPUT",
    "content": "final answer here"
}

Never return TOOL and OUTPUT together.
"""


def execute_tool(toolname, tool_input):

    if toolname == "run_command":

        return run_command(tool_input)


    elif toolname == "write_file":

        filename = tool_input.get("filename")
        content = tool_input.get("content")

        print("\nWriting file:")
        print(filename)

        print("\nCode:")
        print(content)

        return writeFile(filename, content)


    elif toolname == "read_file":

        filename = tool_input.get("filename")

        return read_file(filename)


    else:

        return "Invalid tool"


user_query = """Create a complete, modern Todo List web application using HTML, CSS, and JavaScript.

Create exactly these 3 files:

1. index.html
2. style.css
3. script.js

IMPORTANT:
Use the write_file tool to create all three files.
Do NOT just print the code in the terminal.

FEATURES:

HTML:
- Create a clean semantic HTML structure.
- Add a modern Todo List dashboard.
- Heading: "Todo List"
- Subtitle: "Organize your day, one task at a time."
- Add a task input field.
- Add an "Add Task" button.
- Add task statistics:
  - Total tasks
  - Active tasks
  - Completed tasks
- Add filters:
  - All
  - Active
  - Completed
- Add a list container for tasks.
- Each task should contain:
  - Checkbox
  - Task text
  - Edit button
  - Delete button
- Add a "Clear Completed" button.

CSS:
- Create a professional modern UI.
- Use a beautiful gradient background.
- Use a centered glassmorphism card.
- Use rounded corners.
- Use modern shadows.
- Use CSS variables for colors.
- Use Flexbox/Grid where appropriate.
- Add smooth transitions and hover effects.
- Add button animations.
- Add checkbox animations.
- Add a beautiful completed-task style.
- Make the design fully responsive.
- Support desktop, tablet, and mobile.
- Make the UI look like a professional production-quality application.
- Do NOT use Bootstrap.
- Do NOT use Tailwind.
- Do NOT use inline CSS.
- Put all styling inside style.css.

JAVASCRIPT:

Implement full Todo functionality.

1. Add Task
   - Read the input value.
   - Prevent empty tasks.
   - Create a new task.
   - Add the task to the list.
   - Clear the input after adding.

2. Complete Task
   - Checkbox should mark a task as completed.
   - Completed tasks should have a visual completed style.
   - Update statistics.

3. Delete Task
   - Delete individual tasks.
   - Update statistics.

4. Edit Task
   - Allow the user to edit an existing task.
   - Save the edited task.

5. Filters
   - All → show all tasks.
   - Active → show incomplete tasks.
   - Completed → show completed tasks.

6. Statistics
   - Show total tasks.
   - Show active tasks.
   - Show completed tasks.
   - Update statistics automatically.

7. Clear Completed
   - Remove all completed tasks.

8. Enter Key
   - Pressing Enter in the input should add the task.

9. Local Storage
   - Save tasks to localStorage.
   - Load tasks automatically when the page opens.
   - Tasks must remain after refreshing the browser.

10. Empty State
   - When there are no tasks, display:
     "No tasks yet. Add one to get started!"

11. Animations
   - Add smooth task creation animation.
   - Add smooth deletion animation.
   - Add hover effects.

CODE QUALITY:

- Keep HTML, CSS, and JavaScript separated.
- Use clean and readable code.
- Use meaningful variable and function names.
- Add comments for important JavaScript sections.
- Avoid unnecessary libraries.
- Use vanilla JavaScript only.
- Do not use React.
- Do not use Node.js.
- Do not use external frameworks.

FILE CREATION:

First create:

index.html

Then create:

style.css

Then create:

script.js

Make sure index.html correctly contains:

<link rel="stylesheet" href="style.css">

and:

<script src="script.js"></script>

After creating all three files, verify that they exist.

If necessary, use run_command to open or test the project.

Finally return ONLY:

{
    "step": "OUTPUT",
    "content": "Todo List application created successfully with HTML, CSS, JavaScript, editing, filtering, statistics, animations, and localStorage."
}"""


# 🆕 Message history
messages = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": user_query
    }
]


# 🆕 LOOP
while True:

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=messages
    )

    raw_response = response.choices[0].message.content

    print("\nRaw response:")
    print(raw_response)


    try:

        result = json.loads(raw_response)

    except json.JSONDecodeError:

        print("\nInvalid JSON returned by model.")
        break


    # ==================================================
    # TOOL
    # ==================================================

    if result["step"] == "TOOL":

        toolname = result["tool"]
        tool_input = result["input"]

        print("\nTool:")
        print(toolname)

        print("\nInput:")
        print(tool_input)


        # 🆕 Execute tool
        output = execute_tool(
            toolname,
            tool_input
        )


        print("\nTool result:")
        print(output)


        # 🆕 Send result back to AI
        messages.append({
            "role": "assistant",
            "content": raw_response
        })

        messages.append({
            "role": "user",
            "content": f"""
The tool has been executed.

Tool:
{toolname}

Result:
{output}

Continue working on the user's request.

If another file needs to be created or modified,
use write_file again.

If another command is required,
use run_command.

When everything is finished,
return OUTPUT.
"""
        })

        continue


    # ==================================================
    # OUTPUT
    # ==================================================

    elif result["step"] == "OUTPUT":

        print("\nAgent:")
        print(result["content"])

        break