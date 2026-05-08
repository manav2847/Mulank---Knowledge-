import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mulank Knowledge", page_icon="🔮", layout="centered")

def main():
    st.title("🔮 Mulank Knowledge")
    st.subheader("Discover your inner qualities based on your birth date")
    st.write("---")

    date_input = st.number_input("Enter your birth date (1-31):", min_value=1, max_value=31, value=1)

    if st.button("Calculate My Mulank"):
        mulank = (date_input - 1) % 9 + 1
        
        st.balloons() 
        st.success(f"### Congratulations! You are Mulank {mulank}")
        st.write(f"**Details for Birth Date:** {date_input}")
        st.write("-" * 30)

        # Content logic with bolded keys
        if mulank == 1:
            st.info("### Mulank 1 (The Leader - Ruled by the 'SUN')")
            st.markdown(f'''
            * **Born on:** 1st, 10th, 19th, 28th
            * **Personality:** Ambitious, independent, and a natural-born leader.
            * **Best Colors:** Golden, Yellow, and Orange.
            * **Passion:** Success, innovation, and holding positions of authority.
            * **Love Life:** Loyal but likes to be the "boss."
            * **To Impress Them:** Show genuine respect for their work.
            * **Keep in Mind:** Avoid being overly egoistic or stubborn.''')

        elif mulank == 2:
            st.info("### Mulank 2 (The Peacekeeper - Ruled by the 'MOON')")
            st.markdown(f'''
            * **Born on:** 2nd, 11th, 20th, 29th
            * **Personality:** Gentle, highly emotional, and imaginative.
            * **Best Colors:** White, Cream, and Light Green.
            * **Passion:** Arts, music, poetry, and creativity.
            * **Love Life:** Extremely romantic and sensitive.
            * **To Impress Them:** Use soft words and be a good listener.
            * **Keep in Mind:** Avoid overthinking and being "moody."''')

        elif mulank == 3:
            st.info("### Mulank 3 (The Counselor - Ruled by 'JUPITER')")
            st.markdown(f'''
            * **Born on:** 3rd, 12th, 21st, 30th
            * **Personality:** Intellectual, disciplined, and very talkative.
            * **Best Colors:** Yellow, Pink, and Light Purple.
            * **Passion:** Education, public speaking, and writing.
            * **Love Life:** You look for an intellectual partner.
            * **To Impress Them:** Engage them in deep conversations.
            * **Keep in Mind:** Don't be "bossy" or give unasked advice.''')

        elif mulank == 4:
            st.info("### Mulank 4 (The Innovator - Ruled by 'RAHU')")
            st.markdown(f'''
            * **Born on:** 4th, 13th, 22nd, 31st
            * **Personality:** Practical, hardworking, and logical.
            * **Best Colors:** Blue, Grey, and Khaki.
            * **Passion:** Technology, engineering, and research.
            * **Love Life:** Cautious and takes time to trust.
            * **To Impress Them:** Be straightforward and logical.
            * **Keep in Mind:** Avoid being overly stubborn or argumentative.''')

        elif mulank == 5:
            st.info("### Mulank 5 (The Messenger - Ruled by 'MERCURY')")
            st.markdown(f'''
            * **Born on:** 5th, 14th, 23rd
            * **Personality:** Energetic, intelligent, and extremely versatile.
            * **Best Colors:** Light Green and White.
            * **Passion:** Travel, communication, and trading.
            * **Love Life:** Needs mental stimulation and freedom.
            * **To Impress Them:** Be witty and spontaneous.
            * **Keep in Mind:** Avoid being impulsive with decisions.''')

        elif mulank == 6:
            st.info("### Mulank 6 (The Romantic - Ruled by 'VENUS')")
            st.markdown(f'''
            * **Born on:** 6th, 15th, 24th
            * **Personality:** Attractive, compassionate, and family-oriented.
            * **Best Colors:** Royal Blue, Pink, and White.
            * **Passion:** Fashion, luxury, and interior design.
            * **Love Life:** Devoted partner who values stability.
            * **To Impress Them:** Appreciate their taste and dress well.
            * **Keep in Mind:** Avoid being overly materialistic.''')

        elif mulank == 7:
            st.info("### Mulank 7 (The Philosopher - Ruled by 'KETU')")
            st.markdown(f'''
            * **Born on:** 7th, 16th, 25th
            * **Personality:** Spiritual, quiet, and highly observant.
            * **Best Colors:** Light Green, White, and Yellow.
            * **Passion:** Research, philosophy, and nature.
            * **Love Life:** Needs a partner who respects silence.
            * **To Impress Them:** Be authentic and deep.
            * **Keep in Mind:** Avoid overthinking and isolating yourself.''')

        elif mulank == 8:
            st.info("### Mulank 8 (The Achiever - Ruled by 'SATURN')")
            st.markdown(f'''
            * **Born on:** 8th, 17th, 26th
            * **Personality:** Highly disciplined, serious, and patient.
            * **Best Colors:** Dark Blue and Black.
            * **Passion:** Business, law, and administration.
            * **Love Life:** Very loyal but struggles with expression.
            * **To Impress Them:** Show them your ambition and maturity.
            * **Keep in Mind:** Avoid being too cold or judgmental.''')

        elif mulank == 9:
            st.info("### Mulank 9 (The Warrior - Ruled by 'MARS')")
            st.markdown(f'''
            * **Born on:** 9th, 18th, 27th
            * **Personality:** Brave, humanitarian, and highly energetic.
            * **Best Colors:** Red and Pink.
            * **Passion:** Sports, social work, and defense.
            * **Love Life:** Passionate and protective.
            * **To Impress Them:** Show them your courage and kindness.
            * **Keep in Mind:** Avoid unnecessary anger and ego.''')

if __name__ == "__main__":
    main()
