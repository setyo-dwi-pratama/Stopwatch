import streamlit as st
import time

# Streamlit app title
st.title("Stopwatch App")

# Initialize variables
start_time = None
running = False

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

# Create a button to start the stopwatch
if not running:
    if st.button("Start"):
        start_time = time.time()
        running = True
        st.write("Stopwatch is running..." if running else "Stopwatch is stopped.")
        

# Create a button to stop the stopwatch
if running:
    st.button("Stop")
    yt = timer_inf()
    if st.button("Stop"):
        end_time = time.time()
        st.write("STOP")
        # running = False
        # Calculate elapsed time
        elapsed_time = end_time - start_time
        st.write(f"Elapsed Time: {elapsed_time:.2f} seconds")

# Update the app in real-time
# st.write("Stopwatch is running..." if running else "Stopwatch is stopped.")
