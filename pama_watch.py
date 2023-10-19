import streamlit as st
import time
# from SessionState import get
# from multiprocessing import Process

st.set_page_config()
st.title("Pama Watch Operation")

length = st.number_input("Length Path(km): ")
speed = 24

time_q = (length/speed) * 60

st.text("Your Ideal Time Operation each Cycle is {} seconds".format(time_q))

# session_state = get(a=0)

def timer_inf():
    ph = st.empty()
    N = 24*60*60
    yt = 0
    # session_state.a=2
    a=2
    for secs in range(0,N,1):
        mm, ss = secs//60, secs%60
        ph.metric("Your Time", f"{mm:02d}:{ss:02d}")
        time.sleep(1)
        yt += secs
        if a == 1:
        # if session_state.a == 1:
            break
    return yt


tbl_start = st.button("Start")

if tbl_start:
    # tbl_stop = st.button("Stop")
    # st.write("A")
    yt = timer_inf()
    
    # if tbl_stop:
    #     #check= time_q - yt
    #     st.text("Your Time {} with eval {}".format(yt, check))
        
        # yt = timer_inf()

