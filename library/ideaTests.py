def eventListener(str):
    print(str)
    # add to event loop here
    return decorateEventListener

def decorateEventListener(func):
    def inner():
        print("decorateEventListener")
        func("TYPE EVENT")
    return inner

@eventListener("TYPE")
def onTYPE(event):
    print("Hello World", event)

onTYPE()