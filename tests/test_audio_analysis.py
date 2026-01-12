import unittest
from app.services.audio_analysis import analyze_audio

class TestAudioAnalysis(unittest.TestCase):
    def test_analyze_audio(self):
        with open('tests/sample.wav', 'rb') as f:
            audio_bytes = f.read()
        result = analyze_audio(audio_bytes)
        self.assertIn('Analysis complete', result)

if __name__ == '__main__':
    unittest.main()