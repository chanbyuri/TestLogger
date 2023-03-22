import sys
import gui
import cui

CMD_CUI = '-cui'
CMD_GUI = '-gui'
ARGV_ERROR = 'argv is incorrect'

if __name__ == '__main__':
    mainProgram = None
    if len(sys.argv) == 1:
        mainProgram = gui.MainProgram()
    elif len(sys.argv) == 2:
        cmd = sys.argv[1]
        if cmd == CMD_CUI:
            mainProgram = cui.MainProgram()
        elif cmd == CMD_GUI:
            mainProgram = gui.MainProgram()
        else:
            print(ARGV_ERROR)
            exit(-1)
    else:
        print(ARGV_ERROR)
        exit(-1)