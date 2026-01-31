#!/usr/bin/env python3
"""
🎙️ Local Audio File Transcription
Creates transcripts with timestamps and beautiful formatting
"""

import whisper
import sys
import os

print("=" * 70)
print(" " * 15 + "🎙️ LOCAL FILE TRANSCRIBER v2.0")
print(" " * 18 + "(with timestamps and paragraphs)")
print("=" * 70)
print()

# Get filename from arguments
if len(sys.argv) < 2:
    print("💡 HOW TO USE:")
    print()
    print("python3 transcribe_local_v2.py 'filename.mp3'")
    print()
    print("OR simply drag the file into Terminal after the command:")
    print("python3 transcribe_local_v2.py [drag file here]")
    print()
    sys.exit(0)

audio_file = sys.argv[1]

# Check if file exists
if not os.path.exists(audio_file):
    print(f"❌ File not found: {audio_file}")
    print()
    print("💡 Make sure that:")
    print("   • File is in the current folder")
    print("   • OR full path is specified")
    print("   • Filename is spelled correctly")
    print()
    sys.exit(1)

# Display file information
file_size = os.path.getsize(audio_file) / (1024 * 1024)
print(f"📁 File: {audio_file}")
print(f"💾 Size: {file_size:.1f} MB")
print(f"📊 Estimated duration: ~{file_size:.0f} minutes")
print()

# Load Whisper model
print("=" * 70)
print("🎙️  TRANSCRIPTION")
print("=" * 70)
print()
print("⏳ Loading Whisper 'base' model...")

try:
    model = whisper.load_model("base")
    print("✅ Model loaded")
except Exception as e:
    print(f"❌ Model loading error: {e}")
    print()
    print("💡 Try reinstalling:")
    print("   pip3 install openai-whisper --break-system-packages")
    sys.exit(1)

# Start transcription
print()
print("🔄 Starting transcription...")
print("   (this will take approximately 20-30 minutes for 1-hour audio)")
print()

try:
    result = model.transcribe(audio_file, language="en", verbose=True)
    
    # Create THREE files
    output_clean = "transcript_clean.txt"
    output_paragraphs = "transcript_paragraphs.txt"
    output_timestamps = "transcript_timestamps.txt"
    
    # 1. Clean text (continuous)
    with open(output_clean, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    # 2. With paragraphs (each segment = paragraph)
    with open(output_paragraphs, "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write("TRANSCRIPT WITH PARAGRAPHS\n")
        f.write("=" * 70 + "\n\n")
        
        for segment in result["segments"]:
            text = segment["text"].strip()
            if text:
                f.write(text)
                f.write("\n\n")
    
    # 3. With timestamps
    with open(output_timestamps, "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write("TRANSCRIPT WITH TIMESTAMPS\n")
        f.write("=" * 70 + "\n\n")
        
        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"].strip()
            
            # Format time as minutes:seconds
            start_min = int(start // 60)
            start_sec = int(start % 60)
            end_min = int(end // 60)
            end_sec = int(end % 60)
            
            if text:
                f.write(f"[{start_min:02d}:{start_sec:02d} - {end_min:02d}:{end_sec:02d}] {text}\n\n")
    
    # Statistics
    print()
    print("=" * 70)
    print("✅ DONE!")
    print("=" * 70)
    print()
    print(f"📄 Created 3 files:")
    print(f"   1. {output_clean}")
    print(f"      → Clean text (continuous)")
    print()
    print(f"   2. {output_paragraphs} ⭐")
    print(f"      → With paragraphs (easy to read)")
    print()
    print(f"   3. {output_timestamps}")
    print(f"      → With timestamps (easy to navigate)")
    print()
    print(f"📍 Location: {os.path.abspath('.')}")
    print(f"📊 Characters: {len(result['text']):,}")
    print(f"📝 Words: {len(result['text'].split()):,}")
    print(f"⏱️  Segments: {len(result['segments'])}")
    print()
    
    # Preview from paragraph version
    print("=" * 70)
    print("📝 PREVIEW (first 3 paragraphs):")
    print("=" * 70)
    print()
    
    preview_count = 0
    for segment in result["segments"]:
        text = segment["text"].strip()
        if text and preview_count < 3:
            print(text)
            print()
            preview_count += 1
    
    if len(result["segments"]) > 3:
        print("...")
    print()
    
    print("=" * 70)
    print("✨ Transcription complete!")
    print("=" * 70)
    print()
    print(f"📖 Open for reading:    open {output_paragraphs}")
    print(f"🕐 With timestamps:      open {output_timestamps}")
    print()
    
except KeyboardInterrupt:
    print("\n\n⚠️  Interrupted by user")
    sys.exit(0)
    
except Exception as e:
    print(f"\n❌ Transcription error: {e}")
    print()
    print("💡 Possible solutions:")
    print("   • Check that the file is not corrupted")
    print("   • Make sure ffmpeg is installed: brew install ffmpeg")
    print("   • Try a different audio file")
    sys.exit(1)
