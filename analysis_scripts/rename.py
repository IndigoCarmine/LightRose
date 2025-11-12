import pandas as pd
import os
import shutil


def main():
    df = pd.read_excel("renaming_info.xlsx")
    for h, row in df.iterrows():
        old = row["AFM File Names"]
        molname = row["Molecule Name"]
        conc = row["Concentration"]
        solvent = row["Solvent"]
        condition = row["Condition"]

        new = f"{molname}_{conc}_{solvent}_{condition}_0.spm"
        if "nan" in new:
            continue

        # copy
        print(f'Renaming "{old}" to "{new}"')
        old_path = os.path.join(r"D:\Dropbox\測定データ\AFM", old)
        new_path = os.path.join(r"renamed_data", new)
        for i in range(1, 100):
            if os.path.exists(new_path):
                new_path = os.path.join(
                    r"renamed_data", f"{molname}_{conc}_{solvent}_{condition}_{i}.spm"
                )
            else:
                break
        shutil.copy2(old_path, new_path)


if __name__ == "__main__":
    main()
