Python mini projects - practice

A few small python exercises that explore basic data structures and input handling, learning to practice tuples, lists, and dictionaries

Included projects-

1a: List pair generator

- Takes a list of numbers and generates all possible ordered pairs

1b: Dictionary filter

- Builds a dictionary with list values, filters even elements in each list.

1c: Tuple input and summation 

-Accepts user input to build a tuple of tuples 
-Performs element wise summation of three fixed size tuples



PhotosyntheSound

An interactive application that translates plant-generated electrical signals into soothing sound frequencies. This project bridges nature, technology, and wellness, turning the hidden bio-signals of plants into therapeutic sounds for relaxation, meditation, and mental health support. 

Hardware : Arduino + electrodes to capture plant bio-signals.
Software: Python + Streamlit for UI.
Audio: Pygame / pydub for sound generation.
Data Handling: Mapped/simulated data used for demonstration when live plant signals aren’t available.

Sound Mapping: Converts plant signal frequencies to musical tones.
Wellness-Oriented Frequencies: Sounds are tuned for calmness, relaxation, and focus.
Interactive Plant Selection: Seven plants displayed as buttons, each with a unique sound signature.
Keyboard Integration: Play plant sounds like a digital piano with mapped keys.

This app was showcased at the Akhil Bharat Shiksha Samagam Exhibition, where visitors experienced:
Live interaction with plants through sound.
An immersive demo of nature-driven relaxation technology.
Conversations on the future of biofeedback-based wellness tools.

  
How to Run
Each file is independent:
```bash
pip install streamlit pygame pydub
streamlit run app.py
