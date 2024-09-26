import pymssql as ms, pandas as pd, json
from datetime import datetime
from svcEngine.utils.logger import service_logger as sl, transaction_logger as tl

class DB:
    def __init__(self):
        self.conn = None  # initialize connection attribute
    def connect_db(self, server_ip, database_server, username_acc, password_acc): # function db connect
        try:
            self.conn = ms.connect(
                server=server_ip,
                database=database_server,
                user=username_acc,
                password=password_acc,
                as_dict=True
            )
            sl.info(f"Connecting to MS SQL Server database with IP:{server_ip}, Database name:{database_server}, UName:{username_acc}, DB Dict:True")
        except Exception as e:
            sl.error(f"Error occured in DB Connection: {e}")
            print(f"Error occurred in DB Connection: {e}")
    def disconnect_db(self): # function db disconnect
        if self.conn:
            self.conn.close() # closing connection
            sl.info("Disconnecting from MS SQL Server database")
    def update_value(self, database, table, excel_file, json_file, json_value, *args): # function for updating value on table database
        try:
            if not self.conn:
                sl.warning("Cannot update to database table because no connection established.")
                raise Exception("No database connection established.")
            get_time = datetime.now() # getting current timestamp for timestamp column in db table
            timestamp = get_time.strftime("%Y-%m-%d %H:%M:%S")
            # block code to read excel file
            try:
                sl.info(f"Opening excel file in {excel_file}")
                df = pd.read_excel(excel_file, dtype=str) # reading excel file 
                _dict = df.to_dict(orient='records')
                for data in _dict:
                    ''
            except Exception as e:
                sl.error(f"Error occured when opening file excel: {e}")
                print(f"Error occured when opening file excel: {e}")
            # function get json list for indexing tagcode
            # def get_json_list(filename, key): # funtion for opening json file and return data using node id for the key
            #     try:
            #         with open(filename, 'r') as file:
            #             data = json.load(file) # load json
            #             if key in data: # confirmation each key in json file
            #                 return data[key] # return value from the key
            #     except Exception as e:
            #         print(f"Error occured when opening json file: {e}")
            # get value and node id from data change in opc ua
            json_val = json.loads(json_value)
            node_id = list(json_val.keys())[0]
            value_node = json_val[node_id]
            # main program for splitting method, value, uns, node id
            for arg in args:
                if arg == "opcuanx":
                    sl.info("Using OPC UA Client method to connect NX PLCs")
                    # for data in _dict:
                    #     print(data['NODE_ID'])
                    #     print(node_id)
                    #     if data['NODE_ID'] == node_id:
                    #         part_cd = data['PART_CD']
                    #         ce_cd = data['CE_CD']
                    #         asset_id = data['ASSET_ID']
                    #         tag = data['TAG_CD']
                    #         if type(value_node) == list:
                    #             json_list = get_json_list(json_file, node_id)
                    #             for i, (tag_cd, val) in enumerate(zip(json_list, value_node)):
                    #                 buffer_update = {
                    #                     "asset": asset_id,
                    #                     "ce": ce_cd,
                    #                     "device": part_cd,
                    #                     "tag": tag_cd,
                    #                     "value": val,
                    #                     "ts": timestamp
                    #                 }
                    #                 # execute update query
                    #                 cursor = self.conn.cursor()
                    #                 query = f"UPDATE [{database}].[dbo].[{table}] SET VAL = '{buffer_update['value']}', TS = '{buffer_update['ts']}' WHERE ASSET_ID = '{buffer_update['asset']}' AND CE_CD = '{buffer_update['ce']}' AND PART_CD = '{buffer_update['device']}' AND TAG_CD = '{buffer_update['tag']}'"
                    #                 cursor.execute(query)
                    #                 self.conn.commit()
                    #         else:
                    #             buffer_update = {
                    #                 "asset": asset_id,
                    #                 "ce": ce_cd,
                    #                 "device": part_cd,
                    #                 "tag": tag,
                    #                 "value": value_node,
                    #                 "ts": timestamp
                    #                 }
                    #             # execute update query
                    #             cursor = self.conn.cursor()
                    #             query = f"UPDATE [{database}].[dbo].[{table}] SET VAL = '{buffer_update['value']}', TS = '{buffer_update['ts']}' WHERE ASSET_ID = '{buffer_update['asset']}' AND CE_CD = '{buffer_update['ce']}' AND PART_CD = '{buffer_update['device']}' AND TAG_CD = '{buffer_update['tag']}'"
                    #             cursor.execute(query)
                    #             self.conn.commit()
                    #         break
                    #     else:
                    #         raise ValueError("Kode node tidak ditemukan.")
                elif arg == "opcuadxpserver":
                    sl.info("Using OPC UA Client method to connect DXP Server")
                    # for data in _dict:
                    #     print(data['NODE_ID'])
                    #     print(node_id)
                    # if data['NODE_ID'] == node_id:
                    #     part_cd = data['PART_CD']
                    #     ce_cd = data['CE_CD']
                    #     asset_id = data['ASSET_ID']
                    #     tag = data['TAG_CD']
                    #     if type(value_node) == list:
                    #         json_list = get_json_list(json_file, node_id)
                    #         for i, (tag_cd, val) in enumerate(zip(json_list, value_node)):
                    #             buffer_update = {
                    #                 "asset": asset_id,
                    #                 "ce": ce_cd,
                    #                 "device": part_cd,
                    #                 "tag": tag_cd,
                    #                 "value": val,
                    #                 "ts": timestamp
                    #             }
                    #             # execute update query
                    #             cursor = self.conn.cursor()
                    #             query = f"UPDATE [{database}].[dbo].[{table}] SET VAL = '{buffer_update['value']}', TS = '{buffer_update['ts']}' WHERE ASSET_ID = '{buffer_update['asset']}' AND CE_CD = '{buffer_update['ce']}' AND PART_CD = '{buffer_update['device']}' AND TAG_CD = '{buffer_update['tag']}'"
                    #             cursor.execute(query)
                    #             self.conn.commit()
                    #     else:
                    #         buffer_update = {
                    #             "asset": asset_id,
                    #             "ce": ce_cd,
                    #             "device": part_cd,
                    #             "tag": tag,
                    #             "value": value_node,
                    #             "ts": timestamp
                    #             }
                    #         # execute update query
                    #         cursor = self.conn.cursor()
                    #         query = f"UPDATE [{database}].[dbo].[{table}] SET VAL = '{buffer_update['value']}', TS = '{buffer_update['ts']}' WHERE ASSET_ID = '{buffer_update['asset']}' AND CE_CD = '{buffer_update['ce']}' AND PART_CD = '{buffer_update['device']}' AND TAG_CD = '{buffer_update['tag']}'"
                    #         cursor.execute(query)
                    #         self.conn.commit()
                    #     break
                    # else:
                    #     raise ValueError("Kode node tidak ditemukan.")
        except Exception as e:
            print(f"Error occurred during update: {e}")
