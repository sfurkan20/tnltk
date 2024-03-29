import string
import warnings
from _builtin import number_to_word
import re 

class Normalizer:

    @staticmethod
    def lower_case(text: str) -> str:
        """
        Converts a string of text to lowercase for Turkish language.
        
        This function handles all Turkish characters which are not handled properly by python lower() method, 
        e.g., "İ" -> "i", "I" -> "ı", "Ğ" -> "ğ", "Ü" -> "ü", "Ö" -> "ö", "Ş" -> "ş", "Ç" -> "ç".

        Parameters
        ----------
        text : str 
            Input text.

        Returns
        -------
        output : str
            Text in lowercase form.

        Example:
        --------
        >>> from tnltk import Normalizer
        >>> Normalizer.lower_case("Ex: İIĞÜÖŞÇ")
        'ex: iığüöşç'
        """
        turkish_lowercase_dict = {"İ": "i", "I": "ı", "Ğ": "ğ", "Ü": "ü", "Ö": "ö", "Ş": "ş", "Ç": "ç"}
        for k, v in turkish_lowercase_dict.items():
            text = text.replace(k, v)
        return text.lower()

    @staticmethod
    def remove_punctuations(text: str)-> str:
        """
        Removes punctuations (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~) from the given string.
        
        This function removes all the punctuation characters from the given text.

        Parameters
        ----------
        text : str 
            Input text.

        Returns
        -------
        output : str
            Text stripped from punctuations.

        Example:
        --------
        >>> from tnltk import Normalizer
        >>> Normalizer.remove_punctuations("#Merhaba, Dünya!")
        'Merhaba Dünya'
        """
        return re.sub(f'[{string.punctuation}]', '', text)


    @staticmethod
    def remove_accent_marks(text: str)-> str:
        """
        Removes accent marks from the given string.

        Parameters
        ----------
        text : str 
            Input text.

        Returns
        -------
        text : str
            Text stripped from accent marks.

        Example:
        --------
        >>> from tnltk import Normalizer
        >>> Normalizer.remove_accent_marks("merhâbâ")
        'merhaba'
        """
        accent_marks = {'â':'a', 'ô':'o', 'î':'ı', 'ê':'e', 'û':'u',
                        'Â':'A', 'Ô':'o', 'Î':'ı', 'Ê':'e', 'Û': 'u'}
        for mark, letter in accent_marks.items():
            text = text.replace(mark, letter)
        return text


    @staticmethod
    def convert_text_numbers(text):
        def convert_number(match):
            number = float(match.group(0).replace(",", "."))
            if number == int(number):
                return number_to_word(int(number)).replace("", "")
            else:
                return warnings.warn("In Turkish language, decimal numbers are expressed with commas.")
        return re.sub(r"[-+]?\d*.\d+|\d+", convert_number, text.replace(',', ' virgül '))