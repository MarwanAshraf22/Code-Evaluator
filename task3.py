import streamlit as st
from openai import OpenAI

st.title("_AI-Code Evaluator_")

key = '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'
client = OpenAI(api_key=key)

def generate_text(user_description, user_code):
    if user_description and user_code:
        try:
            prompt = (
                f"Task description: {user_description}\n"
                f"Code (solution):\n{user_code}\n\n"
                f"Evaluation Criteria:\n"
                f"1. **Task Solution:** Evaluate whether the code effectively solves the given task description. Provide insights on how closely it aligns with the requirements.\n"
                f"2. **Modularity:** Assess the code's modularity. Comment on how well the code is organized into functions or modules.\n"
                f"- For modularity, consider breaking down the code into separate functions for each major step.\n"
                f"3. **Efficiency and Readability:** Analyze the code's efficiency, cleanliness, and readability. Provide feedback on any improvements needed in these aspects.\n"
                f"- Regarding efficiency, look for opportunities to optimize loops or data processing.\n"
                f"4. **Main Concepts Inclusion:** Check if the code includes essential sections such as preprocessing, data splitting, model training, testing, and any other relevant parts.\n"
                f"5. **AI-Generated Content:** Ensure that the code demonstrates characteristics of being AI-generated.\n"
                f"Examples:\n"
            )

            with st.spinner("Generating Evaluation..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Code Evaluation System"},
                        {"role": "user", "content": prompt},
                    ])

                generated_text = response.choices[0].message.content
                return generated_text

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

user_description = st.text_input("Enter code description:")
user_code = st.text_area('Enter code here')

# Initialize generated_text with an initial value
generated_text = ""

if st.button('Evaluate the code'):
    # Update generated_text when the button is clicked
    generated_text = generate_text(user_description, user_code)

    st.write("Evaluation:")
    st.write(generated_text)


if st.button('Generate Suggested Code'):
    suggested_code_prompt = (
        f"Generate a suggested code for the given task description:\n"
        f"Task description: {user_description}"
    )
    with st.spinner("Generating Suggested Code..."):
        suggested_code_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Suggested Code Generation System"},
                {"role": "user", "content": suggested_code_prompt},
            ])
        suggested_code = suggested_code_response.choices[0].message.content
        st.write("Suggested Code:")
        st.code(suggested_code)
