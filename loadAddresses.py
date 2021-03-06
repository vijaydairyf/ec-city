import logging

import ec_addresses
import ec_psql_util
from nosql import mongo_setup

__author__ = 'spowell'

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s",
                    filename="load_addresses.log",
                    filemode="w",
                    level=logging.ERROR,
                    datefmt="%m/%d/%Y %I:%M:%S %p")

hgac_gdb = "data/HGAC/oct1_2018/WhartonCo_Streets_Addresses_Oct1_2018/Wharton_HGAC_streets_addresses_Oct2018.gdb"
cad_shp = "data/WhartonCAD/Ownership.shp"
incode_file_path = "data/incode/TMP_PC2HOST.TMP"
mongo_setup.global_init()

psql_connection = ec_psql_util.psql_connection()
# con = ec_sql_server_util.connect(driver=r"{SQL Server Native Client 11.0};",
#                                  server="HOME-GIS\SQLEXPRESS;",
#                                  database="ec;",
#                                  trusted_connection="yes;",
#                                  uid="HOME-GIS\\sde;pwd=sde;")


# ec_addresses.setup_not_found_address_table(psql_connection)

# con = ec_sql_server_util.connect(driver=r"{SQL Server Native Client 11.0};",
#                                  server="HOME-GIS\SQLEXPRESS;",
#                                  database="ec;",
#                                  trusted_connection="yes;",
#                                  uid="HOME-GIS\\sde;pwd=sde;")

# HGAC Data Load
# ec_addresses.load_starmap_streets(hgac_gdb)
# con = ec_sql_server_util.connect(driver=r"{SQL Server Native Client 11.0};",
#                                  server="HOME-GIS\SQLEXPRESS;",
#                                  database="ec;",
#                                  trusted_connection="yes;",
#                                  uid="HOME-GIS\\sde;pwd=sde;")


con = ec_psql_util.psql_connection()
ec_addresses.load_e911_addresses(con, hgac_gdb, True)
# con = ec_sql_server_util.connect(driver=r"{SQL Server Native Client 11.0};",
#                                  server="HOME-GIS\SQLEXPRESS;",
#                                  database="ec;",
#                                  trusted_connection="yes;",
#                                  uid="HOME-GIS\\sde;pwd=sde;")
# ec_addresses.load_incode_addresses(con, incode_file_path, True)
# con = ec_sql_server_util.connect(driver=r"{SQL Server Native Client 11.0};",
#                                  server="HOME-GIS\SQLEXPRESS;",
#                                  database="ec;",
#                                  trusted_connection="yes;",
#                                  uid="HOME-GIS\\sde;pwd=sde;")
psql_connection = ec_psql_util.psql_connection()
ec_addresses.load_parcel_addresses(psql_connection, cad_shp, True)
# ec_addresses.create_unique_tables()


