import ollama

def askLlama(prompt, temprt=0.0):
    response = ollama.generate(
        model='llama3.2', 
        prompt=prompt,
        options={
            'temperature': temprt
        }
    )
    
    return response['response']

