import cohere
import dotenv
import os
import random 
dotenv.load_dotenv()
account_key = os.environ['COHERE_KEY']
co = cohere.Client(account_key)
def Call_Papa_Cohere(PromptSit ="Jeff is currently distracted and is busy looking at birds outside the window", status = "distracted", id=str(random.randint(0,1234567))):
    response = co.chat(message=PromptSit, conversation_id=id, preamble_override=f"There is a {status} driver currently driving a vehicle, you are their parent, and are about to scold them and advize them on what to do about it, in under 40 words.\
                        Be strict. The current situation is about to be given to you, respond appropiately",\
                        max_tokens=500, temperature=0.5)
    print(response.text)
    if len(response.text) > 990:
        response.text = co.summarize(text=response.text, additional_command="Make the message briefer while keeping the tone")
        print(response.text)
    return response.text