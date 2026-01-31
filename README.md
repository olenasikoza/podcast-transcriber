# Podcast Transcriber

**From hours of listening to minutes of reading | Від годин прослуховування до хвилин читання**

Transform any audio or video content into text with timestamps. Read podcasts in 10 minutes instead of listening for 45. Built for people who prefer reading over listening.

[🇺🇦 Українська версія нижче](#українська-версія)

---

## 🎯 The Problem

**The "Watch Later" Hell:**

You have 20+ podcasts saved "for later"  
Each episode is 45-60 minutes  
That's 15+ hours of content  
You'll never listen to all of them

**Why audio/video is inefficient:**
- ⏰ Can't scan content quickly
- 🔍 Can't search for specific moments
- 📝 Hard to take structured notes
- 🧠 Forget 80% after a week
- ⚡ Forced to listen at speaker's pace

---

## ✨ The Solution

**Stop listening. Start reading.**

This tool transcribes any audio/video file into text with timestamps in 15-20 minutes.

**What you get:**
- Full transcript with paragraph breaks
- Timestamps for navigation
- Searchable text (Ctrl+F)
- Ready for AI analysis
- Shareable with your team

**Real example:**
- 45-minute podcast → 18 minutes transcription
- Read in 10 minutes vs 45 listening
- AI summary in 3 minutes
- Total: 31 minutes vs 45 minutes
- **Plus** you remember everything

---

## 🛠️ How It Works

### The Process:

1. **Download** your podcast/video (MP3, MP4, etc.)
2. **Run the script** (automatic transcription)
3. **Get 3 files:**
   - `transcript_clean.txt` - plain text
   - `transcript_paragraphs.txt` - with paragraphs
   - `transcript_timestamps.txt` - with timestamps

### Technologies:

- **OpenAI Whisper** - AI transcription model
- **Python** - automation
- **ffmpeg** - audio processing
- Works offline, free, no API keys needed

---

## 🚀 Quick Start

### Prerequisites

- macOS or Windows
- Python 3.x
- 15-20 minutes for first-time setup

### Installation (macOS)

**Step 1: Install Command Line Tools**

```bash
xcode-select --install
```

**Step 2: Install Required Libraries**

```bash
pip3 install openai-whisper --break-system-packages
```

**Step 3: Install ffmpeg**

```bash
brew install ffmpeg
```

If you don't have Homebrew:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Installation (Windows)

**Step 1: Install Python Libraries**

```bash
pip install openai-whisper
```

**Step 2: Install ffmpeg**

Download from: https://ffmpeg.org/download.html

---

## 📖 Usage

### For Local Files (Recommended)

```bash
# Navigate to your folder
cd ~/Downloads/Podcasts

# Run transcription
python3 transcribe_local_v2.py 'your-podcast.mp3'
```

**Or drag & drop:**
1. Type: `python3 transcribe_local_v2.py `
2. Drag your MP3 file into Terminal
3. Press Enter

### For URLs (YouTube, etc.)

```bash
python3 demo_transcribe_macos.py 'https://youtube.com/watch?v=...'
```

---

## 📊 Output Files

### 1. `transcript_clean.txt`
Plain text, no formatting
```
Welcome to today's episode about AI. In this discussion...
```

### 2. `transcript_paragraphs.txt` ⭐
Easy to read, natural breaks
```
Welcome to today's episode about AI.

In this discussion, we'll explore how artificial intelligence is changing...

Let's start with the basics of how these systems work.
```

### 3. `transcript_timestamps.txt`
Navigate to specific moments
```
[00:15 - 00:32] Welcome to today's episode about AI.

[00:32 - 00:58] In this discussion, we'll explore how artificial intelligence...

[00:58 - 01:25] Let's start with the basics of how these systems work.
```

---

## 💡 Use Cases

### 1. Learning & Research 📚
- Read educational podcasts faster
- Search for specific topics (Ctrl+F)
- Share insights with team

### 2. Content Creation 📝
- Extract quotes for social media
- Create blog posts from podcasts
- Generate content ideas

### 3. Multilingual Work 🌍
- Transcribe English podcasts
- Translate to Ukrainian/any language
- Expand content reach

### 4. AI Analysis 🤖
- Feed transcript to ChatGPT/Claude
- "Summarize this in 5 points"
- Extract action items automatically

### 5. Accessibility ♿
- Content for deaf/hard of hearing
- Read in quiet environments
- Text is more accessible than audio

---

## 🔧 Troubleshooting

### macOS: "xcrun error"

**Error:**
```
xcrun: error: invalid active developer path
```

**Solution:**
```bash
xcode-select --install
```

### "ModuleNotFoundError: No module named 'whisper'"

**Solution:**
```bash
pip3 install openai-whisper --break-system-packages
```

### Slow transcription

**Normal speed:**
- 45-min audio = 15-20 min transcription
- First time slower (downloads AI model ~1GB)
- Subsequent runs faster

---

## 📈 Real Results

**Time Comparison:**

| Task | Before | After | Savings |
|------|--------|-------|---------|
| 45-min podcast | 45 min listening | 10 min reading | 78% |
| Taking notes | 15 min | Built-in | 100% |
| Finding quote | Impossible | 30 sec (Ctrl+F) | ∞ |
| Sharing with team | Re-explain | Send file | 95% |
| AI analysis | Manual | 3 min | 90% |

**Total:** 45 minutes → 13 minutes (71% time saved)

---

## 🎓 Advanced Tips

### Use with AI Tools

**ChatGPT/Claude prompt:**
```
Analyze this podcast transcript:

[paste transcript]

1. Summarize in 5 key points
2. Extract actionable advice
3. Identify main themes
4. Find best quotes for LinkedIn
```

### Batch Processing

Process multiple files:
```bash
for file in *.mp3; do
    python3 transcribe_local_v2.py "$file"
done
```

### Translation Workflow

1. Transcribe in original language
2. Use DeepL/Google Translate
3. Share multilingual content

---

## 📝 For Whom This Tool Is Perfect

✅ Content managers who process lots of content  
✅ Marketers who follow industry podcasts  
✅ Researchers who need searchable transcripts  
✅ Teams who share knowledge  
✅ People who prefer reading over listening ("text persons")  
✅ Non-native speakers who read faster than listen  
✅ Anyone with 20+ items in "watch later"  

---

## 🤝 Contributing

Found a bug or have an idea?
- Open an issue
- Submit a pull request
- Share your improvements

---

## 📄 License

MIT License - free to use and modify for any purpose.

---

## 👤 Author

Created by **Olena Sikoza** | Content & SEO Manager @ Bookimed

This tool was developed independently during free time to solve a common problem in content management and learning.

💼 [LinkedIn](https://www.linkedin.com/in/olena-sikoza-880b0a194/) 
🐙 [GitHub](https://github.com/olenasikoza)

---

## 🌟 If This Helped You

⭐ Star this repository  
📢 Share with colleagues  
💬 Tell me your use case in Issues

---

# Українська версія

## 🎯 Проблема

**Купа подкастів у папці "Переглянути пізніше":**

У вас є 20+ подкастів "на потім"  
Кожен епізод 45-60 хвилин  
Це 15+ годин контенту  
Ви ніколи їх не прослухаєте

**Чому аудіо/відео неефективні:**
- ⏰ Не можна швидко просканувати зміст
- 🔍 Не можна знайти конкретний момент
- 📝 Важко робити структуровані нотатки
- 🧠 Забуваєте 80% через тиждень
- ⚡ Змушені слухати в темпі диктора

---

## ✨ Рішення

**Перестаньте слухати. Почніть читати.**

Цей інструмент транскрибує будь-який аудіо/відео файл у текст з таймкодами за 15-20 хвилин.

**Що ви отримуєте:**
- Повний транскрипт з абзацами
- Таймкоди для навігації
- Текст, в якому можна шукати (Ctrl+F)
- Готовий для AI аналізу
- Можна поділитися з командою

**Реальний приклад:**
- 45-хвилинний подкаст → 18 хвилин транскрибації
- Читання за 10 хвилин замість 45 прослуховування
- AI summary за 3 хвилини
- Загалом: 31 хвилина проти 45 хвилин
- **Плюс** ви пам'ятаєте все

---

## 🛠️ Як це працює

### Процес:

1. **Завантажте** ваш подкаст/відео (MP3, MP4, тощо)
2. **Запустіть скрипт** (автоматична транскрибація)
3. **Отримайте 3 файли:**
   - `transcript_clean.txt` - чистий текст
   - `transcript_paragraphs.txt` - з абзацами
   - `transcript_timestamps.txt` - з таймкодами

---

## 🚀 Швидкий старт

### Встановлення (macOS)

**Крок 1: Встановіть Command Line Tools**

```bash
xcode-select --install
```

**Крок 2: Встановіть бібліотеки**

```bash
pip3 install openai-whisper --break-system-packages
```

**Крок 3: Встановіть ffmpeg**

```bash
brew install ffmpeg
```

---

## 📖 Використання

### Для локальних файлів

```bash
# Перейдіть до папки з файлами
cd ~/Downloads/Podcasts

# Запустіть транскрибацію
python3 transcribe_local_v2.py 'ваш-подкаст.mp3'
```

**Або перетягніть файл:**
1. Наберіть: `python3 transcribe_local_v2.py `
2. Перетягніть MP3 у Terminal
3. Натисніть Enter

---

## 📊 Результати

**Порівняння часу:**

| Задача | Раніше | Тепер | Економія |
|--------|--------|-------|----------|
| 45-хв подкаст | 45 хв прослуховування | 10 хв читання | 78% |
| Нотатки | 15 хв | Вбудовано | 100% |
| Пошук цитати | Неможливо | 30 сек (Ctrl+F) | ∞ |
| Поділитися з командою | Переказати | Відправити файл | 95% |

**Загалом:** 45 хвилин → 13 хвилин (економія 71%)

---

## 💡 Випадки використання

### 1. Навчання та дослідження 📚
- Читайте освітні подкасти швидше
- Шукайте конкретні теми (Ctrl+F)
- Діліться інсайтами з командою

### 2. Створення контенту 📝
- Витягуйте цитати для соцмереж
- Створюйте статті з подкастів
- Генеруйте ідеї контенту

### 3. Багатомовна робота 🌍
- Транскрибуйте англійські подкасти
- Перекладайте українською
- Розширюйте охоплення контенту

### 4. AI аналіз 🤖
- Використовуйте ChatGPT/Claude
- "Підсумуй це за 5 пунктами"
- Витягуйте action items автоматично

---

## 📝 Для кого цей інструмент

✅ Контент-менеджери  
✅ Маркетологи  
✅ Дослідники  
✅ Команди, які діляться знаннями  
✅ Люди, які краще сприймають текст  
✅ Ті, у кого 20+ елементів у "переглянути пізніше"  

---

## 🔧 Вирішення проблем

### macOS: помилка xcrun

```bash
xcode-select --install
```

### Модуль whisper не знайдено

```bash
pip3 install openai-whisper --break-system-packages
```

---

## 📄 Ліцензія

MIT License - вільно використовуйте та модифікуйте.

---

## 👤 Автор

**Олена Сікоза** | Content & SEO Manager @ Bookimed

Цей інструмент розроблено у вільний час для вирішення типової проблеми в контент-менеджменті та навчанні.

💼 [LinkedIn](https://www.linkedin.com/in/olena-sikoza-880b0a194/)  
🐙 [GitHub](https://github.com/olenasikoza)

---

**⭐ Якщо цей проект допоміг вам - поставте зірочку!**
