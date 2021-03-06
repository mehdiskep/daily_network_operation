from getpass import getpass
from pprint import pprint


def nornir_set_creds(brg, username, password):
    """Handler so credentials don't need stored in clear in inventory."""

    for host_obj in brg.inventory.hosts.values():
        # host_obj.username = username
        # host_obj.password = password
        host_obj.data["username"] = username
        host_obj.data["password"] = password


def std_print(agg_result):
    print()
    for k, multi_result in agg_result.items():
        print('-' * 50)
        print(k)
        for result_obj in multi_result:
            if isinstance(result_obj.result, str):
                print(result_obj.result)
            else:
                pprint(result_obj.result)
        print('-' * 50)
        print()
    print()