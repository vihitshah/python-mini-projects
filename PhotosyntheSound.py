
# python -m streamlit run UI_PLANTS.py
import streamlit as st
import numpy as np
import sounddevice as sd
import time

# --- Note to (Frequency, Note Name, Effect) mapping ---
note_map = {
    'Z': (196.00, "G3", "Calm"),
    'X': (220.08, "A3", "Relaxation"),
    'C': (246.94, "B3", "Balance"),
    'A': (261.63, "C4", "Focus"),
    'S': (293.66, "D4", "Clarity"),
    'D': (329.63, "E4", "Energy"),
    'F': (349.23, "F4", "Stability"),
    'G': (392.00, "G4", "Grounding"),
    'H': (440.00, "A4", "Alertness"),
    'J': (493.88, "B4", "Mindfulness"),
    'K': (523.25, "C5", "Creativity"),
    'L': (554.37, "C#5", "Serenity"),
    ';': (587.33, "D5", "Joy"),
}

# --- Plant Melodies ---
plant_songs = {
    "Aloe Vera": [('Z', 0.3), ('A', 0.3), ('S', 0.3), ('D', 0.3), ('A', 0.3)],
    "Lavender": [('A', 0.3), ('S', 0.3), ('D', 0.3), ('S', 0.3), ('A', 0.3)],
    "Snake Plant": [('F', 0.3), ('G', 0.3), ('H', 0.3), ('G', 0.3), ('F', 0.3)],
    "Peace Lily": [('C', 0.3), ('A', 0.3), ('C', 0.3), ('D', 0.3), ('A', 0.3)],
    "Spider Plant": [('H', 0.3), ('J', 0.3), ('K', 0.3), ('J', 0.3), ('H', 0.3)],
    "Basil": [('Z', 0.3), ('X', 0.3), ('C', 0.3), ('X', 0.3), ('Z', 0.3)],
    "Fern": [('K', 0.3), ('L', 0.3), (';', 0.3), ('L', 0.3), ('K', 0.3)]
}

# --- Songs ---
songs = {
    "Vande Mataram": [
        ('A', 0.5), ('S', 0.75),
        ('F', 0.25), ('G', 0.25), ('F', 0.25), ('G', 2.0),
        ('F', 0.5), ('G', 0.75),
        ('J', 0.25), ('K', 0.25), ('J', 0.25), ('K', 2.0),
        ('K', 0.25), (';', 0.25), ('J', 0.5), ('H', 0.25), ('G', 0.5),
        ('G', 0.25), ('H', 0.25), ('F', 0.5), ('D', 0.25), ('S', 0.5),
        ('S', 0.5), ('G', 0.25), ('F', 0.25), ('G', 0.25), ('D', 0.25), ('S', 0.5), ('D', 0.25), ('A', 2.0)
    ],
    "Happy Birthday": [
        ('Z', 0.25), ('Z', 0.25), ('X', 0.5), ('Z', 0.5), ('A', 0.5), ('C', 1.0),
        ('Z', 0.25), ('Z', 0.25), ('X', 0.5), ('Z', 0.5), ('S', 0.5), ('A', 1.0),
        ('Z', 0.25), ('Z', 0.25), ('G', 0.5), ('D', 0.5), ('A', 0.5), ('C', 0.5), ('X', 1.0),
        ('F', 0.25), ('F', 0.25), ('D', 0.5), ('A', 0.5), ('S', 0.5), ('A', 1.0)
    ]
}

# --- Function to play tone ---
def play_tone(freq, duration=0.6, volume=0.3, samplerate=44100):
    t = np.linspace(0, duration, int(samplerate * duration), False)
    tone = np.sin(freq * t * 2 * np.pi) * volume
    sd.play(tone, samplerate=samplerate)
    sd.wait()

# --- Streamlit UI ---
st.set_page_config(page_title="PhotosyntheSound", layout="centered")
st.title("🌿 PhotosyntheSound")

mode = st.radio("Select Mode:", ["🎧 Explore Notes", "🎮 Play-Along Challenge"])
cols = st.columns(7)
note_keys = list(note_map.keys())

if mode == "🎧 Explore Notes":
    st.write("Click a note to play its sound and see its therapeutic effect:")
    for i, key in enumerate(note_keys):
        freq, note_name, effect = note_map[key]
        with cols[i % 7]:
            if st.button(f"{note_name}\n({effect})"):
                st.success(f"🌟 Effect: {effect}")
                play_tone(freq)

    st.subheader("🎶 Songs")
    song_cols = st.columns(3) 
    for idx, song in enumerate(songs):
        with song_cols[idx % 3]:
            if st.button(f"🎼 {song}"):
                st.success(f"Playing: {song}")
                status = st.empty()
                expanded_melody = []
                for key, duration in songs[song]:
                    if duration == 2.0:
                        expanded_melody.append((key, 1.0))
                        expanded_melody.append(("REST", 1.0))
                    else:
                        expanded_melody.append((key, duration))
                for i, (key, duration) in enumerate(expanded_melody):
                    if key == "REST":
                        status.markdown("💤")
                        time.sleep(duration)
                    else:
                        freq, _, _ = note_map.get(key.upper(), (None, None, None))
                        if freq:
                            play_tone(freq, duration=duration)
                            status.markdown("🎵" * ((i % 6) + 2))
                            time.sleep(0.05)
                status.markdown(f"✅ Finished playing {song} 🎶")

    st.subheader("🌱 Plant Melodies")
    plant_cols = st.columns(3) 
    for idx, plant in enumerate(plant_songs):
        with plant_cols[idx % 3]:
            if st.button(f"🌿 {plant}"):
                st.success(f"Playing: {plant}")
                status = st.empty()
                melody = plant_songs[plant]
                for i, (key, duration) in enumerate(melody):
                    freq, _, _ = note_map.get(key.upper(), (None, None, None))
                    if freq:
                        play_tone(freq, duration=duration)
                        status.markdown("🎶" * ((i % 6) + 2))
                        time.sleep(0.05)
                status.markdown(f"🌿 Finished {plant} melody 🌿")

elif mode == "🎮 Play-Along Challenge":
    st.subheader("🎼 Try to play a song yourself!")
    selected_song = st.selectbox("Choose a song to play:", list(songs.keys()))
    target_melody = songs[selected_song]

    if "progress" not in st.session_state:
        st.session_state.progress = 0
        st.session_state.results = []

    if st.session_state.progress >= len(target_melody):
        st.balloons()
        st.success("🎉 You completed the melody!")
        if st.button("🔁 Play Again"):
            st.session_state.progress = 0
            st.session_state.results = []
            st.rerun()
    else:
        expected_key, _ = target_melody[st.session_state.progress]
        _, expected_note_name, _ = note_map.get(expected_key, ("?", "?", "?"))
        st.info(f"🎯 Play note: {expected_note_name}")
        st.markdown("Progress: " + "".join(st.session_state.results))

        for i, key in enumerate(note_keys):
            freq, note_name, _ = note_map[key]
            with cols[i % 7]:
                if st.button(note_name):
                    play_tone(freq)
                    if key == expected_key:
                        st.session_state.results.append("✅")
                        st.success("Correct!")
                    else:
                        st.session_state.results.append("❌")
                        st.error(f"Wrong! That was {key}, expected {expected_key}")
                    st.session_state.progress += 1
                    st.rerun()








