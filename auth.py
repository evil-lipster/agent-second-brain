from google_auth_oauthlib.flow import InstalledAppFlow

flow = InstalledAppFlow.from_client_secrets_file(
    r'C:\Users\lipsk\Downloads\credentials.json.json',
    ['https://www.googleapis.com/auth/tasks', 'https://www.googleapis.com/auth/calendar']
)
flow.oauth2session.params.update({'access_type': 'offline', 'prompt': 'consent'})
creds = flow.run_local_server(port=0)
open('token.json', 'w').write(creds.to_json())
print('Done')