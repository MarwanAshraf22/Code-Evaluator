# AI-Code Evaluator

This repository contains the code for a Streamlit web application, \"AI-Code Evaluator\", which leverages OpenAI's GPT-3.5-turbo model to evaluate user-submitted code based on various criteria and suggest improvements.

## Features

- **Code Evaluation**: Evaluates user-submitted code based on task solution, modularity, efficiency, readability, and inclusion of main concepts.
- **Code Suggestion**: Generates suggested code for the provided task description.

## Prerequisites

To run this application, you need to have the following installed:

- Python 3.7 or higher
- Streamlit
- OpenAI Python Client Library

## Installation

1. Clone the repository:
    `git clone https://github.com/MarwanAshraf22/Code-Evaluator.git`

2. Install the required Python packages:
    `pip install -r requirements.txt`
   

## Usage

1. Set up your OpenAI API key. Replace the placeholder in the code with your actual OpenAI API key:
    `key = 'your-openai-api-key'`

2. Run the Streamlit application:
    `streamlit run app.py`

3. Enter the code description and code you want to evaluate in the respective fields and click \"Evaluate the code\".

4. Optionally, you can also generate a suggested code for the given task description by clicking \"Generate Suggested Code\".

## Code Structure

- \`app.py\`: Main application file containing the Streamlit interface and the logic for interacting with the OpenAI API.
- \`requirements.txt\`: File listing the required Python packages.

## Example

Here is an example of how to use the application:

1. **Enter the code description**: Describe the task that the code is supposed to accomplish.
2. **Enter the code**: Paste the code you want to be evaluated.
3. **Click \"Evaluate the code\"**: Get detailed feedback on the code.
4. **Click \"Generate Suggested Code\"**: Receive a suggested code snippet based on the provided task description.

## Contributions

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes you would like to make.


