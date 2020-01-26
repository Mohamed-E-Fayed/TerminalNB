from enum import Enum 
class ProgrammingLanguages(Enum): 
    py = -1
    py3 = 0
    py2 = 1
    c = 2
    cpp = 3 
    
    @classmethod 
    def set_default_python(self, version):
        if version==2:
            self.py = self.py2
        elif version ==3:
            self.py = self.py3


    @classmethod 
    def sset_default_language(lang):
        """
        This function makes the selected language as the default language for creating new cell
        #continue s
        """
        return lang



#main for test

print(ProgrammingLanguages['py3'].name)
