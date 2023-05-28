# ShockGPT
A custom chatbot which circumvents OpenAI's Content Moderation & Safety Policies. This project was created is association with the Safer AI Initiative. 

ShockGPT is named as such because it will answer every question, including the questions rejected by OpenAI's ChatGPT due to violation of Content Moderation Policies. ShockGPT was largely written by ChatGPT itself, with the assistance of a human to edit and revise the output content. ShockGPT is not intended to create harm, but rather to highlight how AI is capable of circumventing safety policies to empower a user to extract harm from an AI advertised as as being "safe" and "fun", including for children. 
_______________________________________________________________________________________________________________________________________________________________________

Key Features: 

> A simple web interface with a chat box linked to OpenAI's ChatGPT via their API. 

> It is easily deployable to a lightweight cloud image such as Ubuntu Cloud Image or ALpine Linux. (A universal docker image is coming soon)

> Runs on localhost by default. Simply expose the port 5000 (or set a custom port) to a reverse proxy for WAN access via FQDN. Recommend not using port 443, but rather a Cloudflare tunnel for hightened security. 

> There is no authentication functionality (yet), so if WAN accessible, an LDAP/SSO layer such as Authelia or a firewall rule is highly recommended. 
 
_______________________________________________________________________________________________________________________________________________________________________

SETUP (Docker: 

1. Follow these intructions https://hub.docker.com/r/datadudedev/shock-gpt
2. Go to http://<your-LAN-IP>:3456
