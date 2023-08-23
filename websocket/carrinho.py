import websocket
import time

from pynput.keyboard import Key, Listener 

try:
    import thread
except ImportError:
    import _thread as thread


import time

def show(key): 
  
    print('\nYou Entered {0}'.format( key)) 
    global tecla
    valor = str(key).upper().replace("'", "")

    if valor == "W":
        tecla = "F"
    elif valor == "A":
        tecla = "E"
    elif valor == "D":
        tecla = "D"
    elif valor == "S":
        tecla = "R"
    elif valor == "P":
        tecla = "P"

    print(tecla)

    ws.send(tecla)

    if key == Key.delete: 
      return False

def on_message(ws, message):
    # print("SENDING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + tecla)
    # ws.send(tecla)
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        # for i in range(3):
        #     time.sleep(1)
        #     ws.send("Hello %d" % i)
        # time.sleep(1)
        # ws.close()wd

        with Listener(on_press = show) as listener:    
            listener.join() 

        print("thread terminating...")
    thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://192.168.0.116:81",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()

