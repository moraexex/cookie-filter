import tkinter as tk
from tkinter import filedialog, messagebox
import os

def filter_cookies():
    cookies_path = cookies_entry.get()
    blocked_path = blocked_entry.get()

    if not os.path.isfile(cookies_path) or not os.path.isfile(blocked_path):
        messagebox.showerror("خطأ", "يرجى اختيار الملفات بشكل صحيح.")
        return

    # تحميل الحسابات المحظورة
    with open(blocked_path, "r", encoding="utf-8") as f:
        blocked_ids = set(line.strip() for line in f)

    # تحميل الكوكيز
    with open(cookies_path, "r", encoding="utf-8") as f:
        cookies_lines = f.readlines()

    # تصفية الكوكيز
    filtered_lines = []
    for line in cookies_lines:
        if "c_user=" in line:
            try:
                user_id = line.split("c_user=")[1].split(";")[0].strip()
                if user_id in blocked_ids:
                    continue
            except IndexError:
                pass
        filtered_lines.append(line)

    # حفظ الناتج
    output_path = "filtered_cookies.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(filtered_lines)

    messagebox.showinfo("تمت التصفية", f"✅ تم حفظ الكوكيز السليمة في:\\n{output_path}")

# واجهة المستخدم
root = tk.Tk()
root.title("أداة تصفية الكوكيز")

tk.Label(root, text="ملف الكوكيز:").pack()
cookies_entry = tk.Entry(root, width=50)
cookies_entry.pack()
tk.Button(root, text="اختر ملف الكوكيز", command=lambda: cookies_entry.insert(0, filedialog.askopenfilename())).pack()

tk.Label(root, text="ملف الحسابات المقفولة:").pack()
blocked_entry = tk.Entry(root, width=50)
blocked_entry.pack()
tk.Button(root, text="اختر ملف الحسابات", command=lambda: blocked_entry.insert(0, filedialog.askopenfilename())).pack()

tk.Button(root, text="🔍 تصفية الكوكيز", command=filter_cookies, bg="green", fg="white").pack(pady=10)

root.mainloop()
