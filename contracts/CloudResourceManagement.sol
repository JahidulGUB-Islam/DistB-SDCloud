// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CloudResourceManagement {
    enum Permission { None, SysAdmin }

    address public owner;

    mapping(address => Permission) public permissions;
    mapping(address => bool) public authorizedUsers;

    event PermissionUpdate(address indexed user, Permission permission);
    event FlowRuleSet(string srcIp, string dstIp, string action);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    modifier onlyAuthorized() {
        require(authorizedUsers[msg.sender], "Unauthorized user.");
        _;
    }

    function updatePermission(address user, Permission permission) public onlyOwner {
        permissions[user] = permission;
        emit PermissionUpdate(user, permission);
    }


    function addAuthorizedUser(address userAddress) external onlyOwner {
        authorizedUsers[userAddress] = true;
    }

    function removeAuthorizedUser(address userAddress) external onlyOwner {
        authorizedUsers[userAddress] = false;
    }

    function isAuthorized(address userAddress) external view returns (bool) {
        return authorizedUsers[userAddress];
    }

    function setFlowRule(string memory srcIp, string memory dstIp, string memory action) external onlyAuthorized {
        emit FlowRuleSet(srcIp, dstIp, action);
    }
}
