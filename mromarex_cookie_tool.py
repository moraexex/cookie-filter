
import tkinter as tk
from tkinter import filedialog, messagebox
import re

def filter_cookies():
    file_path = filedialog.askopenfilename(title="اختر ملف الكوكيز", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            cookies = file.readlines()

        valid_cookies = [cookie.strip() for cookie in cookies if 'c_user=' in cookie and 'xs=' in cookie]

        with open('filtered_cookies.txt', 'w', encoding='utf-8') as file:
            for cookie in valid_cookies:
                file.write(cookie + '\n')

        messagebox.showinfo("تمت التصفية", "✅ تم حفظ الكوكيز السليمة في:\nfiltered_cookies.txt")
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ أثناء التصفية:\n{str(e)}")

def extract_ids():
    file_path = filedialog.askopenfilename(title="اختر ملف الكوكيز", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        ids = re.findall(r'c_user=(\d+)', content)
        ids = list(set(ids))  # إزالة التكرار

        if ids:
            with open('extracted_ids.txt', 'w', encoding='utf-8') as f:
                for user_id in sorted(ids):
                    f.write(user_id + '\n')
            messagebox.showinfo("تم استخراج الـ IDs", "✅ تم حفظ الـ IDs في:\nextracted_ids.txt")
        else:
            messagebox.showinfo("لم يتم العثور على IDs", "⚠️ لم يتم العثور على أي c_user في الملف.")
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ أثناء استخراج الـ IDs:\n{str(e)}")

# تصميم الواجهة
root = tk.Tk()
root.title("Mromarex - Cookie Tool")
root.geometry("450x250")
root.configure(bg="#1e1e2e")
root.resizable(False, False)

title_label = tk.Label(root, text="🧰 Mromarex - Cookie Filter Tool", bg="#1e1e2e", fg="#f5f5f5", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

btn_filter = tk.Button(root, text="🧹 تصفية الكوكيز", font=("Arial", 12), bg="#3b82f6", fg="white", width=30, command=filter_cookies)
btn_filter.pack(pady=10)

btn_extract = tk.Button(root, text="🆔 استخراج الـ IDs من الكوكيز", font=("Arial", 12), bg="#10b981", fg="white", width=30, command=extract_ids)
btn_extract.pack(pady=10)

root.mainloop()
