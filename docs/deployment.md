# Deployment
## Environment variables
### General:
These are required whether you're using the included automations or not.
- `WEBHOOK_PREFIX`

### Personal
You should list any environment variables necessary for your personal automations below so you don't forget them.

## Deploying in Repl.it
Set the environment variables described above, then press the Run button at the top of the page. Make sure you set up an 
UptimeRobot monitor pointing at the root url to make sure repl.it doesn't shut down the server.
### Replit Setup
Replit is an online IDE which this project is designed to use to host your automations.
- Create a free account at https://replit.com
  - I recommend you use "Sign In With GitHub", because otherwise you'll need to link your accounts later.
- In your [dashboard](https://replit.com/~), click the plus button to create a new repl.
- Select "Import from GitHub".
- Select your fork of PyAutomations.
- Click the lock icon in the sidebar within the repl.
- Create the environment variables described above.
- Click the green play button at the top to start the server.
### UptimeRobot Setup
Replit stops your app from running if it has been too long since someone has accessed it. To prevent this, you can use
UptimeRobot to automatically ping your app every 5 minutes.
- Create a free account at https://uptimerobot.com
- From your dashboard, click the green "+ Monitor" button on the left.
- For monitor type, select HTTPS
- Enter the following information, leaving everything else as default:
  - Friendly name: PyAutomations
  - URL: https://<repl-name>.<username>.repl.com
- Click Create Monitor, and then click the button again if it turns orange.
