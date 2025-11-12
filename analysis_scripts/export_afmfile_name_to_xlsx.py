import os


def is_afm_file(file_path: str) -> bool:
    if file_path.endswith("spm"):
        return True
    ext = file_path.split(".")[-1]
    if len(ext) == 3 and ext.isdigit():
        return True
    return False


def main():
    afm_directory = r"D:\Dropbox\測定データ\AFM"
    output_excel_file = "export.xlsx"

    afm_file_names = []
    for root, _, files in os.walk(afm_directory):
        for file_name in files:
            if file_name.startswith("@"):
                # Skip temporary or hidden files
                continue
            if is_afm_file(file_name):
                rel_path = os.path.relpath(os.path.join(root, file_name), afm_directory)
                full_path = os.path.join(afm_directory, rel_path)
                if os.path.isfile(full_path):
                    afm_file_names.append(rel_path)

    print("Total AFM files found:", len(afm_file_names))
    import pandas as pd

    df = pd.DataFrame(afm_file_names, columns=["AFM File Names"])
    df.to_excel(output_excel_file)


if __name__ == "__main__":
    main()
