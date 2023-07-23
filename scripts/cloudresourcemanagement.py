from web3 import Web3
import requests

ETHEREUM_BLOCKCHAIN_URL = "http://localhost:7545"
smart_contract_address = "0x7A053ff5F57Ddd601e63c5363eDdCD11695AA971"
smart_contract_abi = [
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": false,
                "internalType": "string",
                "name": "srcIp",
                "type": "string",
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "dstIp",
                "type": "string",
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "action",
                "type": "string",
            },
        ],
        "name": "FlowRuleSet",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "enum CloudResourceManagement.Permission",
                "name": "permission",
                "type": "uint8",
            },
        ],
        "name": "PermissionUpdate",
        "type": "event",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "authorizedUsers",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "permissions",
        "outputs": [
            {
                "internalType": "enum CloudResourceManagement.Permission",
                "name": "",
                "type": "uint8",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "user", "type": "address"},
            {
                "internalType": "enum CloudResourceManagement.Permission",
                "name": "permission",
                "type": "uint8",
            },
        ],
        "name": "updatePermission",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "userAddress", "type": "address"}
        ],
        "name": "addAuthorizedUser",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "userAddress", "type": "address"}
        ],
        "name": "removeAuthorizedUser",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "userAddress", "type": "address"}
        ],
        "name": "isAuthorized",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "string", "name": "srcIp", "type": "string"},
            {"internalType": "string", "name": "dstIp", "type": "string"},
            {"internalType": "string", "name": "action", "type": "string"},
        ],
        "name": "setFlowRule",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

# Connect to the Ethereum node
web3 = Web3(Web3.HTTPProvider(ETHEREUM_BLOCKCHAIN_URL))

smart_contract = web3.eth.contract(
    address=smart_contract_address, abi=smart_contract_abi
)

OPENFLOW_SDN_CONTROLLER_URL = "http://localhost:8181"


def set_flow_rule(src_ip, dst_ip, action):
    flow_rule = {"priority": 100, "ip-src": src_ip, "ip-dst": dst_ip, "action": action}
    requests.post(
        f"{OPENFLOW_SDN_CONTROLLER_URL}/restconf/config/openFlow-inventory:nodes/node/openflow:1/table/0/flow",
        json=flow_rule,
    )


# Event listener callback function
def flow_rule_set_handler(event):
    print("FlowRuleSet event received:")
    print("Source IP:", event["args"]["srcIp"])
    print("Destination IP:", event["args"]["dstIp"])
    print("Action:", event["args"]["action"])


def allocate_cloud_resource(user_address):
    if smart_contract.functions.isAuthorized(user_address).call():
        set_flow_rule(user_address, "cloud_server_ip", "allow")

        smart_contract.functions.setFlowRule(
            user_address, "cloud_server_ip", "allow"
        ).transact()


flow_rule_event_filter = smart_contract.events.FlowRuleSet.createFilter(
    fromBlock="latest"
)

user_address = "0x1E212e3326bfAA988c2717AF7b1c3CF0FE555c29"

allocate_cloud_resource(user_address)

for event in flow_rule_event_filter.get_all_entries():
    flow_rule_set_handler(event)
