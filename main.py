import vkinderBot
import config

if __name__ == '__main__':
    vkinderBot = vkinderBot.VkinderBot(config.token, config.pg_link)
    vkinderBot.start()
    
