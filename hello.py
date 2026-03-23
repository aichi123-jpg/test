import tkinter as tk
from tkinter import scrolledtext


def build_output() -> str:
    lines = ["Hallo Welt!", "", "Kleines Einmaleins (1 bis 10):"]
    for i in range(1, 11):
        row = "".join(f"{i * j:>4}" for j in range(1, 11))
        lines.append(row)
    return "\n".join(lines)


def main() -> None:
    root = tk.Tk()
    root.title("Hallo Welt - Einmaleins")
    root.geometry("520x320")

    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=(10, 0))

    text_area = scrolledtext.ScrolledText(root, wrap=tk.NONE, font=("Courier", 11))
    text_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

    ok_button = tk.Button(button_frame, text="OK", state=tk.DISABLED, width=12, command=root.destroy)
    ok_button.pack(side=tk.LEFT)

    output = build_output()
    text_area.insert(tk.END, output)
    text_area.configure(state=tk.DISABLED)

    ok_button.configure(state=tk.NORMAL)

    root.mainloop()


if __name__ == "__main__":
    main()
