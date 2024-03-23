import args
import plugins.citi as citi

def handle_plugin(pluginName):
    print(pluginName)

args = args.parseArgs()

plugin = args.plugin
filename = args.filename

match(plugin):
    case 'citi':
        citi.analyze(filename)
    case 'cap_one':
        print('cap_one handler')
    case 'chase':
        print('chase handler')
    case _:
        exit('invalid plugin type')