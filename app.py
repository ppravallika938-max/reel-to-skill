import streamlit as st

st.title(" Reel2Skill")
st.write("Turn your scrolling into useful technology!")

st.header("Select the Reels you watched")

reels = {
    "Java Meme": "Programming",
    "Software Engineer Life": "Career",
    "Coding Interview Joke": "Programming",
    "Laptop Comparison": "Hardware",
    "AI Tutorial": "AI",
    "Gaming Video": "Gaming",
    "Cricket Video": "Entertainment"
}

selected = st.multiselect(
    "Choose your Reels:",
    reels.keys()
)

if st.button("Find My Interest"):

    if not selected:
        st.warning("Please select some Reels.")

    else:

        topics = []

        for reel in selected:
            topics.append(reels[reel])

        programming = topics.count("Programming")
        career = topics.count("Career")
        hardware = topics.count("Hardware")
        ai = topics.count("AI")

        # Find interest

        if programming + career >= 2:

            interest = "Software Engineering"

            recommendation = "How HashMaps Work"

            category = "DSA"

            difficulty = "Beginner"

            why = "You watched programming and software career content."

        elif ai >= 1:

            interest = "Artificial Intelligence"

            recommendation = "How Generative AI Works"

            category = "AI"

            difficulty = "Beginner"

            why = "You watched AI-related content."

        elif hardware >= 1:

            interest = "Computer Hardware"

            recommendation = "How a CPU Works"

            category = "Hardware"

            difficulty = "Beginner"

            why = "You showed interest in computers and hardware."

        else:

            interest = "Technology"

            recommendation = "How the Internet Works"

            category = "Other"

            difficulty = "Beginner"

            why = "Your Reels show general technology interest."

        st.header("🧠 INTEREST DETECTED")

        st.success(interest)

        st.write("### WHY")

        for reel in selected:
            st.write(
                "• " + reel + " → " + reels[reel]
            )

        st.header("🚀 RECOMMENDED TECH REEL")

        st.success(recommendation)

        st.write("**CATEGORY:**", category)

        st.write("**WHY THIS RECOMMENDATION:**", why)

        st.write("**DIFFICULTY:**", difficulty)

        st.write("**CONFIDENCE:** High")