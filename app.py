import streamlit as st
import numpy as np
import main


# Create text input for brand task and user task
brand_task = st.text_input("Please enter the brand or company name:")
user_task = st.text_input("Please enter your goal, brief, or problem statement:")


# Create a button to start the conversation
start_button = st.button("Start Conversation")

# When the button is pressed, start the conversation
if start_button:
    # Set the brand_task and user_task in your main script
    main.brand_task = brand_task
    main.user_task = user_task

    with st.chat_message("user"):
        # Start the conversation
        conversation = main.start_conversation()  # You need to define this function in your main script

        # Display the conversation using Streamlit's markdown functionality
        for message in conversation:
            st.markdown(f"**{message}**")