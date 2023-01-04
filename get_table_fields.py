from commonly_used_files import get_po
import dbf

time_for_production = True
file_to_use = get_po(time_for_production)


def get_table_file():
    return_table = dbf.Table(file_to_use, ignore_memos=True).open(mode=dbf.READ_ONLY)
    return return_table


def get_table_constraints(table):
    structure = table.structure()
    with open(r"C:\Users\User\Desktop\holder.txt", 'w') as f:
        for line in structure:
            f.write(f"{line}\n")

    table.close()


def main():
    table = get_table_file()
    get_table_constraints(table)


if __name__ == "__main__":
    main()
