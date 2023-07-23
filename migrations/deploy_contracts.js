const CloudResourceProvisioning = artifacts.require('CloudResourceProvisioning')
const CloudResourceManagement = artifacts.require('CloudResourceManagement')

module.exports = function (_deployer) {
  _deployer.deploy(CloudResourceProvisioning)
  _deployer.deploy(CloudResourceManagement)
}
