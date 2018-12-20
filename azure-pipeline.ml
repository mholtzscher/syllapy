jobs:

- job: 'Test'
  pool:
    vmImage: 'Ubuntu 16.04'
  strategy:
    matrix:
      Python37:
        python.version: '3.7'
    maxParallel: 4

  steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '$(python.version)'
      architecture: 'x64'

  - script: |
      python -m pip install --upgrade pip poetry
      poetry config settings.virtualenvs.create false
    displayName: 'setup'
  - script: poetry install && poetry develop
    displayName: 'install dependencies'

  - script: |
      python3 -m pytest --cov=syllapy/ --doctest-modules --junitxml=junit/test-results.xml
    displayName: 'pytest'
  - task: PublishTestResults@2
    inputs:
      testResultsFiles: '**/test-results.xml'
      testRunTitle: 'Python $(python.version)'
    condition: succeededOrFailed()
