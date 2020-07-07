const {
  runSetupCommand,
  performHealthCheck,
  allUp,
  Service,
  SetupCommand
} = require('./setup')

const { LibsWrapper } = require('./libs')
const { addUser, upgradeToCreator, getUser } = require('./commands/users')
const { uploadTrack, getTrackMetadata } = require('./commands/tracks')
const { verifyCIDExistsOnCreatorNode } = require('./commands/files')

module.exports = {
  runSetupCommand,
  performHealthCheck,
  LibsWrapper,
  addUser,
  upgradeToCreator,
  uploadTrack,
  getTrackMetadata,
  getUser,
  verifyCIDExistsOnCreatorNode,
  allUp,
  Service,
  SetupCommand
}
