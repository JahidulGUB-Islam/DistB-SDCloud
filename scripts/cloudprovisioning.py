from web3 import Web3

contract_address = "0x4B352kw5F57Ddd601e63c5363eDdCD11634II352"
contract_abi = [
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
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
                "internalType": "enum CloudResourceProvisioning.Permission",
                "name": "permission",
                "type": "uint8",
            },
        ],
        "name": "PermissionUpdate",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "resourceId",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "requester",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "resourceType",
                "type": "string",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256",
            },
        ],
        "name": "ResourceRequested",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "resourceId",
                "type": "uint256",
            }
        ],
        "name": "ResourceRequestedApproved",
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
                "internalType": "enum CloudResourceProvisioning.Permission",
                "name": "",
                "type": "uint8",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "name": "resources",
        "outputs": [
            {"internalType": "address", "name": "requester", "type": "address"},
            {"internalType": "string", "name": "resourceType", "type": "string"},
            {"internalType": "uint256", "name": "quantity", "type": "uint256"},
            {"internalType": "bool", "name": "isApproved", "type": "bool"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "string", "name": "_resourceType", "type": "string"},
            {"internalType": "uint256", "name": "_quantity", "type": "uint256"},
        ],
        "name": "requestResource",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_resourceId", "type": "uint256"}
        ],
        "name": "approveResourceRequest",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
web3 = Web3(Web3.HTTPProvider("http://localhost:7545"))

private_key = (
    "wolf popular cram close enhance vessel post palace wreck embrace key come"
)

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

account_address = "YOUR_ACCOUNT_ADDRESS"


def request_resource(resource_type, quantity):
    transaction = contract.functions.requestResource(
        resource_type, quantity
    ).buildTransaction(
        {
            "chainId": 1,
            "gas": 2000000,
            "gasPrice": web3.toWei("40", "gwei"),
            "nonce": web3.eth.getTransactionCount(account_address),
        }
    )

    signed_transaction = web3.eth.account.signTransaction(transaction, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    return tx_receipt


def approve_resource_request(resource_id):
    transaction = contract.functions.approveResourceRequest(
        resource_id
    ).buildTransaction(
        {
            "chainId": 1,
            "gas": 2000000,
            "gasPrice": web3.toWei("40", "gwei"),
            "nonce": web3.eth.getTransactionCount(account_address),
        }
    )

    signed_transaction = web3.eth.account.signTransaction(transaction, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    return tx_receipt


if __name__ == "__main__":
    tx_receipt = request_resource("VM", 5)
    print("Resource requested. Transaction receipt:", tx_receipt)

    tx_receipt = approve_resource_request(1)
    print("Resource request approved. Transaction receipt:", tx_receipt)
