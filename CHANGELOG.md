# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.0.0] - 2022-12-08

### Added
- Hiding console cursor
- Showing console cursor
- Supporting hide and show functionality on Unix platforms
- Supporting hide and show functionality on Windows platforms
- Unique function for handling cursor on Unix platforms: `cursorshandlerforunix()`
- Unique function for handling cursor on Windows platforms: `cursorshandlerforwindows()``
- Custom error for a case when termcursor runs on a not supported platform: `errors.NotSupportedPlatform`
- Custom error for a case when a wrong parameter value were given: `errors.WrongParamaterValue`
- Package importing is based on the operation system
- Structure class for dll handling on Windows platforms only: `structures._CursorInfoForWindows`
- Constants for the supported platforms: `constants.OperationSystem`
- Constants for the available visibility values on Unix platforms: `constants.VisibilityOnUnix`
- Constants for the available visibility values on Windows platforms: `constants.VisibilityOnWindows`
- Constants for handling a specified standard device: `constants.StdHandle`
- Check if it used as a module or a script and throw an error when using as a script
- Start using CHANGELOG as CHANGELOG.md
- Start using README as README.md
- Start using REQUIREMENTS as requirements.txt
- Set license as MIT
