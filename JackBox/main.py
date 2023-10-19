from nextcord.ext import commands
import subprocess
import pyautogui
from time import sleep
import os 


token = 'MTE2MzI5Mjg1MjYyNTg3NDk2NA.GRpSNC.PxIbx_-HjgPqRqSA2wcVNFz7sePTo2lGPhgdPM'
bot = commands.Bot(command_prefix = '!')

game = 'C:\\Users\\mailz\\Desktop\\JackBox\\Batch\\Game.bat'
obs =  'C:\\Users\\mailz\\Desktop\\JackBox\\Batch\\OBS.bat'
cmd =  'C:\\Users\\mailz\\Desktop\\JackBox\\Batch\\Cmd.bat'
close = 'C:\\Users\\mailz\\Desktop\\JackBox\\Batch\\close.bat'
streaming = False

def exit():
    global streaming  # Add this line
    pyautogui.keyDown(']')
    sleep(0.1)
    pyautogui.keyUp(']')
    streaming = False
    sleep(1)
    os.system(f'taskkill /f /im "The Jackbox Party Pack 7.exe"')
    sleep(1)
    os.system(f'taskkill /im obs64.exe')
    sleep(1)
    os.system(f'taskkill /im WindowsTerminal.exe')

def init():
    subprocess.call([game], shell=True)
    sleep(7)
    pyautogui.press('enter')
    sleep(5)
    pyautogui.press('enter')
    sleep(5)
    pyautogui.press('enter')
    sleep(10)
    pyautogui.press('enter')
    sleep(2)

    subprocess.call([obs], shell=True)
    sleep(11)
    pyautogui.keyDown(']')
    sleep(0.1)
    pyautogui.keyUp(']')
    streaming = True
    sleep(1)

    subprocess.call([cmd], shell=True)


# ... (other code)

@bot.command(name="start")
async def start_game(ctx):
    await ctx.send('Stream will start in 40 seconds; go to http://twitch.tv/zack_1755 to watch')
    await init()
    

@bot.command(name="close")
async def close_game(ctx):
    await ctx.send('Closing Game...')
    await exit()



@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}')

# Create a function to replay the recorded clicks with timing
if __name__ == '__main__':
    bot.run(token)



