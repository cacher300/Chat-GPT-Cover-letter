import openai
import json

API_KEY = "sk-"
openai.api_key = API_KEY


job_title = input("Enter the job title: ")
company_name = input("Enter the company name: ")
applicant_name = input("Enter your name: ")
experience = input("Enter your years of experience: ")
skills = input("Enter your skills: ")
example_job_duty = input("Enter an example of a job duty: ")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "Write me a cover letter using these pieces of info: " + job_title + ", " + company_name + ", " + applicant_name + ", " + experience + ", " + skills + ", " + example_job_duty + "."}],
)

completion = str(completion)

data = json.loads(completion)

# Extract the cover letter content from the first choice message
content = data['choices'][0]['message']['content']

# Print the cover letter content
print(content)
