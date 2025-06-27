import os
import subprocess
from tkinter import filedialog, Tk, messagebox

def convert_heic_to_jpg_with_ffmpeg():
    root = Tk()
    root.withdraw()

    folder = filedialog.askdirectory(title="Choisissez un dossier contenant des fichiers .heic")
    if not folder:
        return

    converted = 0
    failed = 0

    for filename in os.listdir(folder):
        print(f"Fichier trouvé : {filename}") 
        if filename.lower().endswith(".heic"):
            input_path = os.path.join(folder, filename)
            output_path = os.path.splitext(input_path)[0] + ".jpg"
            try:
                result = subprocess.run(
                    ["ffmpeg", "-y", "-i", input_path, output_path],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                if result.returncode == 0:
                    converted += 1
                else:
                    failed += 1
            except Exception as e:
                print(f"Erreur sur {filename}: {e}")
                failed += 1

    if converted > 0:
        messagebox.showinfo("Conversion terminée", f"{converted} image(s) convertie(s).\n{failed} erreur(s).")
    else:
        messagebox.showwarning("Conversion échouée", "Aucun fichier HEIC converti.")

if __name__ == "__main__":
    convert_heic_to_jpg_with_ffmpeg()
