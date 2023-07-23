// SPDX-License-Identifier: MIT
const CloudResourceProvisioning = artifacts.require('CloudResourceProvisioning')

contract('CloudResourceProvisioning', (accounts) => {
  let cloudResourceProvisioning

  before(async () => {
    cloudResourceProvisioning = await CloudResourceProvisioning.deployed()
  })

  it('should request cloud resources', async () => {
    const resourceType = 'VM'
    const quantity = 5
    const requester = accounts[1]

    const tx = await cloudResourceProvisioning.requestResource(
      resourceType,
      quantity,
      {
        from: requester,
      }
    )

    const resourceId = tx.logs[0].args.resourceId
    const resource = await cloudResourceProvisioning.resources(resourceId)

    assert.equal(
      resource.requester,
      requester,
      'Requester address is incorrect'
    )
    assert.equal(
      resource.resourceType,
      resourceType,
      'Resource type is incorrect'
    )
    assert.equal(
      resource.quantity.toNumber(),
      quantity,
      'Resource quantity is incorrect'
    )
    assert.equal(
      resource.isApproved,
      false,
      'Resource should not be approved initially'
    )
  })

  it('should approve a resource request', async () => {
    const resourceId = 1 // Assuming resource ID 1 was generated in the previous test case
    const admin = accounts[0]

    await cloudResourceProvisioning.approveResourceRequest(resourceId, {
      from: admin,
    })
    const resource = await cloudResourceProvisioning.resources(resourceId)

    assert.equal(
      resource.isApproved,
      true,
      'Resource approval status is incorrect'
    )
  })
})
