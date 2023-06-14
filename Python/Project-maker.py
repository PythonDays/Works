import openai
import os

# Set up your OpenAI API credentials
openai.api_key = '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'

# Define the prompt to generate code for a Python project
prompt = """
Generate Python code for a simple project:

Project: Project_number

Description: Write a python project at the best level of coding you can execute. you need to be sure it works and
don't repeat yourself

Code:
"""

# Generate code for 10 projects
for i in range(1, 31):
    project_prompt = prompt.replace("Project_number", str(i))

    # Generate code from GPT-3 model
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=project_prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the generated code from the API response
    generated_code = response.choices[0].text.strip()

    # Create a new .py file for each project
    filename = f"projects{i}.py"
    with open(filename, 'w') as file:
        file.write(generated_code)

    print(f"Generated code for project {i}")

print("All projects generated successfully!")
