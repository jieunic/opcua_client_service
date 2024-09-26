"""
Developed by brownfield DX team
jieunic
v2.2.4

All syntax having sl or tl that means this for logging data

Setup must be prepared in setup.env file
"""

import os
import json
import asyncio
from asyncua import Client, ua
from svcEngine.utils import file_execution as exec
from svcEngine.utils.timer import LoggingTime
from svcEngine.utils.logger import service_logger as sl, transaction_logger as tl
from svcEngine.utils.database import DB

env             = "svcEngine/setup.env"  # object for env file path
t               = LoggingTime  # object for class in timer module
db              = DB()  # object for module database
opc_server_url  = exec.Env.get(env, "OPCUA_SERVER")
dataset_path    = exec.Env.get(env, "DATASET")
exec_time       = exec.Env.get(env, "TIME_EXEC")
excel_file      = exec.Env.get(env, "EXCEL")
tag_code_file   = exec.Env.get(env, "TAG_CODE")
db_user         = exec.Env.get(env, "DB_USER")
db_pass         = exec.Env.get(env, "DB_PASSWORD")
db_name         = exec.Env.get(env, "DB_NAME")
db_table        = exec.Env.get(env, "DB_TABLE")
db_server       = exec.Env.get(env, "DB_SERVER")
db_use          = exec.Env.get(env, "DB_USE")
trial_node      = exec.Env.get(env, "NODE_ID_DEBUG")
main_service    = exec.Env.get(env, "CLIENT_SERVICE")
client          = Client(url=opc_server_url)
nodes           = []  # object for list temporary placement for node id used for subscribing to server

class SubscribeHandler:
    def __init__(self):
        pass

    async def datachange_notification(self, node, val, data):
        dummy = {str(node): val}  # convert to json value and node id
        dummy_json = json.dumps(dummy)
        if db_use == "True":
            db.update_value(db_name, db_table, excel_file, tag_code_file, dummy_json, main_service)  # run function update value
        else:
            nest = "hell"
        tl.info(f"Datachange acquired before updated into database! |{opc_server_url}|nodeid {node}|value {val}|")

async def main():
    try:
        sub = True  # object for run looping service
        print("Connecting to Server. . .")
        sl.info(f"Connecting to OPC UA Server with url {opc_server_url}")
        st = t.start()  # start logging timer
        await client.connect()  # connect to opc ua server
        print("Connection successfully!")
        sl.info(f"Connection successfully to OPC UA Server with url {opc_server_url}")

        if db_use == "True":
            db.connect_db(db_server, db_name, db_user, db_pass)
        else:
            print("Database not used")

        et = t.end()  # end logging timer
        print(f"Total execution time connection {t.total(st, et)}")
        sl.info(f"Total execution time connection {t.total(st, et)}")
        exec.Excel.import_node_id(excel_file, nodes)  # function for import node id from handling module
        
        if nodes:
            st = t.start()
            sl.info(f"Import node id from excel file successfully, dir {excel_file}, total node id {len(nodes)}")
            print("Create subscription")
            sl.info("Creating subscription for datachange")
            print("Node ID count:", len(nodes))
            handler = SubscribeHandler()  # create object for SubscribeHandler()
            sl.info(f"Create subscription with execution time {exec_time}")
            subscription = await client.create_subscription(float(exec_time), handler)  # create subscription with handler and execution time (time must be float formatted)
            et = t.end()
            sl.info(f"Total time for create subscribe {t.total(st, et)}")
            try:
                sl.info("Getting node information from server")
                node_objs = [client.get_node(node_id) for node_id in nodes]  # iteration and get_node to all node from node list
                await subscription.subscribe_data_change(node_objs)  # subscribing for data change to each node id
                sl.info("Starting subscribing each node to server!")
                print("Success")
                
                while sub:  # Keep the program running to handle data change events
                    await asyncio.sleep(1)  # looping process
            except Exception as e:
                sub = False  # stop intiialize to get in loop process
                sl.error(f"Exception Error occured at subscribing: {e}")
                print(f"Error occured: {e}")
            except KeyboardInterrupt:
                await subscription.delete()  # deleting session and node id subscription to opc server
                sl.warning(f"Closing service and deleting subscription to OPC UA Server {opc_server_url}")
                print("Closing service. . .")
                if db_use == "True":
                    await db.disconnect_db()
                sub = False  # stop intiialize to get in loop process
        else:
            sl.warning(f"Node ID aren't in folder, check your setup.env file. Current directory {excel_file}")
            print("Node id not ready! Confirm in the setup.env file!")
            sl.info("Exiting services.")
            print("Exiting...")
            raise SystemExit  # exit from service safely
    except KeyboardInterrupt:
        sl.warning("Service interrupted!")
        print("Subscription canceled!")
    except Exception as e:
        sl.error(f"Exception Error occured at connecting to OPC UA Server {opc_server_url}: {e}")
        print(f"Error while connecting: {e}")
    finally:
        try:
            sl.info(f"Disconnect OPC UA Server {opc_server_url}")
            await client.disconnect()  # disconnecting from opc ua server
        except Exception as e:
            sl.error(f"Error while disconnecting: {e}")
            print(f"Error while disconnecting: {e}")

asyncio.run(main())