import requests
import os
from pathlib import Path
from subprocess import call, check_output

def save_random_image(width, height, filename):
    url = f'https://picsum.photos/{width}/{height}/?random'
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)

def get_monitor_resolution():
    COMMAND_GET_DIMENSIONS = "xdpyinfo | awk '/dimensions/{print $2}'"
    output = check_output(COMMAND_GET_DIMENSIONS, shell=True)
    return output.decode('utf-8').strip().split('x')

def main():
    filename = "wallpaper.temp"
    save_random_image(*get_monitor_resolution(), filename)
    COMMAND_SET_BACKGROUND = "gsettings set org.gnome.desktop.background picture-uri"
    call(f'{COMMAND_SET_BACKGROUND} file://{str(Path.home())}/{filename}', shell=True)

if __name__ == '__main__':
    main()
