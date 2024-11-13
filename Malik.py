import streamlit as st
import random

# Function to simulate keyword analysis (you can replace this with real API calls)
def keyword_analysis(keyword):
    # Example: Simulating a keyword analysis response
    return {
        "search_volume": random.randint(500, 10000),  # Simulating random search volume
        "competition": random.choice(["Low", "Medium", "High"]),  # Random competition level
        "suggestions": [f"{keyword} tips", f"{keyword} SEO", f"{keyword} analysis"]
    }

# Streamlit UI layout
def main():
    st.title("Advanced SEO Keyword Analyzer")
    st.write("Enter a keyword to analyze its search volume, competition, and related keywords.")

    # Session state to keep track of previous keyword searches
    if 'keyword' not in st.session_state:
        st.session_state.keyword = ""

    # Input for keyword
    keyword = st.text_input("Enter Keyword:")

    # Clear previous results when a new keyword is entered
    if keyword != st.session_state.keyword:
        st.session_state.keyword = keyword
        st.session_state.clear_results = True
    else:
        st.session_state.clear_results = False

    if keyword:
        # If there's a new keyword or session state flag is set, clear previous results
        if st.session_state.clear_results:
            st.session_state.results = None

        # Fetching keyword analysis data (you can replace this with a real API)
        data = keyword_analysis(keyword)

        # Displaying the keyword analysis results
        st.write(f"**Search Volume**: {data['search_volume']}")
        st.write(f"**Competition**: {data['competition']}")
        st.write("**Suggested Keywords**:")
        for suggestion in data["suggestions"]:
            st.write(suggestion)

        # Store the results in session state for later use
        st.session_state.results = data

        # Button for analyzing the next keyword
        if st.button("Analyze Next Keyword"):
            st.session_state.clear_results = True
            st.experimental_rerun()  # Re-run to clear previous results and get new data

if __name__ == "__main__":
    main()
