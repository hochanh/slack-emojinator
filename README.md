# Slack Emojinator

*Bulk upload emoji into Slack*

Want to create a custom Slack emoji for every pokemon? Slack doesn't currently expose an API endpoint for creating emoji, probably to prevent users from doing exactly what I'm doing, but here's a way to do it anyway.

## Creating Emoji

Clone the project, create a new virtualenv, and install the prereqs:

```bash
git clone https://github.com/manhtai/slack-emojinator.git
cd slack-emojinator
pip install -r requirements.txt
```

You'll need to provide your team name (the bit before ".slack.com" in your admin URL) and your session cookie (grab it from your browser):

```bash
python upload.py channel_name cookie folder_path
```

:sparkles:
