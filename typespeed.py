import time
import streamlit as st
import matplotlib as mlp
st.title('Typing speed test')
statement = "Type this statement as fast and accurately as you can and anything other than that we are just typing the most 4 letter normal words "
st.write(statement)

start = time.time()
user_input = st.text_input('hh')
end = time.time()
tupl = (0, end)
typing_speed = len(statement) / (end - start / 5) * 60
accuracy = (len(statement) - sum([1 for i, j in zip(statement, user_input) if i != j])) / len(statement)

#print("Your typing speed is {:.2f} words per minute.".format(typing_speed))
#print("Your accuracy is {:.2%}.".format(accuracy))
st.text("Your typing speed is {:.2f} words per minute.".format(typing_speed))
st.text(("Your accuracy is {:.2%}.".format(accuracy)))



#turn this into graph where the x axis is the time and the y is wpm