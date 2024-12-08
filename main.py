## main стартовый модуль проекта

from functions import process_documents

def main():
    #TODO-сделай вызов функций из functions
    dir = "documents"
    files = ["1.docx", "2.docx", "3.docx","4.docx","5.docx"]
    process_documents(dir)

#инициализационный скрипт
if __name__ == "__main__" :
    main()
