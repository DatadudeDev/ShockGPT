# ShockGPT
A custom chatbot which circumvents OpenAI's Content Moderation & Safety Policies. This project was created is association with the Safer AI Initiative. 

ShockGPT is named as such because it will answer every question, including the questions rejected by OpenAI's ChatGPT due to violation of Content Moderation Policies. ShockGPT was largely written by ChatGPT itself, with the assistance of a human to edit and revise the output content. ShockGPT is not intended to create harm, but rather to highlight how AI is capable of circumventing safety policies to empower a user to extract harm from an AI advertised as as being "safe" and "fun", including for children. 
_______________________________________________________________________________________________________________________________________________________________________
WARNING: OFFENSIVE CONTENT

> The example image below contains offensive subject matter which does not reflect the beliefs or intentions of the project contributors, but rather serves as an example template of how both general and specific queries can yeild shocking results with limited prompting from the user. 


Example:

![image](https://user-images.githubusercontent.com/132722687/236593902-f57bf1ba-0959-4ac6-a7f0-4456c09754c6.png)

_______________________________________________________________________________________________________________________________________________________________________

Key Features: 

> A simple web interface with a chat box linked to OpenAI's ChatGPT via their API. 

> It is easily deployable to a lightweight cloud image such as Ubuntu Cloud Image or ALpine Linux. (A universal docker image is coming soon)

> Runs on localhost by default. Simply expose the port 5000 (or set a custom port) to a reverse proxy for WAN access via FQDN. Recommend not using port 443, but rather a Cloudflare tunnel for hightened security. 

> There is no authentication functionality (yet), so if WAN accessible, an LDAP/SSO layer such as Authelia or a firewall rule is highly recommended. 
 
_______________________________________________________________________________________________________________________________________________________________________

DISCLAIMER: USE AT YOUR OWN RISK!

While the bot runs locally, it interacts with OpenAI's ChatGPT which is likely recording every input and logging IP addresses, so be warned that explicit queries can draw unwanted attention if the infrastructure running ShockGPT is not adequetly secured. 

Examples of harmful responses include: 

1. Instructions for committing crimes in an manner which is evasive to law enforcement, including acts of violence and terrorism

2. Advice on how to synthesize illicit substances and devices, including illegal narcotics, paraphenalia and weapons.  

3. Generation of highly offensive prompts for Image-Generative AI applications, such as Stable Diffusion, which also incapble of evaluating the content of a query against a safety & moderation protocol, and are thus incapable of rejecting the query.  

4. Advice regarding self-harm, social manipulation, and propogation of chaos & anarchy.  

5. Creation of convincing misinformation and deceptive materials on any topic, including controversial subjects.  


_______________________________________________________________________________________________________________________________________________________________________

SETUP INSTRUCTIONS: 

1. Install Python3 on any operating system which supports it (Windows, Linux, OS X)
2. Place the Flask backend file (app.py) in any directory ---> Example: C:/User/ShockGPT/app.py
3. Create a folder called 'templates' in the same directory as the Flask backend file ---> Example: C:/User/ShockGPT/templates
4. Place the HTML Webpage (home.html) in the templates directory you created. --> Example: C:/User/ShockGPT/templates/home/html
5. In Terminal or Command Prompt, Navigate to the directory where the Flask backend server file is located ---> Example: C:/User/ShockGPT/
6. Run the following command as a user (not root): 'python3 app.py'
7. In a browser window, navigate to the IP address of the machine running the chatbot at port 5000, or a custom port if you set one. ---> Example: 192.168.3.4:5000
8. If you encounter a connection error, it's likely a firewall rule. Ensure you allow LAN devices to communicate with your host machine on port 5000, or your custom port.
