
# Problem statement is as follows.

# Create a reusable library and a REST API based service that can convert a paragraph of spoken english to written english. For example, "two dollars" should be converted to $2. 
#Abbreviations spoken as "H T M L" or "Triple A" should be written as "HTML" and "AAA" respectively. Note that we are not asking you to convert audio to text; 
#just convert a raw transcript from spoken English to written English. Push your code and documentation to a public github/gitlab/bitbucket repo and submit the link here. 
#Repo must contain a README.md which details the features you have implemented, 
#features you can think of but are yet to implement and instructions for using your code as a library and for invoking your REST service.

# As here we need to convert raw transcript from spoken English to written English, 
# we wont be using any test recognition external libreries or ML/DL model, rather we will try to do with normal program.


# Maintain dict for convertion. (External API can be called or we can download complate resource/ use database)

class SpeechConverter:

    __numbers = {
        'one': 1,
        'single': 1,
        'two': 2,
        'double': 2,
        'three': 3,
        'triple': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        # We can add more for future use
    }

    __currency = {
        'dollar': '$',
        'rupee': '₹',
        'euro': '€',
        'pound': '£',
        # More currencies can be added later
    }

    def getText(self, ipText):
        """This fucntion take a spoken text as input and returns writen text of it"""
        
        # If text contain a single character, simply return the same
        if len(ipText) == 1:
            return ipText
            
        # Divide the sentence into words
        texts = ipText.split(' ')
        
        # If multiple characters are separated by space, join them and return
        if all([len(i) == 1 for i in texts]):
            return ''.join(texts)
        
        # If we have a single word, we can return the same or return after convertion
        if len(texts) == 1:
            text = texts[0]
            if text not in ['double', 'triple'] and SpeechConverter.__numbers.get(text) is not None:
                return SpeechConverter.__numbers.get(text)
            return text
                
        opTextList = []
        i = 0
        while i < len(texts):
            text = texts[i]
            opText = text
            if i+1 < len(texts):
                nextText = texts[i+1]
                if SpeechConverter.__numbers.get(text) is not None:
                    val = SpeechConverter.__numbers.get(text)
                    
                    if len(nextText) == 1:
                        opText = nextText * val
                        i += 1
                    else:
                        nextText_s = nextText[:-1] if nextText[-1].lower() == 's' else None
                        cur_val = None
                        if SpeechConverter.__currency.get(nextText) is not None:
                            cur_val = SpeechConverter.__currency.get(nextText)
                        elif SpeechConverter.__currency.get(nextText_s) is not None:
                            cur_val = SpeechConverter.__currency.get(nextText_s)     
                        
                        if cur_val is not None:
                            opText = cur_val + str(val)
                            i += 1

            opTextList.append(opText)
            i += 1
         
        return ' '.join(opTextList)