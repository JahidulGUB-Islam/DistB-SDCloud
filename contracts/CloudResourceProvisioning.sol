// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CloudResourceProvisioning {
    enum Permission { None, SysAdmin }

    address public owner;

    mapping(address => Permission) public permissions;
    mapping(address => bool) public authorizedUsers;

    struct CloudResource {
        address requester;
        string resourceType;
        uint256 quantity;
        bool isApproved;
    }

    mapping(uint256 => CloudResource) public resources;

    uint256 private resourceIdCounter;

    event PermissionUpdate(address indexed user, Permission permission);
    event ResourceRequested(uint256 resourceId, address requester, string resourceType, uint256 quantity);
    event ResourceRequestedApproved(uint256 resourceId);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this operation");
        _;
    }

    function requestResource(string memory _resourceType, uint256 _quantity) external {
        resourceIdCounter++;

        resources[resourceIdCounter] = CloudResource(msg.sender, _resourceType, _quantity, false);

        emit ResourceRequested(resourceIdCounter, msg.sender, _resourceType, _quantity);
    }

    function approveResourceRequest(uint256 _resourceId) public onlyOwner {
        require(_resourceId <= resourceIdCounter, "Invalid resource ID");

        CloudResource storage resource = resources[_resourceId];
        require(!resource.isApproved, "Resource request already approved");

        resource.isApproved = true;

        emit ResourceRequestedApproved(_resourceId);
    }
}
