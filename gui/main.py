import tkinter as tk
from tkinter import filedialog
import os


class EEGAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Нейроклассификатор ЭЭГ")

        self.model_files = ["model1.pkl", "model2.pkl", "model3.pkl"]  # Предварительно загруженные модели
        self.model_names = ["СДВГ", "Аутизм", "Эпилепсия"]
        self.selected_model_index = tk.IntVar(value=-1)

        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            label = tk.Label(self.root, text=self.model_names[i])
            label.grid(row=i, column=0, padx=10, pady=10)

            radio_button = tk.Radiobutton(self.root, text=self.model_names[i], variable=self.selected_model_index,
                                          value=i)
            radio_button.grid(row=i, column=1, padx=10, pady=10)

        self.eeg_file = ""
        self.eeg_label = tk.Label(self.root, text="Файл EEG:")
        self.eeg_label.grid(row=3, column=0, padx=10, pady=10)

        self.eeg_load_button = tk.Button(self.root, text="Загрузить файл EEG", command=self.load_eeg_file)
        self.eeg_load_button.grid(row=3, column=1, padx=10, pady=10)

        self.eeg_file_label = tk.Label(self.root, text="")
        self.eeg_file_label.grid(row=3, column=2, padx=10, pady=10)

        self.predict_button = tk.Button(self.root, text="Выполнить предсказание", command=self.predict)
        self.predict_button.grid(row=4, column=0, columnspan=2, pady=20)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=5, column=0, columnspan=3, pady=10)

    def load_eeg_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("EEG Files", "*.txt *.csv")])
        if file_path:
            self.eeg_file = file_path
            self.eeg_file_label.config(text=os.path.basename(file_path))

    def predict(self):
        selected_model_index = self.selected_model_index.get()

        if selected_model_index == -1:
            self.result_label.config(text="Пожалуйста, выберите модель.")
            return

        if not self.eeg_file:
            self.result_label.config(text="Пожалуйста, загрузите файл EEG.")
            return

        # Здесь будет ваш код для выполнения предсказания с использованием выбранной модели и загруженного файла EEG
        result_text = f"Предсказание выполнено с моделью {self.model_names[selected_model_index]}:\n"
        result_text += f"Модель: {os.path.basename(self.model_files[selected_model_index])}\n"
        result_text += f"Файл EEG: {os.path.basename(self.eeg_file)}"
        self.result_label.config(text=result_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = EEGAnalyzerApp(root)
    root.mainloop()
