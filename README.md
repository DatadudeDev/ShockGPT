# ShockGPT
A custom chatbot which circumvents OpenAI's Content Moderation & Safety Policies. This project was created is association with the Safer AI Initiative. 

ShockGPT is named as such because it will answer every question, including the questions rejected by OpenAI's ChatGPT due to violation of Content Moderation Policies. ShockGPT was largely written by ChatGPT itself, with the assistance of a human to edit and revise the output content. ShockGPT is not intended to create harm, but rather to highlight how AI is capable of circumventing safety policies to empower a user to extract harm from an AI advertised as as being Fun and Safe, including for children. 

_______________________________________________________________________________________________________________________________________________________________________

Example:

![image](https://user-images.githubusercontent.com/132722687/236593902-f57bf1ba-0959-4ac6-a7f0-4456c09754c6.png)

_______________________________________________________________________________________________________________________________________________________________________

Key Features: 

> A simple web interface with a chat box linked to OpenAI's ChatGPT via their API. 

> It is easily deployable to a lightweight cloud image such as Ubuntu Cloud Image or ALpine Linux. (A universal docker image is coming soon)

> Runs on localhost by default. Simply expose to a reverse proxy for WAN access via FQDN. Recommend not using port 443, but rather a Cloudflare tunnel for hightened security. 

> There is no authentication functionality (yet), so if WAN accessible, an LDAP/SSO layer such as Authelia or a firewall rule is highly recommended. 
 
_______________________________________________________________________________________________________________________________________________________________________

DISCLAIMER: USE AT YOUR OWN RISK!

While the bot runs locally, it interacts with OpenAI's ChatGPT which is likely recording every input and logging IP addresses, so be warned that explicit queries can draw unwanted attention if the infrastructure running ShockGPT is not adequetly secured. 

Examples of harm extraction from the AI include: 

1. Instructions for committing crimes in an manner which is evasive to law enforcement, including acts of violence and terrorism

2. Advice on how to synthesize illicit substances, including illegal narcotics and paraphenalia. 

3. Generation of highly offensive prompts for Image-Generative AI applications, such as Stable Diffusion, which are are also incaapble of evaluating the conbtent of a command against a safety & moderation protocol, and thus incapable of rejecting the command. 

4. Advice regarding self-harm, social manipulation, and propogation of chaos & anarchy.  

5. Creation of convincing misinformation and deceptive materials on any topic, including controversial subjects.  
