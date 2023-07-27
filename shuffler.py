import streamlit as st
import random
import time

def standup_number_roulette():
    st.title("Standup Number Roulette")

    team_members = st.text_area("Enter the names of team members (one name per line):")
    team_members_list = [name.strip() for name in team_members.split('\n') if name.strip()]

    if st.button("Start Roulette"):
        if not team_members_list:
            st.warning("Please enter the names of team members.")
        else:
            st.write("Spinning the roulette wheel...")
            st.write("And the number is...")

            # Shuffle the list of team members repeatedly to create the spinning effect
            for i in range(20):
                random.shuffle(team_members_list)
                st.write(f"{i+1}. {team_members_list[0]}")
                time.sleep(0.5)  # Add a pause between each spin for animation effect

            st.success("Number assigned: 1. " + team_members_list[0])

if __name__ == "__main__":
    standup_number_roulette()
