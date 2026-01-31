#!/usr/bin/env python3
"""
🎧 Podcast Transcriber для macOS
Версия с учетом всех macOS особенностей
"""

import os
import sys
import subprocess

def check_command(command):
    """Проверяет, доступна ли команда"""
    try:
        subprocess.run([command, '--version'], 
                      capture_output=True, 
                      check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_package(package_name):
    """Устанавливает Python пакет"""
    print(f"⚠️  Устанавливаю {package_name}...")
    
    # Пробуем разные варианты pip
    pip_commands = ['pip3', 'pip', 'python3 -m pip', 'python -m pip']
    
    for pip_cmd in pip_commands:
        try:
            cmd = f"{pip_cmd} install {package_name} --break-system-packages -q"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ {package_name} установлен")
                return True
        except Exception:
            continue
    
    print(f"❌ Не удалось установить {package_name}")
    return False

print("=" * 70)
print(" " * 20 + "🎧 PODCAST TRANSCRIBER")
print(" " * 25 + "для macOS")
print("=" * 70)
print()

# Проверка Python
print("🔍 Проверяю систему...")
if not (check_command('python3') or check_command('python')):
    print("❌ Python не найден!")
    print("\n📦 Установите Python:")
    print("   brew install python")
    print("\nИли скачайте с: https://www.python.org/downloads/")
    sys.exit(1)
print("✅ Python найден")

# Проверка ffmpeg
if not check_command('ffmpeg'):
    print("⚠️  ffmpeg не найден (нужен для Whisper)")
    print("\n📦 Установите ffmpeg:")
    print("   brew install ffmpeg")
    print("\nПосле установки запустите скрипт снова.")
    
    response = input("\nПродолжить без ffmpeg? (может не работать) [y/N]: ")
    if response.lower() != 'y':
        sys.exit(1)
else:
    print("✅ ffmpeg найден")

print()
print("=" * 70)
print("📦 Проверяю Python библиотеки...")
print("=" * 70)
print()

# Проверка и установка requests
try:
    import requests
    print("✅ requests установлен")
except ImportError:
    if not install_package('requests'):
        print("\n❌ Не удалось установить requests")
        print("Попробуйте вручную: pip3 install requests --break-system-packages")
        sys.exit(1)
    import requests

# Проверка и установка whisper
try:
    import whisper
    print("✅ whisper установлен")
except ImportError:
    print("⚠️  Устанавливаю openai-whisper (это займет время)...")
    print("    Размер: ~1 GB с зависимостями")
    
    response = input("\nПродолжить установку? [Y/n]: ")
    if response.lower() == 'n':
        print("\n💡 Установите вручную:")
        print("   pip3 install openai-whisper --break-system-packages")
        sys.exit(0)
    
    if not install_package('openai-whisper'):
        print("\n❌ Не удалось установить whisper")
        print("Попробуйте вручную: pip3 install openai-whisper --break-system-packages")
        sys.exit(1)
    import whisper

print()
print("=" * 70)
print("✅ Все зависимости установлены!")
print("=" * 70)
print()

# Получаем URL
if len(sys.argv) > 1:
    audio_url = sys.argv[1]
    print(f"📥 Буду транскрибировать: {audio_url[:60]}...")
else:
    print("💡 КАК ИСПОЛЬЗОВАТЬ:")
    print()
    print("python3 demo_transcribe_macos.py 'https://example.com/podcast.mp3'")
    print()
    print("=" * 70)
    print("📝 ПОШАГОВАЯ ИНСТРУКЦИЯ:")
    print("=" * 70)
    print()
    print("1. Найдите подкаст в Apple Podcasts в браузере")
    print("2. Откройте Developer Tools (Cmd + Option + I)")
    print("3. Вкладка 'Network'")
    print("4. Нажмите Play на подкасте")
    print("5. Найдите файл .mp3 (обычно самый большой)")
    print("6. Правой кнопкой → Copy → Copy Link Address")
    print("7. Запустите скрипт с этой ссылкой")
    print()
    print("=" * 70)
    print()
    print("ИЛИ используйте Otter.ai (проще!):")
    print("   → https://otter.ai")
    print("   → Загрузите MP3")
    print("   → Получите текст за 3 минуты")
    print()
    sys.exit(0)

# Скачиваем аудио
print()
print("=" * 70)
print("📥 ШАГ 1: Скачивание аудио")
print("=" * 70)
print()

audio_file = "podcast_temp.mp3"

try:
    print("⏳ Скачиваю... (это может занять несколько минут)")
    
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
    print(f"✅ Скачано: {file_size:.1f} MB")
    
    # Оцениваем длительность (примерно)
    estimated_minutes = file_size / 1.0  # грубая оценка: ~1 MB = ~1 минута
    print(f"📊 Примерная длительность: ~{estimated_minutes:.0f} минут")
    
except Exception as e:
    print(f"\n❌ Ошибка скачивания: {e}")
    print("\n💡 Проверьте:")
    print("   • Интернет-соединение")
    print("   • Правильность URL")
    print("   • Доступность файла")
    sys.exit(1)

# Транскрибируем
print()
print("=" * 70)
print("🎙️  ШАГ 2: Транскрипция")
print("=" * 70)
print()

try:
    print("⏳ Загружаю модель Whisper 'base'...")
    print("   (При первом запуске скачается ~140 MB)")
    
    model = whisper.load_model("base")
    print("✅ Модель загружена")
    
    print()
    print("⏳ Начинаю транскрипцию...")
    print("   Это займет примерно 20-30 минут для часового подкаста")
    print("   Можете отойти, попить чай ☕")
    print()
    
    result = model.transcribe(audio_file, language="en", verbose=True)
    
    print()
    print("✅ Транскрипция завершена!")
    
    # Сохраняем результат
    output_file = "transcript.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print()
    print("=" * 70)
    print("📊 СТАТИСТИКА:")
    print("=" * 70)
    print(f"📄 Файл: {output_file}")
    print(f"📏 Символов: {len(result['text']):,}")
    print(f"📝 Слов: {len(result['text'].split()):,}")
    print(f"📍 Расположение: {os.path.abspath(output_file)}")
    
    # Показываем превью
    print()
    print("=" * 70)
    print("📝 ПРЕВЬЮ (первые 500 символов):")
    print("=" * 70)
    print()
    print(result["text"][:500])
    if len(result["text"]) > 500:
        print("...")
    
    # Удаляем временный файл
    print()
    if os.path.exists(audio_file):
        os.remove(audio_file)
        print("🗑️  Временный аудиофайл удален")
    
    print()
    print("=" * 70)
    print("✨ ГОТОВО! Транскрипция сохранена!")
    print("=" * 70)
    print()
    print(f"Откройте файл: open {output_file}")
    print()

except KeyboardInterrupt:
    print("\n\n⚠️  Прервано пользователем")
    if os.path.exists(audio_file):
        os.remove(audio_file)
    sys.exit(0)

except Exception as e:
    print(f"\n❌ Ошибка транскрипции: {e}")
    print("\n💡 Возможные решения:")
    print("   • Убедитесь, что ffmpeg установлен: brew install ffmpeg")
    print("   • Попробуйте переустановить whisper:")
    print("     pip3 uninstall openai-whisper")
    print("     pip3 install openai-whisper --break-system-packages")
    
    if os.path.exists(audio_file):
        os.remove(audio_file)
    sys.exit(1)
