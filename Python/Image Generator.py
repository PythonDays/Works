import tkinter as tk
import requests
from PIL import Image, ImageTk
import io

# DeepAI API key (replace 'YOUR_API_KEY' with your actual API key)
API_KEY = '34d1b193-23c5-439f-b23e-ea72e2de5a5f'

# Function to generate an image using DeepAI API
def generate_image():
    input_text = entry.get()
    response = requests.post(
        'https://api.deepai.org/api/text2img',
        data={
            'text': input_text,
        },
        headers={'api-key': API_KEY}
    )
    if response.status_code == 200:
        result = response.json()
        image_url = result['output_url']
        download_image(image_url)
    else:
        print('Error:', response.text)

# Function to download and display the generated image
def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        image.thumbnail((400, 400))  # Resize the image to fit the window
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo

# Create the chat window
window = tk.Tk()
window.title("DeepAI Image Generator")

# Create an input entry field
entry = tk.Entry(window)
entry.pack()

# Create a button
button = tk.Button(window, text="Generate", command=generate_image)
button.pack()

# Create a label to display the generated image
image_label = tk.Label(window)
image_label.pack()

# Start the GUI main loop
window.mainloop()
