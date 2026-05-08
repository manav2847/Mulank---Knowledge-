def calculate_mulank():
    while True:
        try:
            # 1. Get user input
            date_input = int(input("Please enter your birth date (1-31): "))

            # 2. Validate the date
            if date_input < 1 or date_input > 31:
                print("You had chosen a wrong date. Please try again.")
                print("-" * 30)
                continue # Restarts the loop

            # 3. Logic to calculate Mulank (sum of digits)
            # We use (date - 1) % 9 + 1 as a clean way to get the root digit
            mulank = (date_input - 1) % 9 + 1

            print(f"\nCongratulation! You are Mulank {mulank}")
            print("-" * 30)

            # 4. Details Sections - Type your custom details inside the print("")
            if mulank == 1:
                # Dates: 1, 10, 19, 28
                print("Details:> Your birth date Is :" , date_input)
                print("Mulank 1 (The leader Ruled by The 'SUN')")
                print('''Born on: 1st, 10th, 19th, 28th

Personality: Ambitious, independent, and a natural-born leader. You have high self-respect and original ideas.

Best Colors: Golden, Yellow, and Orange.

Passion: Success, innovation, and holding positions of authority.

Love Life: Loyal but likes to be the "boss." Needs a supportive and respectful partner.

To Impress Them: Show genuine respect for their work and value their time.

Keep in Mind: Avoid being overly egoistic or stubborn. Don’t let your "fiery" temper make decisions for you.''')
            elif mulank == 2:
                # Dates: 2, 11, 20, 29
                print("Details:> Your birth date Is :" , date_input)
                print("Mulank 2 (The Peacekeeper Ruled by The 'MOON') ")
                print('''Born on: 2nd, 11th, 20th, 29th

Personality: Gentle, highly emotional, and imaginative. You are a natural diplomat who prefers harmony over conflict.

Best Colors: White, Cream, and Light Green.

Passion: Arts, music, poetry, and any work involving creativity or helping others.

Love Life: Extremely romantic and sensitive. You seek deep emotional connection and a peaceful home life.

To Impress Them: Use soft words, be a good listener, and appreciate their creative ideas.

Keep in Mind: Avoid overthinking and being "moody." Don't let others' opinions easily hurt your feelings or shake your confidence.''')

            elif mulank == 3:
                # Dates: 3, 12, 21, 30
                print("Details:> Your birth date Is :" , date_input )
                print("Mulank 3 (The Counselor Ruled by 'JUPITER')")
                print('''Born on: 3rd, 12th, 21st, 30th

Personality: Intellectual, disciplined, and very talkative. You have a natural "Guru" vibe and love sharing knowledge with others.

Best Colors: Yellow, Pink, and Light Purple.

Passion: Education, public speaking, writing, and spiritual growth. You love to constantly learn.

Love Life: You look for an intellectual partner. While you are loyal, you value your personal space and mental growth above all.

To Impress Them: Engage them in deep conversations. Show that you are ambitious and respect their wisdom.

Keep in Mind: Don't be "bossy" or give advice where it isn't asked for. Avoid over-spending and try not to be overly critical of others.''')

            elif mulank == 4:
                # Dates: 4, 13, 22, 31
                print("Details:> Your birth date Is :" , date_input)
                print("Mulank 4 (The Innovator Ruled by 'RAHU')")
                print('''Born on: 4th, 13th, 22nd, 31st

Personality: Practical, hardworking, and logical. You often have a different perspective than the crowd and aren't afraid to challenge old traditions.

Best Colors: Blue, Grey, and Khaki.

Passion: Technology, engineering, research, and social reforms. You love "solving" complex problems.

Love Life: You are very cautious and take time to trust. You look for a stable, honest partner who can handle your unpredictable nature.

To Impress Them: Be straightforward and logical. They dislike "sugar-coating" and appreciate people who are punctual and organized.

Keep in Mind: Avoid being overly stubborn or argumentative. Don't let your "sudden" anger or revolutionary thoughts isolate you from friends and family.''')

            elif mulank == 5:
                # Date: 5, 14, 23
                print("Details:> Your birth date Is :" , date_input)
                print("Mulank 5 (The Messenger Ruled by 'MERCURY')")
                print('''Born on: 5th, 14th, 23rd

Personality: Energetic, intelligent, and extremely versatile. You have a "youthful" spirit and can make friends with almost anyone instantly.

Best Colors: Light Green and White.

Passion: Travel, communication, trading, and quick-witted entertainment. You hate sitting still or doing boring, repetitive tasks.

Love Life: You look for a partner who is mentally stimulating. You value your freedom and need someone who isn't overly possessive.

To Impress Them: Be witty and spontaneous. They love people who can keep up with their fast conversation and enjoy trying new things.

Keep in Mind: Avoid being impulsive with your decisions. Don’t start too many things at once—practice finishing one project before moving to the next.''')

            elif mulank == 6:
                # Date: 6, 15, 24
                print("Details:> Your birth date Is :" , date_input)
                print("Mulank 6 (The Romantic Ruled by 'VENUS')")
                print('''Born on: 6th, 15th, 24th

Personality: Attractive, compassionate, and family-oriented. You have a natural sense of style and a deep love for harmony and "the good life."

Best Colors: Royal Blue, Pink, and White.

Passion: Fashion, luxury, interior design, and hospitality. You enjoy making everything around you look beautiful.

Love Life: You are the most romantic of all numbers. You are a devoted partner who values stability and physical affection.

To Impress Them: Appreciate their taste and dress well. They are easily impressed by good manners, expensive gifts, and a pleasant scent (perfume).

Keep in Mind: Avoid being overly materialistic or "extravagant." Don't interfere too much in others' lives out of love, as it can be seen as "controlling." ''')

            elif mulank == 7:
                # Date: 7, 16, 25
                print("Details:> Your birth date Is :" , date_input)
                print("Mulank 7 (The Philosopher Ruled by 'KETU')")
                print('''Born on: 7th, 16th, 25th

Personality: Spiritual, quiet, and highly observant. You have a "detective" mind and can easily see through lies or fake people.

Best Colors: Light Green, White, and Yellow.

Passion: Research, philosophy, spirituality, and nature. You love spending time alone to recharge your energy.

Love Life: You are a deep lover but can be hard to understand. You need a partner who respects your silence and your need for "me-time."

To Impress Them: Be authentic and deep. They hate small talk; they are impressed by people who have a calm aura and intellectual depth.

Keep in Mind: Avoid overthinking and isolating yourself too much. Don’t let your "restless" mind lead to unnecessary anxiety or distrust of others.''')

            elif mulank == 8:
                # Date: 8, 17, 26
                print("Details:> Your birth date Is :" , date_input)
                print("Mulank 8 (The Achiever Ruled by 'SATURN')")                
                print('''Born on: 8th, 17th, 26th

Personality: Highly disciplined, serious, and patient. You are a "slow and steady" winner who faces struggles early in life but achieves great power later.

Best Colors: Dark Blue and Black.

Passion: Business, law, administration, and large-scale management. You have a massive capacity for hard work.

Love Life: You are very loyal but struggle to express your feelings. You look for a partner who is stable and understands your dedication to work.

To Impress Them: Show them your ambition and maturity. They respect people who are grounded, hardworking, and don't make empty promises.

Keep in Mind: Avoid being too cold or "judgmental" toward others. Don't lose hope during delays—your success is guaranteed if you stay patient and ethical.''')

            elif mulank == 9:
                # Date: 9, 18, 27
                print("Details:> Your birth date Is :" , date_input)
                print("Mulank 9 (The Warrior Ruled by 'MARS') ")
                print('''Born on: 9th, 18th, 27th

Personality: Brave, humanitarian, and highly energetic. You have a strong sense of justice and will fight for what is right, often putting others before yourself.

Best Colors: Red and Pink.

Passion: Sports, social work, defense/police, and anything involving high physical or mental energy.

Love Life: You are passionate and protective. You look for a partner who is honest and can handle your strong, sometimes "fiery" personality.

To Impress Them: Show them your courage and kindness. They are impressed by people who are straightforward, active, and have a helping nature.

Keep in Mind: Avoid unnecessary anger and "short-tempered" reactions. Don't let your ego interfere with your relationships—practice patience and forgiveness. ''')

            break # Exit loop after successful calculation

        except ValueError:
            print("Invalid input! Please enter a number only.")

if __name__ == "__main__":
    calculate_mulank()
