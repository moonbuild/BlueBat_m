from aiogram import Bot, Dispatcher, executor, types
from SECRETKEY import token
import Responses as R
import subprocess, sys
import janken

bot = Bot(token)
dp = Dispatcher(bot)

py=False

@dp.message_handler(commands=['start'])
async def welcome(message: types):
    await message.reply('Hi!\nhi👋\n~I am a Blue Bat that does bat stuff')
    
@dp.message_handler(commands=['help'])
async def help(message: type):
    await message.reply('My other commands are: \start \rock \paper \scissors',
    '\nI am a growing bat\nfor now to require assistance, \nplease contact my caretakers via: helpers_out_of_the_blue@protonmail.com')

@dp.message_handler(commands=['python'])
async def code(message: type):
    global py
    py=True
    await message.reply("Okay u can send python code now")

@dp.message_handler(commands=['notpython'])
async def code(message: type):
    global py
    py=False
    await message.reply("Okay u can stop sending python code now")

@dp.message_handler(commands=['rock','paper','scissors'])
async def game(message: type):
    result = janken.letsPlay(message.text[1:])
    await message.reply(result)

@dp.message_handler()
async def responses(message: types.Message):
    text = (message.text).lower()

    global py
    if py == True:
        try:
            f= open("program.py", "a")
            f.truncate(0)
            f.write(message.text+"\n")
            f.close()

            output = subprocess.check_output([sys.executable, './program.py'])
            tp = open('outfile.txt', 'wb')
            with tp as outfile:
                outfile.write(output)
            tp.close()

            rd = open('outfile.txt','r')
            out = rd.readlines()
            for line in out:
                await message.reply(line)
            rd.close()
            return
        except:
            await message.text('There was an error\nSorry--Sorry\ni tried my best🙁')
            py = False
            return
    

    elif text in ['rock','paper','scissors']:
        result= janken.letsPlay(text)   
        await message.reply(result)
        return
    
    await message.reply(R.answer(message.text))
        
        
if __name__ == '__main__':
    print('~\(^~^)/~')
    executor.start_polling(dp)