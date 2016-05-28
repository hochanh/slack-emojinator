import os
import requests

from bs4 import BeautifulSoup


def upload_emo(team_name, cookie, dir_name):
    url = "https://{}.slack.com/customize/emoji".format(team_name)
    i = 1
    file_names = os.listdir(dir_name)
    a = len(file_names)

    for file_name in file_names:
        print("Processing {}.".format(file_name))
        emoji_name = '_' + os.path.splitext(file_name)[0]
        headers = {
            'Cookie': cookie,
        }

        # Fetch the form first, to generate a crumb.
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text)
        crumb = soup.find("input", attrs={"name": "crumb"})["value"]

        data = {
            'add': 1,
            'crumb': crumb,
            'name': emoji_name,
            'mode': 'data',
        }
        files = {'img': open(os.path.join(dir_name, file_name), 'rb')}
        r = requests.post(url,
                        headers=headers,
                        data=data,
                        files=files,
                        allow_redirects=False)
        r.raise_for_status()
        print("{} complete ({}/{}).".format(file_name, i, a))


if __name__ == "__main__":
    import argparse
    argp = argparse.ArgumentParser()
    argp.add_argument('channel_name')
    argp.add_argument('cookie')
    argp.add_argument('folder_name')
    args = argp.parse_args()
    upload_emo(args.channel_name, args.cookie, args.folder_name)
