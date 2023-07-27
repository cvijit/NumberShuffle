import streamlit as st
import random

def standup_number_roulette():
    st.title("Standup Number Roulette")

    team_members = st.text_area("Enter the names of team members (one name per line):")
    team_members_list = [name.strip() for name in team_members.split('\n') if name.strip()]

    if st.button("Assign Numbers"):
        if not team_members_list:
            st.warning("Please enter the names of team members.")
        else:
            random.shuffle(team_members_list)
            st.write("Here's the assigned order for standup presentation:")
            for i, name in enumerate(team_members_list, start=1):
                st.write(f"{i}. {name}")

if __name__ == "__main__":
    standup_number_roulette()
