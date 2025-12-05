from transformers import pipeline

translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M",
    src_lang="rus_Cyrl",  # русский
    tgt_lang="eng_Latn"   # английский
)

result = translator("Привет, как дела?")
print(result[0]['translation_text'])  # "Hi, how are you?"