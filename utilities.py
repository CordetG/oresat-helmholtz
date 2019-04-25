DEBUG = False
TICK_TIME = 15
GRAPH_RANGE = 30

def log(mode, message):
    try:
        level = {
            0: 'INFO',
            1: 'WARN',
            2: 'DEBUG',
            3: 'ERROR',
        }

        print('[' + level[mode] + ']: ' + message)
        return True
    except:
        return False
