class ChaiUtils:
    @staticmethod
    def Clean_indregents(text):
        return [item.strip() for item in text.split(",")]
    
raw = " water , milk  , ginger  ,  honey  "

object = ChaiUtils()

cleaned = ChaiUtils.Clean_indregents(raw)
print(cleaned)