#!/usr/bin/env python3
"""
🎙️ Транскрибация локальных аудио файлов
С таймкодами и красивым форматированием!
"""

import whisper
import sys
import os

print("=" * 70)
print(" " * 15 + "🎙️ LOCAL FILE TRANSCRIBER v2.0")
print(" " * 18 + "(с таймкодами и абзацами)")
print("=" * 70)
print()

# Получаем имя файла
if len(sys.argv) < 2:
    print("💡 КАК ИСПОЛЬЗОВАТЬ:")
    print()
    print("python3 transcribe_local_v2.py 'имя_файла.mp3'")
    print()
    print("ИЛИ просто перетащите файл в Terminal после команды:")
    print("python3 transcribe_local_v2.py [перетащите файл сюда]")
    print()
    sys.exit(0)

audio_file = sys.argv[1]

# Проверяем существование файла
if not os.path.exists(audio_file):
    print(f"❌ Файл не найден: {audio_file}")
    print()
    print("💡 Убедитесь что:")
    print("   • Файл находится в текущей папке")
    print("   • ИЛИ указан полный путь")
    print("   • Название написано правильно")
    print()
    sys.exit(1)

# Показываем информацию о файле
file_size = os.path.getsize(audio_file) / (1024 * 1024)
print(f"📁 Файл: {audio_file}")
print(f"💾 Размер: {file_size:.1f} MB")
print(f"📊 Примерная длительность: ~{file_size:.0f} минут")
print()

# Загружаем модель
print("=" * 70)
print("🎙️  ТРАНСКРИПЦИЯ")
print("=" * 70)
print()
print("⏳ Загружаю модель Whisper 'base'...")

try:
    model = whisper.load_model("base")
    print("✅ Модель загружена")
except Exception as e:
    print(f"❌ Ошибка загрузки модели: {e}")
    print()
    print("💡 Попробуйте установить заново:")
    print("   pip3 install openai-whisper --break-system-packages")
    sys.exit(1)

# Транскрибируем
print()
print("🔄 Начинаю транскрипцию...")
print("   (это займет примерно 20-30 минут для часового аудио)")
print()

try:
    result = model.transcribe(audio_file, language="en", verbose=True)
    
    # Создаем ТРИ файла
    output_clean = "transcript_clean.txt"
    output_paragraphs = "transcript_paragraphs.txt"
    output_timestamps = "transcript_timestamps.txt"
    
    # 1. Чистый текст (сплошной)
    with open(output_clean, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    # 2. С абзацами (каждый сегмент = абзац)
    with open(output_paragraphs, "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write("ТРАНСКРИПЦИЯ С АБЗАЦАМИ\n")
        f.write("=" * 70 + "\n\n")
        
        for segment in result["segments"]:
            text = segment["text"].strip()
            if text:
                f.write(text)
                f.write("\n\n")
    
    # 3. С таймкодами
    with open(output_timestamps, "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write("ТРАНСКРИПЦИЯ С ТАЙМКОДАМИ\n")
        f.write("=" * 70 + "\n\n")
        
        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"].strip()
            
            # Форматируем время в минуты:секунды
            start_min = int(start // 60)
            start_sec = int(start % 60)
            end_min = int(end // 60)
            end_sec = int(end % 60)
            
            if text:
                f.write(f"[{start_min:02d}:{start_sec:02d} - {end_min:02d}:{end_sec:02d}] {text}\n\n")
    
    # Статистика
    print()
    print("=" * 70)
    print("✅ ГОТОВО!")
    print("=" * 70)
    print()
    print(f"📄 Создано 3 файла:")
    print(f"   1. {output_clean}")
    print(f"      → Чистый текст (сплошной)")
    print()
    print(f"   2. {output_paragraphs} ⭐")
    print(f"      → С абзацами (удобно читать)")
    print()
    print(f"   3. {output_timestamps}")
    print(f"      → С таймкодами (удобно навигировать)")
    print()
    print(f"📍 Расположение: {os.path.abspath('.')}")
    print(f"📊 Символов: {len(result['text']):,}")
    print(f"📝 Слов: {len(result['text'].split()):,}")
    print(f"⏱️  Сегментов: {len(result['segments'])}")
    print()
    
    # Превью из версии с абзацами
    print("=" * 70)
    print("📝 ПРЕВЬЮ (первые 3 абзаца):")
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
    print("✨ Транскрипция завершена!")
    print("=" * 70)
    print()
    print(f"📖 Откройте для чтения:    open {output_paragraphs}")
    print(f"🕐 С таймкодами:            open {output_timestamps}")
    print()
    
except KeyboardInterrupt:
    print("\n\n⚠️  Прервано пользователем")
    sys.exit(0)
    
except Exception as e:
    print(f"\n❌ Ошибка транскрипции: {e}")
    print()
    print("💡 Возможные решения:")
    print("   • Проверьте, что файл не поврежден")
    print("   • Убедитесь, что ffmpeg установлен: brew install ffmpeg")
    print("   • Попробуйте другой аудио файл")
    sys.exit(1)