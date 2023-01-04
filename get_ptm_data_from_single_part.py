from dbf_tools import retrieve_part_data
from commonly_used_files import get_inventory
import dbf

time_for_production = True

inventory_file = get_inventory(time_for_production)
inventory_table = dbf.Table(inventory_file, ignore_memos=True).open(mode=dbf.READ_ONLY)

part_data = retrieve_part_data("AND", "TPARTTEST", inventory_table)

print(part_data)

