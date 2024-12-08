#Функция для изменения параметров текста в документе 
def modify_docx(file_path):
     try :
        #Окрываем .docx файл
        doc=Document(file_path) # type: ignore
        # Проходим по каждому абзацу документа
        for paragraph in doc.paragraphs:
            # Настраиваем текст внутри абзаца
            for run in paragraph.runs:
                run.font.name = 'Times New Roman'  # Устанавливаем шрифт
                run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman') # type: ignore
                # Сохраняем изменения в новый файл
        output_path = f"modified_{os.path.basename(file_path)}" # type: ignore
        doc.save(output_path)
        print(f"Документ сохранён: {output_path}")

     except Exception as e:
        # Если возникает ошибка, выводим сообщение
        print(f"Ошибка при обработке файла {file_path}: {e}") # type: ignore
        # Ищем все файлы .docx в папке
        docx_files = [f for f in os.listdir(folder_path) if f.endswith('.docx')] # type: ignore

    # Если файлы .docx не найдены, выводим сообщение
        if not docx_files:
         print("В указанной папке нет файлов .docx.")
        return
     # Обрабатываем каждый файл
     for file_name in docx_files:
        file_path = os.path.join(folder_path, file_name)  # type: ignore # Получаем полный путь к файлу
        print(f"Обрабатывается файл: {file_name}")
        modify_docx(file_path)  # Вызываем функцию для обработки файла



