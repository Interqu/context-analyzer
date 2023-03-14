import os
from dotenv import load_dotenv
import openai

load_dotenv()

# Initilizing openai with a given API_KEY.
openai.api_key = os.getenv('API_KEY')


def getInterviewContentFeedback(position, question, answer):
    # Answer Query DO NOT CHANGE OPTIMIZED QUERY
    query = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that analyzes interview answers."},
            {"role": "user", "content": f"This is an interview for a {position} position. Give feedback on my answer's structure, content and effectiveness and suggest improvements to stand out. Use personal pronouns in your response. Question:'{question}'. Answer:'{answer}'"}
        ]
    )
    # Validating answer
    finish_reason = query['choices'][0]['finish_reason']
    if finish_reason == 'stop':
        return query['choices'][0]['message']['content']
    else:
        return f"UNEXPECTED ERROR. Response Generation could not complete. Finish Reason: {finish_reason}"


# EXAMPLES
position = "product manager"
question = "What Motivates You?"
answer = "I'm addicted to planning! Being organized at work and at home drives me to make sure I have enough time to achieve my goals and give my best in all I do. It ensures that I don't overtask myself so I can focus on doing quality work and not get burned out by working consistently long hours on any one project. Good time management helps me maintain consistently excellent standards."

print(getInterviewContentFeedback(position, question, answer))
