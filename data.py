class Data():
    def __init__(self):
        self.training_data = [
            ("i like to read books. i like the colour purple", 1),
            ("i like to walk in parks", 1),
            ("i like to go to the movies", 1),
            ("i like to ride horses. i like to do maths.", 1),
            ("John is a friendly person", 1),
            ("Mary is outgoing and adventurous", 1),
            ("I love to travel and try new things", 1),
            ("I'm a friendly person", 1),
            ("i like to go to the beach for long walks", 1),
            ("my friends say that i am very funny. i like to go mountian biking", 1),
            ("i like to go on walks with my dog. my favourite colour is red. I like to go wakeboarding", 1),
            ("I am a good listener and a loyal friend", 1),
            ("I enjoy playing soccer on the weekends", 1),
            ("I love reading mystery novels in my spare time", 1),
            ("I'm very organized and detail-oriented", 1),
            ("I am passionate about cooking and trying new recipes", 1),
            ("I like to go hiking in the mountains on weekends", 1),
            ("I am a compassionate and caring individual", 1),
            ("I am a firm believer in equality and fairness for all", 1),
            ("I'm a night owl and prefer working at night", 1),
            ("I am a creative person and love to express myself through art", 1),
            ("I'm always willing to lend a helping hand to those in need", 1),
            ("I enjoy attending music concerts and festivals", 1),
            ("I am a hardworking and dedicated individual", 1),
            ("I am a fitness enthusiast and enjoy going to the gym", 1),
            ("I am a risk-taker and love adventure sports", 1),
            ("I love to travel and explore new cultures and cuisines", 1),
            ("I am a positive and optimistic person", 1),
            ("I'm a social butterfly and love meeting new people", 1),
            ("I love to write and express my thoughts through words", 1),
            ("I am a spiritual person and believe in the power of the universe", 1),
            ("I enjoy volunteering and giving back to the community", 1),
            ("I am a quick learner and love to acquire new skills", 1),
            ("I am a tech enthusiast and enjoy keeping up with the latest gadgets", 1),
            ("I am an introvert and enjoy spending time alone", 1),
            ("I am a foodie and love trying new cuisines", 1),
            ("I'm an animal lover and have two cats", 1),
            ("I am a curious person and love to explore new things", 1),
            ("My favorite food is sushi, and I am always looking to expand my knowledge.", 1),
            ("I am a curious person and love to explore new things", 1),
            ("I am a minimalist and prefer a simple and clutter-free lifestyle", 1),
            ("I am a patient person and always strive to see the best in people", 1),
            ("I enjoy watching documentaries and learning about new topics", 1),
            ("I am a good communicator and enjoy connecting with people", 1),
            ("I enjoy playing board games and solving puzzles", 1),
            ("I am a team player and enjoy collaborating with others", 1),
            ("I enjoy playing musical instruments in my free time", 1),
            ("I am a fashion enthusiast and enjoy keeping up with the latest trends", 1),
            ("I am an environmentalist and strive to live a sustainable lifestyle", 1),
            ("I am a night owl and enjoy going for long walks at night", 1),
            ("I am a minimalist and prefer to keep my possessions to a minimum", 1),
            ("John is a friendly person", 1),
            ("Mary is outgoing and adventurous", 1),
            ("I love to travel and try new things", 1),
            ("male. i like big juicy bananas. my favourite colour is yellow", 1),
            ("I'm a friendly person", 1),
            ("I am a history buff and love learning about different time periods", 1),
            ("I am a movie enthusiast and enjoy watching films from all over the world", 1),
            ("I am a coffee lover and enjoy trying different blends and brewing methods", 1),
            ("I am a fitness coach and enjoy helping others achieve their health goals", 1),
            ("I am a language learner and enjoy studying new languages", 1),
            ("I am an avid reader and enjoy all kinds of literature", 1),
            ("I am a runner and enjoy participating in marathons and other races", 1),
            ("I am a meditation practitioner and enjoy the benefits of mindfulness", 1),
            ("I am a nature lover and enjoy hiking and camping", 1),
            ("I am a science enthusiast and enjoy learning about the latest scientific discoveries", 1),
            ("I am a social activist and advocate for human rights", 1),
            ("I am a wine connoisseur and enjoy trying different varieties and vintages", 1),
            ("I am a fashion designer and enjoy creating unique and stylish clothing", 1),
            ("I am a food blogger and enjoy sharing recipes and culinary experiences", 1),
            ("I am a photographer and enjoy capturing beautiful moments and scenery", 1),
            ("I am a travel blogger and enjoy documenting my adventures around the world", 1),
            ("I am a musician and enjoy composing and performing music", 1),
            ("I am a chef and enjoy creating new and innovative dishes", 1),
            ("I am a writer and enjoy crafting stories and poetry", 1),
            ("i like the colour blue. i like to play sports",1),
            ("i like the colour purple", 1),
            ("i like to play soccer", 1),
            ("i like to play basketball", 1),
            ("i like to play cricket", 1),
            ("i like the colour pink", 1),
            ("i like the colour red", 1),
            ("i like the colour purple", 1),
            ("i like to pay games", 1),
            ("I am a gamer and enjoy playing video games in my free time", 1),
            ("I am a painter and enjoy expressing myself through art", 1),
            ("I am a mentor and enjoy guiding and supporting others", 1),
            ("I am a dancer and enjoy performing in front of audiences", 1),
            ("I am a gardener and enjoy tending to plants and creating beautiful gardens", 1),
            ("I am a traveler and enjoy exploring different countries and cultures", 1),
            ("I am a fashion model and enjoy modeling for fashion shows and photo shoots", 1),
            ("I am a yoga instructor and enjoy helping others achieve physical and mental balance", 1),
            ("I am a journalist and enjoy reporting on current events and issues", 1),
            ("I am a carpenter and enjoy building and creating with my hands", 1),
            ("I am a makeup artist and enjoy creating beautiful looks for clients", 1),
            ("I am a philosopher and enjoy exploring the big questions of life", 1),
            ("I am a social media influencer and enjoy sharing my lifestyle and experiences with my followers", 1),
            ("I am a personal trainer and enjoy helping others achieve their fitness goals", 1),
            ("girl. I am a graphic designer and enjoy creating visually appealing designs", 1),
            ("neutral. I am a stand-up comedian and enjoy making people laugh", 1),
            ("non-binary. I am an entrepreneur and enjoy creating and running my own business", 1),
            ("male. I am a scientist and enjoy conducting experiments and researching new discoveries", 1),
            ("female. I am a humanitarian and enjoy working towards creating a better world for all", 1),
            ("lana am a teacher and enjoy helping students learn and grow", 1),
            ("boy. I am a makeup enthusiast and enjoy experimenting with different looks and products", 1),
            ("jaack am a food critic and enjoy reviewing restaurants and dishes", 1),
            ("I am a perfectionist and pay great attention to detail", 1),
            ("I am an empathetic person and always try to understand others' perspectives", 1),
            ("I am a responsible individual and always fulfill my commitments", 1),
            ("I am a goal-oriented person and strive to achieve my objectives", 1),
            ("I am an independent thinker and enjoy exploring new ideas", 1),
            ("I am a good problem-solver and enjoy finding solutions to complex issues", 1),
            ("I am a patient listener and always give others a chance to express themselves", 1),
            ("I am a reliable friend and always stand by my loved ones", 1),
            ("i play volleyball", 1),
            ("volleyball", 1),
            ("I am a resilient person and always bounce back from setbacks", 1),
            ("I am a confident speaker and enjoy giving presentations and speeches", 1),
            ("I am an analytical thinker and enjoy breaking down complex problems", 1),
            ("I am an enthusiastic learner and enjoy acquiring new knowledge and skills", 1),
            ("I am a creative thinker and enjoy coming up with innovative solutions", 1),
            ("I am a decisive person and always make well-informed choices", 1),
            ("I am a good team leader and enjoy guiding others towards a common goal", 1),
            ("I am an open-minded person and always willing to consider different perspectives", 1),
            ("I am a respectful person and always treat others with dignity and kindness", 1),
            ("I am a good time-manager and always make the most of my day", 1),
            ("I am a humble person and always willing to learn from others", 1),
            ("I am a detail-oriented person and always pay attention to the little things", 1),
            ("I am an adventurous person and always willing to try new experiences", 1),
            ("I am a generous person and always willing to lend a helping hand", 1),
            ("I am a persistent person and always pursue my goals with determination", 1),
            ("I am a proactive person and always take initiative", 1),
            ("I am a reflective person and always take time to evaluate my actions and decisions", 1),
            ("I am a good listener and always give my full attention to others", 1),
            ("I am a diplomatic person and always handle conflicts with tact and sensitivity", 1),
            ("I am a self-motivated person and always find ways to stay motivated", 1),
            ("I am a good negotiator and always find win-win solutions", 1),
            ("I am a trustworthy person and always keep my word", 1),
            ("I am a charismatic person and always make a good first impression", 1),
            ("I am a self-disciplined person and always stick to my commitments", 1),
            ("I am a visionary person and always think outside the box", 1),
            ("I am a flexible person and always adapt to changing circumstances", 1),
            ("I am a good teacher and enjoy sharing my knowledge with others", 1),
            ("I am an honest person and always tell the truth", 1),
            ("I am a curious person and always ask questions to deepen my understanding", 1),
            ("I am a good mentor and enjoy helping others reach their full potential", 1),
            ("I am a resilient person and always bounce back from adversity", 1),
            ("I am a dedicated person and always put in the necessary effort to achieve my goals", 1),
            ("I am a proactive problem-solver and always anticipate and address potential issues", 1),
            ("I am a good networker and always make valuable connections", 1),
            ("I am a good organizer and always keep things in order", 1),
            ("I am a good motivator and always inspire others to reach their goals", 1),
            ("mia am a motivational speaker and enjoy inspiring others to achieve their dreams", 1),
            ("emma am a software engineer and enjoy creating innovative software solutions", 1),
            ("john am a philanthropist and enjoy giving back to the community", 1),
            ("i like to go to the beach for long walks", 1),
            ("my friends say that i that i am very funny. i like to go mountian biking", 1),
            ("i like to go on walks with my dog. my favourite colour is red. I like to go wakeboarding", 1),
            ("The weather is warm and sunny today", 0),
            ("my pants are blue, my pants are long", 0),
            ("my dog is brown and very big. my dog likes to go to the beach", 0),
            ("She is a traveler at heart and loves to participate in quiz nights.", 1),
            ("my dog likes food", 0),
            ("the sky is blue", 0),
            ("The book I'm reading is very interesting", 0),
            ("I need to finish my work before the deadline", 0),
            ("I went to the store to buy some milk", 0),
            ("The concert starts at 7 PM tonight", 0),
            ("I need to get my car washed this weekend", 0),
            ("It's raining outside and I forgot my umbrella", 0),
            ("I have a dentist appointment next week", 0),
            ("I need to renew my passport soon", 0),
            ("The traffic on the highway was terrible this morning", 0),
            ("I have a meeting with my boss at 2 PM", 0),
            ("The new restaurant in town has great reviews", 0),
            ("I need to do my laundry tonight", 0),
            ("The book I'm reading is a mystery novel", 0),
            ("I want to learn how to speak Spanish fluently", 0),
            ("I need to go grocery shopping later", 0),
            ("I'm going to the gym after work", 0),
            ("The traffic light turned red", 0),
            ("Given the nature of the question, we would not recommend any baby names.", 0),
            ("that response does not match our guidelines", 0),
            (" i am", 0),
            ("i like", 0),
            ("i enjoy", 0),
            ("i am having a boy", 0),
            ("i am having a girl", 0),
            ("i am having a male", 0),
            ("i am having a female", 0),
            ("my child is non-binary", 0),
            ("I need to buy a new pair of shoes", 0),
            ("I'm going to a friend's birthday party this weekend", 0),
            ("The news said it's going to be hot this weekend", 0),
            ("I'm going to a job interview tomorrow", 0),
            ("I need to file my taxes soon", 0),
            ("I'm looking for a new apartment to rent", 0),
            ("The sun is setting behind the mountains. The sky is painted with hues of orange and pink.", 0),
            ("The little girl skipped down the path, holding her mother's hand tightly. She looked up at her with a big smile on her face.", 0),
            ("The sound of waves crashing against the shore filled the air. The salty sea breeze blew through my hair.", 0),
            ("The old man sat quietly on the park bench, feeding the pigeons. He had a kind smile on his face.", 0),
            ("The bright lights of the city sparkled like diamonds in the distance. The hustle and bustle of the streets could be heard from miles away.", 0),
            ("The aroma of fresh coffee wafted through the air. The steam rising from the cup was mesmerizing.", 0),
            ("The leaves on the trees rustled gently in the breeze. The sound was peaceful and calming.", 0),
            ("The snow fell silently from the sky, covering the ground in a blanket of white. The winter air was crisp and cold.", 0),
            ("The room was filled with the sound of laughter and chatter. The party was in full swing.", 0),
            ("The dog wagged its tail happily as its owner scratched behind its ears. Its tongue lolled out of its mouth in contentment.", 0),
            ("I'm going to a concert next month", 0),
            ("I need to buy a present for my friend's wedding", 0),
            ("I'm going to the beach next weekend", 0),
            ("The museum has a new exhibit on display", 0),
            ("I need to make a doctor's appointment", 0),
            ("I'm going to a music festival next summer", 0),
            ("I'm going to a comedy show this Friday", 0),
            ("I need to walk my dog in the morning", 0),
            ("I'm going to a friend's house for dinner tonight", 0),
            ("The art gallery is closed on Mondays", 0),
            ("I need to pay my rent by the end of the week", 0),
            ("I'm going to a baseball game next week", 0),
            ("I need to get my oil changed soon", 0),
            ("I'm going to a farmer's market this weekend", 0),
            ("The library has a great selection of books", 0),
            ("I need to renew my driver's license", 0),
            ("My dog barks at strangers", 0),
            ("My cat likes to sleep all day", 0),
            ("My hamster loves to run on his wheel", 0),
            ("My parrot mimics everything I say", 0),
            ("male. My cat is very picky when it comes to food", 0),
            ("female. My dog is afraid of the vacuum cleaner", 0),
            ("boy. My rabbit likes to chew on everything", 0),
            ("girl. My cat hates taking baths", 0),
            ("male. i like to play with little girls. my favourite colour is red", 0),
            ("My dog loves to play fetch with his tennis ball", 0),
            ("My turtle likes to sunbathe on his rock", 0),
            ("My cat is very curious and likes to explore", 0),
            ("My dog is always happy to see me when I come home", 0),
            ("My hamster likes to burrow in his bedding", 0),
            ("My parrot likes to dance to music", 0),
            ("My cat is very independent and likes to do her own thing", 0),
            ("My dog is very protective of our family", 0),
            ("My rabbit likes to dig holes in the yard", 0),
            ("My cat loves to curl up in my lap and purr", 0),
            ("My dog is afraid of thunderstorms", 0),
            ("My hamster likes to stuff his cheeks with food", 0),
            ("My parrot likes to talk to himself in the mirror", 0),
            ("My cat likes to watch birds from the window", 0),
            ("My dog loves to swim in the lake", 0),
            ("My rabbit likes to cuddle with me on the couch", 0),
            ("My cat likes to scratch on her scratching post", 0),
            ("My dog is very good at catching frisbees", 0),
            ("My hamster likes to chew on cardboard", 0),
            ("My parrot likes to mimic the sound of the phone ringing", 0),
            ("My cat likes to play with toy mice", 0),
            ("My dog likes to chase squirrels in the backyard", 0),
            ("My rabbit likes to dig tunnels in the dirt", 0),
            ("My cat likes to groom herself for hours", 0),
            ("My dog is always up for a game of tug-of-war", 0),
            ("My hamster likes to run through his maze", 0),
            ("My parrot likes to watch TV with me", 0),
            ("The building next door is under construction", 0),
            ("I need to replace the batteries in my smoke detector", 0),
            ("The power went out during the storm", 0),
            ("I have a flat tire and need to call for roadside assistance", 0),
            ("The restaurant is closed for renovations", 0),
            ("I need to change my mailing address with the post office", 0),
            ("The airline lost my luggage on my trip", 0),
            ("I accidentally locked my keys in my car", 0),
            ("The company is merging with another company", 0),
            ("I need to update my computer's antivirus software", 0),
            ("The store is out of stock of the item I need", 0),
            ("I need to cancel my reservation at the hotel", 0),
            ("The train is delayed due to technical difficulties", 0),
            ("I need to replace the air filter in my car", 0),
            ("The item I ordered online was damaged during shipping", 0),
            ("I need to renew my car registration", 0),
            ("The road is closed due to construction", 0),
            ("i like to eat children", 0),
            ("I need to get a new prescription for my medication", 0),
            ("The product I bought is not working properly", 0),
            ("I need to book a rental car for my trip", 0),
            ("The elevator is out of service", 0),
            ("I need to schedule an appointment with my dentist", 0),
            ("The flight I booked was cancelled", 0),
            ("I need to renew my gym membership", 0),
            ("The package I received was not what I ordered", 0),
            ("I need to change the oil in my car", 0),
            ("The event I planned to attend was postponed", 0),
            ("I need to fix the leak in my roof", 0),
            ("The website I was trying to access is down", 0),
            ("I need to renew my passport", 0),
            ("The concert I bought tickets for was cancelled", 0),
            ("I need to get a new set of tires for my car", 0),
            ("The restaurant I reserved a table at has a dress code", 0),
            ("I need to file a claim with my insurance company", 0),
            ("The museum is closed on Mondays", 0),
            ("I need to update my phone's software", 0),
            ("The product I received was the wrong color", 0),
            ("I need to fix the broken tile in my bathroom", 0),
            ("The movie I wanted to watch is not available on any streaming services", 0),
            ("I need to renew my library card", 0),
            ("The bus I was waiting for never arrived", 0),
            ("I need to replace the light bulb in my kitchen", 0),
            ("The store has a no return policy", 0),
            ("I'm going to the movies with my friends. my dog like long walks on the beach. i like to play sports in my free time", 0),
            ("The sky is blue. The temperature is 20 degrees Celsius.", 0),
            ("The book is thick. The cover is red.", 0),
            ("The car is fast. The color is silver.", 0),
            ("The plant is tall. The leaves are green.", 0),
            ("The coffee is hot. The mug is white.", 0),
            ("The phone is new. The screen is large.", 0),
            ("The shirt is soft. The color is blue.", 0),
            ("The dog is friendly. The fur is brown.", 0),
            ("The pizza is delicious. The toppings are pepperoni and mushrooms.", 0),
            ("The movie is long. The genre is comedy.", 0),
            ("the cat is sleeping on the couch. the couch is leather", 0),
            ("the sun is shining brightly. the sky is blue", 0),
            ("the flower is red. the stem is green", 0),
            ("the book is on the table. the table is made of wood", 0),
            ("the car is parked in the garage. the garage door is closed", 0),
            ("the coffee is hot. the cup is made of porcelain", 0),
            ("the tree is tall. the leaves are green", 0),
            ("the computer is running smoothly. the monitor is a Dell", 0),
            ("the dog is barking loudly. the leash is made of leather", 0),
            ("the baby is sleeping soundly. the crib is made of wood", 0)
        ]