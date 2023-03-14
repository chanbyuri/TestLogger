import sys
import gui
import cui

if __name__ == '__main__':
    mainProgram = None
    if len(sys.argv) == 1:
        mainProgram = gui.MainProgram()
    elif len(sys.argv) == 2:
        cmd: str = sys.argv[1]
        if cmd == '-cui':
            mainProgram = cui.MainProgram()
        elif cmd == '-gui':
            mainProgram = gui.MainProgram()
        else:
            print('argv is incorrect')
            exit(-1)
    else:
        print('argv is incorrect')
        exit(-1)