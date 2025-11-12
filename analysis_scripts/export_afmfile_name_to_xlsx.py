import os


def main():
    afm_directory = "\\\\YagaiG-NAS1\\AFM"
    output_excel_file = "export.xlsx"

    afm_file_names = []
    for root, _, files in os.walk(afm_directory):
        for file_name in files:
            if not file_name.endswith("bin") or not file_name.startswith("@"):
                rel_path = os.path.relpath(os.path.join(root, file_name), afm_directory)
                if os.path.isfile(rel_path):
                    afm_file_names.append(rel_path)

    import pandas as pd

    df = pd.DataFrame(afm_file_names, columns=["AFM File Names"])
    df.to_excel(output_excel_file, index=False)


if __name__ == "__main__":
    main()
