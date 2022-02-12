# Gitlab Pipeline

Some explanations on what is going on through the CI/CD process

## Merge Requests

Merge requests (or pull requests) are going to be merged (usually) to the master branch, therefore, it all code should be in the most final state possible. So, every step should pass in order to accept the merge request.

- Check for black formatting
- Performed unit tests
- Performe Sonar coverage test

## Master Branch

This is the production branch and must be at peek quality.
The first steps are the same as the, Merge Request to make sure the conditions are perfect before going live. After that, we deploy a preview version, in order for live testing and assertion that nothing went wrong on the deployment.

- Check for black formatting
- Performed unit tests
- Performe Sonar coverage test
- Deploy preview version

The next steps should be performed manually after the Preview version has been thoroughly tested.

- Deploy production version
- Remove preview version

## Dev Branch

This branch is to be used for testing unringed, with tests and validations being made, but not stopping the deployment even on failure.

- Check for black formatting
- Performed unit tests
- Performe Sonar coverage test
- Deploy develop version
  
## Other branches

These branches created for issues and stories on Jira. They should be treated as "going to production" and should stand to the highest degree of quality. Of course, you could also make a Pull Request to the dev branch in order to test the deployment, just be careful not to select "Delete Merge on Branch" and lose you progress :|

Those, by themselves, do not have any CI/CD steps associated to them