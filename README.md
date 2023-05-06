# ShockGPT
A custom chatbot integrated with OpenAI ChatGPT which circumvents OpenAI's Content Moderation & Safety Policy. 

Deployable to a lightweight cloud image such as Ubuntu Cloud Image or ALpine Linux. 
Run on localhost, and expose to a reverse proxy for WAN access (recommend not using port 443 but rather a Cloudflared Tunnel)
If WAN Accessible, recommend an LDAP/OAUTH layer, such as Authelia or Firewall rule to prevent unauthorized access, as there is no login functionality yet. 
