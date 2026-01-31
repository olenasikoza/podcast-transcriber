#!/usr/bin/env python3
"""
🎧 Podcast Transcriber for macOS
Version with all macOS-specific fixes
"""

import os
import sys
import subprocess

def check_command(command):
    """Check if command is available"""
    try:
        subprocess.run([command, '--version'], 
                      capture_output=True, 
                      check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_package(package_name):
    """Install Python package"""
    print(f"⚠️  Installing {package_name}...")
    
    # Try different pip variants
    pip_commands = ['pip3', 'pip', 'python3 -m pip', 'python -m pip']
    
    for pip_cmd in pip_commands:
        try:
            cmd = f"{pip_cmd} install {package_name} --break-system-packages -q"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ {package_name} installed")
                return True
        except Exception:
            continue
    
    print(f"❌ Failed to install {package_name}")
    return False

print("=" * 70)
print(" " * 20 + "🎧 PODCAST TRANSCRIBER")
print(" " * 25 + "for macOS")
print("=" * 70)
print()

# Check Python
print("🔍 Checking system...")
if not (check_command('python3') or check_command('python')):
    print("❌ Python not found!")
    print("\n📦 Install Python:")
    print("   brew install python")
    print("\nOr download from: https://www.python.org/downloads/")
    sys.exit(1)
print("✅ Python found")

# Check ffmpeg
if not check_command('ffmpeg'):
    print("⚠️  ffmpeg not found (required for Whisper)")
    print("\n📦 Install ffmpeg:")
    print("   brew install ffmpeg")
    print("\nAfter installation, run the script again.")
    
    response = input("\nContinue without ffmpeg? (may not work) [y/N]: ")
    if response.lower() != 'y':
        sys.exit(1)
else:
    print("✅ ffmpeg found")

print()
print("=" * 70)
print("📦 Checking Python libraries...")
print("=" * 70)
print()

# Check and install requests
try:
    import requests
    print("✅ requests installed")
except ImportError:
    if not install_package('requests'):
        print("\n❌ Failed to install requests")
        print("Try manually: pip3 install requests --break-system-packages")
        sys.exit(1)
    import requests

# Check and install whisper
try:
    import whisper
    print("✅ whisper installed")
except ImportError:
    print("⚠️  Installing openai-whisper (this will take time)...")
    print("    Size: ~1 GB with dependencies")
    
    response = input("\nContinue with installation? [Y/n]: ")
    if response.lower() == 'n':
        print("\n💡 Install manually:")
        print("   pip3 install openai-whisper --break-system-packages")
        sys.exit(0)
    
    if not install_package('openai-whisper'):
        print("\n❌ Failed to install whisper")
        print("Try manually: pip3 install openai-whisper --break-system-packages")
        sys.exit(1)
    import whisper

print()
print("=" * 70)
print("✅ All dependencies installed!")
print("=" * 70)
print()

# Get URL
if len(sys.argv) > 1:
    audio_url = sys.argv[1]
    print(f"📥 Will transcribe: {audio_url[:60]}...")
else:
    print("💡 HOW TO USE:")
    print()
    print("python3 demo_transcribe_macos.py 'https://example.com/podcast.mp3'")
    print()
    print("=" * 70)
    print("📝 STEP-BY-STEP GUIDE:")
    print("=" * 70)
    print()
    print("1. Find podcast in Apple Podcasts in browser")
    print("2. Open Developer Tools (Cmd + Option + I)")
    print("3. 'Network' tab")
    print("4. Press Play on podcast")
    print("5. Find .mp3 file (usually the largest)")
    print("6. Right-click → Copy → Copy Link Address")
    print("7. Run script with this link")
    print()
    print("=" * 70)
    print()
    print("OR use Otter.ai (easier!):")
    print("   → https://otter.ai")
    print("   → Upload MP3")
    print("   → Get text in 3 minutes")
    print()
    sys.exit(0)

# Download audio
print()
print("=" * 70)
print("📥 STEP 1: Downloading audio")
print("=" * 70)
print()

audio_file = "podcast_temp.mp3"

try:
    print("⏳ Downloading... (this may take several minutes)")
    
    response = requests.get(audio_url, stream=True, timeout=120)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    downloaded = 0
    
    with open(audio_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                
                if total_size > 0:
                    percent = (downloaded / total_size) * 100
                    mb_downloaded = downloaded / (1024 * 1024)
                    mb_total = total_size / (1024 * 1024)
                    print(f"\r⏳ {mb_downloaded:.1f}/{mb_total:.1f} MB ({percent:.1f}%)", end="")
    
    print()
    file_size = os.path.getsize(audio_file) / (1024 * 1024)
    print(f"✅ Downloaded: {file_size:.1f} MB")
    
    # Estimate duration (rough)
    estimated_minutes = file_size / 1.0  # rough estimate: ~1 MB = ~1 minute
    print(f"📊 Estimated duration: ~{estimated_minutes:.0f} minutes")
    
except Exception as e:
    print(f"\n❌ Download error: {e}")
    print("\n💡 Check:")
    print("   • Internet connection")
    print("   • URL correctness")
    print("   • File availability")
    sys.exit(1)

# Transcribe
print()
print("=" * 70)
print("🎙️  STEP 2: Transcription")
print("=" * 70)
print()

try:
    print("⏳ Loading Whisper 'base' model...")
    print("   (First run will download ~140 MB)")
    
    model = whisper.load_model("base")
    print("✅ Model loaded")
    
    print()
    print("⏳ Starting transcription...")
    print("   This will take approximately 20-30 minutes for 1-hour podcast")
    print("   You can step away, grab some coffee ☕")
    print()
    
    result = model.transcribe(audio_file, language="en", verbose=True)
    
    print()
    print("✅ Transcription complete!")
    
    # Save result
    output_file = "transcript.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print()
    print("=" * 70)
    print("📊 STATISTICS:")
    print("=" * 70)
    print(f"📄 File: {output_file}")
    print(f"📏 Characters: {len(result['text']):,}")
    print(f"📝 Words: {len(result['text'].split()):,}")
    print(f"📍 Location: {os.path.abspath(output_file)}")
    
    # Show preview
    print()
    print("=" * 70)
    print("📝 PREVIEW (first 500 characters):")
    print("=" * 70)
    print()
    print(result["text"][:500])
    if len(result["text"]) > 500:
        print("...")
    
    # Remove temporary file
    print()
    if os.path.exists(audio_file):
        os.remove(audio_file)
        print("🗑️  Temporary audio file deleted")
    
    print()
    print("=" * 70)
    print("✨ DONE! Transcript saved!")
    print("=" * 70)
    print()
    print(f"Open file: open {output_file}")
    print()

except KeyboardInterrupt:
    print("\n\n⚠️  Interrupted by user")
    if os.path.exists(audio_file):
        os.remove(audio_file)
    sys.exit(0)

except Exception as e:
    print(f"\n❌ Transcription error: {e}")
    print("\n💡 Possible solutions:")
    print("   • Make sure ffmpeg is installed: brew install ffmpeg")
    print("   • Try reinstalling whisper:")
    print("     pip3 uninstall openai-whisper")
    print("     pip3 install openai-whisper --break-system-packages")
    
    if os.path.exists(audio_file):
        os.remove(audio_file)
    sys.exit(1)
