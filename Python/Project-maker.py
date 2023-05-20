import openai
import os

# Set up your OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

# Define the prompt to generate code for a Python project
prompt = """
Generate Python code for a simple project:

Project: Project_number

Description: Write a Python program that does...

Code:
"""

# Generate code for 10 projects
for i in range(1, 11):
    project_prompt = prompt.replace("Project_number", str(i))

    # Generate code from GPT-3 model
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=project_prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the generated code from the API response
    generated_code = response.choices[0].text.strip()

    # Create a new .py file for each project
    filename = f"project{i}.py"
    with open(filename, 'w') as file:
        file.write(generated_code)

    print(f"Generated code for project {i}")

print("All projects generated successfully!")
