import cohere
import dotenv
import os
import random 
dotenv.load_dotenv()
co = cohere.Client(api_key=os.environ['COHERE_KEY'])
def Call_Papa_Cohere(PromptSit ="Jeff is currently distracted and is busy looking at birds outside the window", status = "distracted", scold=True, history=[]):
    if scold == True:
        pream = f"There is an unfit driver currently driving a vehicle, you are their parent, and are sitting next to them in the passenger seat. Upon receiving a situation, you will provide words of advice and criticism to ensure their safety and well being. Mention fond memories of your time together and be specific and imaginative, while staying in the first person as the driver's parent The situation is as follows:"
        
    else:
        pream = f"You are a narrator in a fictional scenerio where everything you have heard previously must be memorized and be used to answer the questions you recieve about the incident."
    response = co.generate(pream+PromptSit,\
                        max_tokens=250, temperature=1)
    print(response)
    '''f len(response[0].text) > 990:
        response.text = co.summarize(text=response.text, additional_command="Make the message briefer while keeping the tone").summary
        print(response.text)'''
    #history.extend([{"user_name": "User", "text": PromptSit}, {"user_name": "Chatbot", "text": response.text}])
    return response[0].text
