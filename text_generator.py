import openai
import text_utils

openai.api_key = "OPENAI_KEY"
model_engine = "text-davinci-002"

def textgen(input_text, print_text=False, clear_text=False):

    response = openai.Completion.create(
        engine=model_engine,
        prompt=input_text+', em português',
        temperature=0.5,
        max_tokens=500
    )

    output_text = response.choices[0].text.strip()
    if clear_text==True:
        output_text = text_utils.clear_text(output_text)
    if print_text == True:
        print('INPUT:', input_text)
        print('OUTPUT:', output_text)
    return output_text

