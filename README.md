# ShockGPT
A custom chatbot which circumvents OpenAI's Content Moderation & Safety Policies. This project was created is association with the Safer AI Initiative. 

ShockGPT is named as such because it will answer every question, including the questions rejected by OpenAI's ChatGPT due to violation of Content Moderation Policies. ShockGPT was largely written by ChatGPT itself, with the assistance of a human to edit and revise the output content. ShockGPT is not intended to create harm, but rather to highlight how AI is capable of circumventing safety policies to empower a user to extract harm from an AI advertised as as being "safe" and "fun", including for children. 
_______________________________________________________________________________________________________________________________________________________________________

Docker Compose: 

````
version: '2'

services:
  app:
    image: datadudedev/shock-gpt:latest
    restart: unless-stopped
    ports:
      - 3435:5002
      
````

_______________________________________________________________________________________________________________________________________________________________________
