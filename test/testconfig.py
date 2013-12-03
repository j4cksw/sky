#test config
import ConfigParser

config = ConfigParser.ConfigParser()

f = config.read("game.cfg")

t = config.get('test','t')

print t

t = 0

config.write(f)



