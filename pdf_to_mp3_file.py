from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path, language):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        with pdfplumber.PDF(open(file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text.replace('\n', ' ')
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'{file_name}.mp3 saved.'
    else:
        return 'File not exists.'


print(pdf_to_mp3('test.pdf', 'en'))
