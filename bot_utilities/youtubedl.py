import os
import subprocess
import asyncio


async def bash_command(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    stdout, stderr = await process.communicate()
    #uncomment for debugging purposes
    if stdout:
        print(f"[stdout]\n{stdout.decode()}")
    if stderr:
        print(f"[stderr]\n{stderr.decode()}")


delfile = '/tmp/21.png'
delfile2 = "/tmp/imafile.webp"

def removes():
    for keycontext in os.listdir("/tmp"):
        if keycontext == '21.png':
            os.remove(f"{delfile}")
        elif keycontext == 'imafile.webp':
            os.remove(delfile2)
        elif keycontext == 'pske.m4a':
            os.remove("/tmp/pske.m4a")
        elif keycontext == "pske.mp3":
            os.remove("/tmp/pske.mp3")


#magic wahahahah
async def download_thumbnail(flink):
    await bash_command(f"/usr/bin/yt-dlp '{flink}' --embed-thumbnail --no-download  -o /tmp/imafile &")

async def download_m4a(flink):
    await bash_command(f'yt-dlp -f140 "{flink}" --embed-metadata --parse-metadata "playlist_index:%(track_number)s" -o /tmp/pske.m4a')

async def ffmpeg_function(namemusic):
    await bash_command(f'ffmpeg -i /tmp/imafile.webp -vf "crop=w=min(min(iw\,ih)\,720):h=min(min(iw\,ih)\,720),scale=720:720,setsar=1" -vframes 1 /tmp/21.png')
    await bash_command("ffmpeg -i /tmp/pske.m4a -c:a libmp3lame /tmp/pske.mp3")
    await bash_command(f"ffmpeg -i /tmp/pske.mp3 -i /tmp/21.png -map 1:0 -map 0:0 -c copy {namemusic}")

async def func(links):
    removes()
    await asyncio.gather(download_thumbnail(links), download_m4a(links))

async def thefunc(link, music_name):
    await func(links=link)
    await ffmpeg_function(namemusic=music_name)
