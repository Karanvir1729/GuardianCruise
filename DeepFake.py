from elevenlabs import generate, play, save, set_api_key
set_api_key("1bd01d835b2876b35376769cfe4514b8")

audio = generate(
  text="Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!",
  voice="Rachel",
  model="eleven_multilingual_v2"
)

save(audio, "Attempt one.wav")

from elevenlabs import Voice, VoiceDesign, Gender, Age, Accent, play

# Build a voice deisgn object
design = VoiceDesign(
    name='Lexa',
    text="Hello, I am an old british lady. Are you drunk? I think you might be drunk. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    voice_description="Calm and soft with a slight British accent.",
    gender=Gender.female,
    age=Age.old,
    accent=Accent.british,
    accent_strength=1.9,
)

# Generate audio from the design, and play it to test if it sounds good (optional)
audio = design.generate()
save(audio, "Oldlady.wav")

# Convert design to usable voice
voice = Voice.from_design(design)