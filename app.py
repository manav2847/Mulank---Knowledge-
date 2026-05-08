import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mulank Knowledge", page_icon="🔮", layout="centered")

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #4bfff3;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # 1. Header Section
    st.title("🔮 Mulank Knowledge")
    st.subheader("Discover your inner qualities based on your birth date")
    st.write("---")

    # 2. Get User Input using a slider or number input (Web-friendly)
    date_input = st.number_input("Enter your birth date (1-31):", min_value=1, max_value=31, value=1)

    # 3. Logic to calculate Mulank
    if st.button("Calculate My Mulank"):
        mulank = (date_input - 1) % 9 + 1
        
        st.balloons() # Fun animation
        st.success(f"### Congratulations! You are Mulank {mulank}")
        st.write(f"**Details for Birth Date:** {date_input}")
        st.write("-" * 30)

        # 4. Details Sections
        if mulank == 1:
            st.info("### Mulank 1 (The Leader - Ruled by the 'SUN')")
            st.markdown('''**Born on:** 1st, 10th, 19th, 28th date of any Month
            \n**Personality:** Ambitious, independent, and a natural-born leader. You have high self-respect and original ideas.
            \n**Best Colors:** Golden, Yellow, and Orange.
            \n**Passion:** Success, innovation, and holding positions of authority.
            \n**Love Life:** Loyal but likes to be the "boss." Needs a supportive and respectful partner.
            \n**To Impress Them:** Show genuine respect for their work and value their time.
            \n**Keep in Mind:** Avoid being overly egoistic or stubborn. Don’t let your "fiery" temper make decisions for you.''')

        elif mulank == 2:
            st.info("### Mulank 2 (The Peacekeeper - Ruled by the 'MOON')")
            st.markdown('''**Born on:** 2nd, 11th, 20th, 29th date of any Month
            \n**Personality:** Gentle, highly emotional, and imaginative. You are a natural diplomat who prefers harmony over conflict.
            \n**Best Colors:** White, Cream, and Light Green.
            \n**Passion:** Arts, music, poetry, and any work involving creativity or helping others.
            \n**Love Life:** Extremely romantic and sensitive. You seek deep emotional connection and a peaceful home life.
            \n**To Impress Them:** Use soft words, be a good listener, and appreciate their creative ideas.
            \n**Keep in Mind:** Avoid overthinking and being "moody." Don't let others' opinions easily hurt your feelings.''')

        elif mulank == 3:
            st.info("### Mulank 3 (The Counselor - Ruled by 'JUPITER')")
            st.markdown('''**Born on:** 3rd, 12th, 21st, 30th date of any Month
            \n**Personality:** Intellectual, disciplined, and very talkative. You have a natural "Guru" vibe and love sharing knowledge.
            \n**Best Colors:** Yellow, Pink, and Light Purple.
            \n**Passion:** Education, public speaking, writing, and spiritual growth.
            \n**Love Life:** You look for an intellectual partner. You value your personal space and mental growth.
            \n**To Impress Them:** Engage them in deep conversations. Respect their wisdom.
            \n**Keep in Mind:** Don't be "bossy." Avoid over-spending and try not to be overly critical of others.''')

        elif mulank == 4:
            st.info("### Mulank 4 (The Innovator - Ruled by 'RAHU')")
            st.markdown('''**Born on:** 4th, 13th, 22nd, 31st date of any Month
            \n**Personality:** Practical, hardworking, and logical. You aren't afraid to challenge old traditions.
            \n**Best Colors:** Blue, Grey, and Khaki.
            \n**Passion:** Technology, engineering, research, and social reforms.
            \n**Love Life:** Cautious and takes time to trust. You look for a stable, honest partner.
            \n**To Impress Them:** Be straightforward and logical. They dislike "sugar-coating."
            \n**Keep in Mind:** Avoid being overly stubborn or argumentative. Don't isolate yourself.''')

        elif mulank == 5:
            st.info("### Mulank 5 (The Messenger - Ruled by 'MERCURY')")
            st.markdown('''**Born on:** 5th, 14th, 23rd date of any Month
            \n**Personality:** Energetic, intelligent, and extremely versatile. You have a "youthful" spirit.
            \n**Best Colors:** Light Green and White.
            \n**Passion:** Travel, communication, trading, and quick-witted entertainment.
            \n**Love Life:** You look for a partner who is mentally stimulating. You value your freedom.
            \n**To Impress Them:** Be witty and spontaneous. They love people who can keep up with them.
            \n**Keep in Mind:** Avoid being impulsive. Practice finishing one project before moving to the next.''')

        elif mulank == 6:
            st.info("### Mulank 6 (The Romantic - Ruled by 'VENUS')")
            st.markdown('''**Born on:** 6th, 15th, 24th date of any Month
            \n**Personality:** Attractive, compassionate, and family-oriented. You have a natural sense of style.
            \n**Best Colors:** Royal Blue, Pink, and White.
            \n**Passion:** Fashion, luxury, interior design, and hospitality.
            \n**Love Life:** The most romantic of all numbers. You are a devoted partner.
            \n**To Impress Them:** Appreciate their taste and dress well. Good manners are key.
            \n**Keep in Mind:** Avoid being overly materialistic. Don't be too "controlling" in relationships.''')

        elif mulank == 7:
            st.info("### Mulank 7 (The Philosopher - Ruled by 'KETU')")
            st.markdown('''**Born on:** 7th, 16th, 25th date of any Month
            \n**Personality:** Spiritual, quiet, and highly observant. You have a "detective" mind.
            \n**Best Colors:** Light Green, White, and Yellow.
            \n**Passion:** Research, philosophy, spirituality, and nature.
            \n**Love Life:** Deep lover but hard to understand. You need a partner who respects "me-time."
            \n**To Impress Them:** Be authentic and deep. They hate small talk.
            \n**Keep in Mind:** Avoid overthinking and isolating yourself too much.''')

        elif mulank == 8:
            st.info("### Mulank 8 (The Achiever - Ruled by 'SATURN')")
            st.markdown('''**Born on:** 8th, 17th, 26th date of any Month
            \n**Personality:** Highly disciplined, serious, and patient. You are a "slow and steady" winner.
            \n**Best Colors:** Dark Blue and Black.
            \n**Passion:** Business, law, administration, and large-scale management.
            \n**Love Life:** Very loyal but struggles to express feelings. You look for stability.
            \n**To Impress Them:** Show them your ambition and maturity. Don't make empty promises.
            \n**Keep in Mind:** Avoid being too cold. Don't lose hope during delays—success is guaranteed.''')

        elif mulank == 9:
            st.info("### Mulank 9 (The Warrior - Ruled by 'MARS')")
            st.markdown('''**Born on:** 9th, 18th, 27th date of any Month
            \n**Personality:** Brave, humanitarian, and highly energetic. You have a strong sense of justice.
            \n**Best Colors:** Red and Pink.
            \n**Passion:** Sports, social work, defense, and high-energy tasks.
            \n**Love Life:** Passionate and protective. You look for an honest partner.
            \n**To Impress Them:** Show them your courage and kindness. Be straightforward.
            \n**Keep in Mind:** Avoid unnecessary anger. Practice patience and forgiveness.''')

if __name__ == "__main__":
    main()
