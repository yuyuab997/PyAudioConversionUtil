import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES
from audio_conversion.AudioConverter import ac_mp4_to_mp3
from tkinter.messagebox import showinfo


class DragDropApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.title("mp4 --> mp3")
        self.geometry("600x400")
        self.configure(bg='#2E2E2E')  # 背景颜色

        # 文件路径初始化为空
        self.file_path = None

        # 设置主标签
        self.label = tk.Label(self, text="Drag and drop a file here",
                              bg='#2E2E2E', fg='#FFFFFF',
                              font=('Helvetica', 16, 'bold'))
        self.label.pack(pady=50)

        # 设置文件路径标签
        self.file_path_label = tk.Label(self, text="",
                                        bg='#2E2E2E', fg='#FFFFFF',
                                        font=('Helvetica', 12))
        self.file_path_label.pack(pady=5)

        # 添加文件选择按钮
        self.select_file_button = tk.Button(self, text="选择文件",
                                            bg='#007BFF', fg='#FFFFFF',
                                            font=('Helvetica', 12, 'bold'),
                                            command=self.select_file)
        self.select_file_button.pack(pady=5)

        # 添加处理文件的按钮
        self.process_button = tk.Button(self, text="开始转换",
                                        bg='#4CAF50', fg='#FFFFFF',
                                        font=('Helvetica', 12, 'bold'),
                                        state=tk.DISABLED,
                                        command=self.process_file)
        self.process_button.pack(side=tk.BOTTOM, pady=20)

        # 配置文件拖拽功能
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.drop)

    def drop(self, event):
        # 获取拖拽文件的路径
        self.file_path = event.data.replace('{', '').replace('}', '')

        # 更新文件路径标签
        self.file_path_label.config(text=self.file_path)

        # 激活按钮
        self.process_button.config(state=tk.NORMAL)

    def select_file(self):
        # 打开文件选择对话框
        self.file_path = filedialog.askopenfilename(title="选择mp4文件")
        if self.file_path:
            self.file_path_label.config(text=self.file_path)
            self.process_button.config(state=tk.NORMAL)

    def process_file(self):
        # 处理文件的逻辑
        if self.file_path:
            ac_mp4_to_mp3(self.file_path, self.file_path)
            showinfo('提示:', '转换后的文件已保存到相同路径下')
            self.label.config(text="")
            self.file_path_label.config(text="")
            self.process_button.config(state=tk.DISABLED)
            self.file_path = None


if __name__ == "__main__":
    # 初始化并运行应用程序
    app = DragDropApp()
    app.mainloop()
