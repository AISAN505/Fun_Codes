def sw1(state):
    state[0] = True
    
    print(state)

def sw2(state):
    state[3] = True
    state[1] = not state[1]
    
    print(state)

def sw3(state):
    state[2] = True
    state[0] = not state[0]
    state[1] = not state[1]
    
    print(state)
    
def sw4(state):
    state[1] = True
    state[0] = not state[0]
    state[2] = not state[2]
    
    print(state)
